import grpc
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

import socket 

PORT = 65432
HOSTNAME = '127.0.0.1'

# Initialize Socket and Open TCP Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to Server Socket
    s.connect((HOSTNAME, PORT))

    rfw_id = int(input("Enter RFD"))
    benchmark_type = int(input("Select one the following (enter the number): \n1. DVD\n2.NDBench"))
    workload_metric = int(input("Select from the following (enter number): \n1. CPU Utilization Average\n2. NetworkIn Average\n3. NetworkOut Average\n4. Memory Utilization Average"))
    batch_id = int(input("Enter the batch id: "))
    batch_unit = int(input("Enter the bach size"))
    data_type = int(input("Select one of the following (enter number): \n1. Training Data\n2. Testing Data"))

    if benchmark_type == 1:
        benchmark_type = "DVD"
    else:
        benchmark_type = "NDBench"

    if workload_metric == 1:
        workload_metric = "CPU"
    elif workload_metric == 2:
        workload_metric = "NetworkIn"
    elif workload_metric == 3:
        workload_metric = "NetworkOut"
    else:
        workload_metric = "Memory"

    if data_type == 1:
        data_type = "Training"
    else:
        data_type = "Testing"


        
    # Send Request to Server
    s.sendall("Sending Request")

    # Receive Response from Server
    # 1024 Represents Buffer Size in Bytes
    data = s.recv(1024)


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
