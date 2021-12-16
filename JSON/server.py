import os
import sys
import json
import socket 
from dotenv import load_dotenv

# Enable Import File From Outside Folder
sys.path.append("..")
from request_input import write_warning_message
from response_output import get_file_name, read_data_samples

# Script Starting Point
if __name__ == '__main__':
    # Load Env to Get Port and Hostname Env Variables
    load_dotenv()
    PORT = int(os.getenv("PORT"))
    HOSTNAME = os.getenv("HOSTNAME")

    # Initialize Socket using 
    #   - AF_INET6 (Address Family Internet for IPv6) Specifying the Address Family 
    #   - SOCK_STREAM Specifying Connection Type As TCP
    # Using With Statement Closes Socket When With Statement is Complete
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Bind Hostname Address and Port Number to Socket
            s.bind((HOSTNAME, PORT))

            # Open TCP Connection
            s.listen()

            print("Server Listening...\n")

            # Accept Client Connection
            # - Connection Represents Client Socket Object
            # - Address Represents Client IPv6 Address
            connection, address = s.accept()
            print("Server Connected!\n")

            with connection:
                while True:
                    # Receive Data from Client Connection
                    # 1024 Represents Buffer Size in Bytes
                    data = connection.recv(1024)

                    # Break and Close Server Socket When Client Socket Closes
                    if not data:
                        break

                    # Deserialize and Print Request
                    print("Request Received!")

                    req = json.loads(data.decode('utf-8'))
                    print(req)

                    print("\nPerfoming Request ...")


                    # Get File to Read
                    file_name = get_file_name(req['benchmark_type'], req['data_type'])


                    # Get Data Samples By Reading File and Iterating Over Request Batch Range
                    data_samples = read_data_samples(file_name, req['batch_unit'], req['batch_size'], req['batch_id'], req['workload_metric'])

                    last_batch_id = req['batch_id'] + req['batch_size'] - 1
                    
                    # Serialize Response
                    rfd = {"rfw_id": req['rfw_id'], "last_batch_id": last_batch_id, "data_samples": data_samples} 
                    res = json.dumps(rfd)

                    # Send All Data Back to Client Socket
                    connection.sendall(res.encode('utf-8'))

                    print("\nResponse Sent!\n")
                    print(res)
                    
                    print("\nWaiting for Another Request ...\n")

        except KeyboardInterrupt:
            # Close Socket on Keyboard Interrupt Before Ending Program
            write_warning_message("Closing Socket due to Keyboard Interrupt! (Ctrl C)")
    
    print("Server Socket Closed!\n")