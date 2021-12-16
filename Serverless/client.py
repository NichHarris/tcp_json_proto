import os
import sys
import grpc 
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

from dotenv import load_dotenv

# Enable Import File From Outside Folder
sys.path.append("..")
from request_input import make_request, keep_connection

# Script Starting Point
if __name__ == '__main__':
    # Load Env to Get Server Address
    load_dotenv()
    SERVER_ADDR = os.getenv("SERVER_ADDR")

    # Set Up a Channel/HTTP Connection to Server with GRPC
    with grpc.insecure_channel(SERVER_ADDR) as c:
        # Create Stub to First Connect to Server then Send Request and Retrieve Response
        stub = pb_grpc.WorkloadServiceStub(c)

        has_reqs = True
        while has_reqs:
            # Get User Input for Request
            rfw_id, benchmark_type, workload_metric, batch_unit, batch_size, batch_id, data_type = make_request() 

            # Serialize Req with Protobuf
            req = pb.WorkloadRFW(rfw_id = rfw_id, benchmark_type = benchmark_type, workload_metric = workload_metric, batch_unit = batch_unit, batch_id = batch_id, batch_size = batch_size, data_type = data_type)

            print("\nRequest Sent to Serverless Function: ")
            print(req)

            # Call Workload RPC using Stub to Get Response
            res = stub.Workload(req)

            # Print Response
            print("Response Obtained from Serverless Function: ")
            print(res)

            # Continue Loop If More Requests Are to Be Done
            has_reqs = keep_connection()

    print("\nConnection Closed!\n")
