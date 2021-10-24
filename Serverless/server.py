import grpc 
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

# Parallel Threads
from concurrent import futures 

# Serverless Architecture - Function Based
class WorkloadServiceServicer(pb_grpc.WorkloadServiceServicer):
    def Workload(self, request, context):
        # Request For Workload Data
        rfw_id = request.rfw_id
        benchmark_type = request.benchmark_type
        workload_metric = request.workload_metric
        batch_unit = request.batch_unit
        batch_id = request.batch_id
        batch_size = request.batch_size
        data_type = request.data_type

        # TODO: Write Method to Take the Response Arguments to Get RFD Arguments
        last_batch_id = 2
        requested_data_samples = [1, 2.0, 3]

        # Expected Return Response
        return pb.WorkloadRFD(rfw_id = rfw_id, last_batch_id = last_batch_id, requested_data_samples = requested_data_samples)

# Code From GRPC Python Guide Repo (https://github.com/grpc/grpc/blob/v1.30.0/examples/python/route_guide/route_guide_server.py) 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_WorkloadServiceServicer_to_server( WorkloadServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()