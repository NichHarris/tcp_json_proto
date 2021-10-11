import grpc
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

# Set Up a Channel/Connection to Server
# TODO: Move Channel Address to Env
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
