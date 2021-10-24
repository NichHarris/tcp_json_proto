import grpc 
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

# Serverless Architecture
# Set Up a Channel/HTTP Connection to Server
with grpc.insecure_channel("localhost:50051") as c:
    # Create Stub to First Connect to Server then Send Request and Retrieve Response
    stub = pb_grpc.WorkloadServiceStub(c)

    # Request Arguments 
    rfw_id = 1
    benchmark_type = False
    workload_metric = 2
    batch_unit = 3
    batch_id = 1
    batch_size = 5
    data_type = True

    # Request
    req = pb.WorkloadRFW(rfw_id = rfw_id, benchmark_type = benchmark_type, workload_metric = workload_metric, batch_unit = batch_unit, batch_id = batch_id, batch_size = batch_size, data_type = data_type)

    # Response
    res = stub.Workload(req) 

    # Print Request and Response Data
    print(f"RFW:\n{req} \nRFD:\n{res}")