import os
import sys
import json
import socket
import workload_pb2 as pb
from google.protobuf.json_format import MessageToJson
from dotenv import load_dotenv

# Enable Import File From Outside Folder
sys.path.append("..")
from request_input import write_warning_message, make_request, keep_connection

# Write to File Request and Response
def write_file_output(data_id, data_type, content):
    with open(f"../Output/{data_id}/{data_type}_{data_id}.json", "w") as file:
        json.dump(MessageToJson(content), file)

# Script Starting Point
if __name__ == '__main__':
    # Load Env to Get Port and Hostname Env Variables
    load_dotenv()
    PORT = int(os.getenv("PORT"))
    HOSTNAME = os.getenv("HOSTNAME")

    # Initialize Socket and Open TCP Connection
    #   - AF_INET6 (Address Family Internet for IPv6) Specifying the Address Family 
    #   - SOCK_STREAM Specifying Connection Type As TCP
    # Using With Statement Closes Socket When With Statement is Complete
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to Server Socket
            s.connect((HOSTNAME, PORT))
            
            print("Client Connected!\n")

            has_reqs = True
            while has_reqs:
                # Get User Input for Request
                rfw_id, benchmark_type, workload_metric, batch_unit, batch_size, batch_id, data_type = make_request() 

                # Create Folder to Store Request and Response
                os.mkdir(f"../Output/{rfw_id}")

                # Serialize Request
                rfw = pb.WorkloadRFW(rfw_id = rfw_id, benchmark_type = benchmark_type, workload_metric = workload_metric, batch_unit = batch_unit, batch_id = batch_id, batch_size = batch_size, data_type = data_type)
                req = rfw.SerializeToString()

                # Write Request to File
                write_file_output(rfw_id, "rfw", rfw)

                # Send Request to Server
                s.sendall(req)
                
                # Notify User Request Sent
                print("\nRequest Sent!")
                print(req)
                print("\nWaiting for Response ...\n")

                # Receive Response from Server
                # 1024 Represents Buffer Size in Bytes
                data = s.recv(1024)

                # Deserialize Response
                res = pb.WorkloadRFD()
                res.ParseFromString(data)

                # Print Response
                print("Response Received!")
                print(res)

                # Write Response to File
                write_file_output(rfw_id, "rfd", res)

                # Continue Loop If More Requests Are to Be Done
                has_reqs = keep_connection()

        except KeyboardInterrupt:
            # Close Socket on Keyboard Interrupt Before Ending Program
            write_warning_message("Closing Socket due to Keyboard Interrupt! (Ctrl C)")
        except Exception:
            # Could Not Connect to Server Socket 
            write_warning_message("Failed to Connect to Server Socket! Must Run Server Before Running Client!")

    print("\nClient Socket Closed!\n")