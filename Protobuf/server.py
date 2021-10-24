#import grpc
#import workload_pb2 as pb
#import workload_pb2_grpc as pb_grpc

import os
import socket
from dotenv import load_dotenv

# Load Env, then Get Port and Hostname Env Variables
load_dotenv()
PORT = int(os.getenv("PORT"))
HOSTNAME = os.getenv("HOSTNAME")

# Initialize Socket using 
#   - AF_INET6 (Address Family Internet for IPv6) Specifying the Address Family 
#   - SOCK_STREAM Specifying Connection Type As TCP
# Using With Statement Closes Socket When With Statement is Complete
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    # Bind Hostname Address and Port Number to Socket
    s.bind((HOSTNAME, PORT))

    # Open TCP Connection
    s.listen()

    # Accept Client Connection
    # - Connection Represents Client Socket Object
    # - Address Represents Client IPv6 Address
    connection, address = s.accept()

    with connection:
        while True:
            # Receive Data from Client Connection
            # 1024 Represents Buffer Size in Bytes
            data = connection.recv(1024)

            # TODO: Deserialize Request


            # Read from Corresponding File

            # TODO: Serialize Response

            # Break Condition
            if not data:
                break

            # Send All Data Back to Client Socket
            connection.sendall(data)

# # Serverless Architecture - Function Based
# class WorkloadServicer(pb_grpc.WorkloadServiceServicer):
#     def Workload(self, request, context):
#         # Request For Workload
#         rfw_id = request.rfw_id
#         benchmark_type = request.benchmark_type
#         workload_metric = request.workload_metric
#         batch_id = request.batch_id
#         batch_size = request.batch_seize
#         data_type = request.data_type

#         # TODO: Write Method to Take the Response Arguments to Get RFD Arguments
#         # - Not Sure What to do In Between So Far Will Just Return the Request

#         # Expected Return Response
#         # return pb.WorkloadRFD(rfw_id, last_batch_id, requested_data_samples)
        
#         # Since Method to Get RFD Arguments Not in Place, Return Back the RFW for Now
#         return pb.WorkloadRFW(rfw_id, benchmark_type, workload_metric, batch_id, batch_size, data_type)
