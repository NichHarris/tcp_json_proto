import os
import sys
import csv
import socket 
import workload_pb2 as pb
from dotenv import load_dotenv

# Enable Import File From Outside Folder
sys.path.append("..")
from request_input import write_warning_message

# Get File Name from Benchmark and Data Types
def get_file_name(benchmark_type, data_type): 
    # Convert Boolean to Actual Values
    benchmark_type = "DVD" if req.benchmark_type else "NDBench"
    data_type = "training" if req.data_type else "testing"

    # Return File to Read
    return f"../data/{benchmark_type}-{data_type}.csv"

# Read File And Get Data Samples
def read_data_samples(file_name, batch_unit, batch_size, batch_id, workload_metric): 
    data_samples = []
    
    # Read File Line By Line
    with open(file_name, mode = 'r') as file:
        csv_reader = csv.reader(file)

        # Convert to List to Access Rows and Columns
        csv_rows = list(csv_reader)
        
        # Number of Batches = Number of Samples / Batch Unit
        num_samples = csv_reader.line_num - 1
        num_batches = num_samples/batch_unit

        # Start and End Indices User Requested
        start_record = batch_id * batch_unit
        end_record = start_record + batch_size * batch_unit - 1

        # Iterate Over File and Add All Data Samples from Requested Range
        for record_index in range(start_record, end_record): 
            data_samples.append(float(csv_rows[record_index][workload_metric - 1]))
    
    return data_samples

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

                    print("Request Received!")

                    # Deserialize and Print Request
                    req = pb.WorkloadRFW()
                    req.ParseFromString(data)
                    print(req)

                    print("\nPerfoming Request ...")

                    # Get File to Read
                    file_name = get_file_name(req.benchmark_type, req.data_type)

                    # Get Data Samples By Reading File and Iterating Over Request Batch Range
                    data_samples = read_data_samples(file_name, req.batch_unit, req.batch_size, req.batch_id, req.workload_metric)

                    # Calculate Last Batch Id        
                    last_batch_id = req.batch_id + req.batch_size - 1

                    # Serialize Response
                    rfd = pb.WorkloadRFD(rfw_id = req.rfw_id, last_batch_id = last_batch_id, requested_data_samples = data_samples)
                    res = rfd.SerializeToString()

                    # Send All Data Back to Client Socket
                    connection.sendall(res)
                    print("\nResponse Sent!")
                    print(res)

                    print("\nWaiting for Another Request ...\n")

        except KeyboardInterrupt:
            # Close Socket on Keyboard Interrupt Before Ending Program
            write_warning_message("Closing Socket due to Keyboard Interrupt! (Ctrl C)")
    
    print("Server Socket Closed!\n")