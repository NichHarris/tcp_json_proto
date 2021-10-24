# import grpc
# import workload_pb2 as pb
# import workload_pb2_grpc as pb_grpc

import os
import sys
import socket 
from dotenv import load_dotenv

# Load Env, then Get Port and Hostname Env Variables
load_dotenv()
PORT = int(os.getenv("PORT"))
HOSTNAME = os.getenv("HOSTNAME")

# Print Warning Message with Different Colors
WARNING = "\033[1;31m"
RESET = "\033[0;0m"
def writeWarningMessage(msg):
    sys.stdout.write(WARNING)
    print(msg)
    sys.stdout.write(RESET)

# Initialize Socket and Open TCP Connection
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    # Connect to Server Socket
    s.connect((HOSTNAME, PORT))

    # Read User Input to Create Request
    rfw_id = int(input("Enter RFW ID: "))

    # Used to Validate Request
    isValidated = False
    while not isValidated:
        benchmark_type = input("Enter Benchmark Type As 1 (DVD) Or 2 (NDBench): ").strip()
            
        # Validate Benchmark Type from Input
        if benchmark_type == "1":
            benchmark_type = "DVD"
            isValidated = not isValidated
        elif benchmark_type == "2":
            benchmark_type = "NDBench"
            isValidated = not isValidated
        else: 
            writeWarningMessage("\nInvalid Benchmark Type! Must Enter Either 1 or 2! \n")

    
    isValidated = False
    while not isValidated:
        workload_metric = input("Enter Workload Metric As 1 (CPU Utilization Average), 2 (Network In Average),\n 3 (Network Out Average) Or 4 (Memory Utilization Average): ").strip()

        # Validate Worklod Metric from Input
        if workload_metric == "1":
            workload_metric = "CPUUtilization_Average"
            isValidated = not isValidated
        elif workload_metric == "2":
            workload_metric = "NetworkIn_Average"
            isValidated = not isValidated
        elif workload_metric == "3":
            workload_metric = "NetworkOut_Average"
            isValidated = not isValidated
        elif workload_metric == "4":
            workload_metric = "MemoryUtilization_Average"
            isValidated = not isValidated
        else:
            writeWarningMessage("\nInvalid Workload Metric! Must Enter Either 1, 2, 3, or 4! \n")

    batch_id = int(input("Enter Batch Id: "))
    batch_size = int(input("Enter Batch Size: "))

    isValidated = False
    while not isValidated:
        data_type = input("Enter Data Type As 1 (Training) Or 2 (Testing): ").strip()
            
        # Validate Data Type from Input
        if data_type == "1":
            data_type = "training"
            isValidated = not isValidated
        elif data_type == "2":
            data_type = "testing"
            isValidated = not isValidated
        else: 
            writeWarningMessage("\nInvalid Data Type! Must Enter Either 1 or 2!\n")

    # Serialize Request
    rfw = {"rfw_id": rfw_id,  "benchmark_type": benchmark_type, "workload_metric": workload_metric, "batch_id": batch_id, "batch_size": batch_size, "data_type": data_type}
        
    # Send Request to Server
    #s.sendall(rfw)

    # Receive Response from Server
    # 1024 Represents Buffer Size in Bytes
    #data = s.recv(1024)

    # TODO: Deserialize Response

    # TODO: Print Response



# # Serverless Architecture
# # Set Up a Channel/Connection to Server
# with grpc.insecure_channel("localhost:50051") as c:
#     # Create Stub to First Connect to Server then Send Request and Retrieve Response
#     stub = pb_grpc.WorkloadServiceStub(c)

#     # Request Arguments 
#     rfw_id = 1
#     benchmark_type = False
#     workload_metric = 2
#     batch_id = 1
#     batch_size = 5
#     data_type = True

#     # TODO: Request Here
#     req = pb.WorkloadRFW(rfw_id, benchmark_type, workload_metric, batch_id, batch_size, data_type)

#     # TODO: Response Here
#     res = stub.WorkloadRFD(req)

#     # Print Request and Response Data
#     print(f"RFW: {req}, \nRFD: {res}")
