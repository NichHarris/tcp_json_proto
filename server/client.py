import grpc
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

import socket 

PORT = 65432
HOSTNAME = '127.0.0.1'

# TCP Connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to Server Socket
    s.connect((HOSTNAME, PORT))

    # Send Request to Server
    s.sendall("Sending Request")

    # Receive Response from Server
    # 1024 Represents Buffer Size in Bytes
    data = s.recv(1024)


# Serverless Architecture
# Set Up a Channel/Connection to Server
with grpc.insecure_channel("localhost:50051") as c:
    # Create Stub to First Connect to Server then Send Request and Retrieve Response
    stub = pb_grpc.WorkloadServiceStub(c)

    # Request Arguments 
    rfw_id = 1
    benchmark_type = False
    workload_metric = 2
    batch_id = 1
    batch_size = 5
    data_type = True

    # TODO: Request Here
    req = pb.WorkloadRFW(rfw_id, benchmark_type, workload_metric, batch_id, batch_size, data_type)

    # TODO: Response Here
    res = stub.WorkloadRFD(req)

    # Print Request and Response Data
    print(f"RFW: {req}, \nRFD: {res}")
