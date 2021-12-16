import sys
import grpc 
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

# Parallel Threads
from concurrent import futures 

# Enable Import File From Outside Folder
sys.path.append("..")
from response_output import get_file_name, read_data_samples

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

        print("Request Received! Performing Request ...")
        print(request)

        # Get File to Read
        file_name = get_file_name(benchmark_type, data_type)

        # Get Data Samples By Reading File and Iterating Over Request Batch Range
        data_samples = read_data_samples(file_name, batch_unit, batch_size, batch_id, workload_metric)
        last_batch_id = batch_id + batch_size - 1

        print("Request Completed!\n")

        # Return Response
        return pb.WorkloadRFD(rfw_id = rfw_id, last_batch_id = last_batch_id, requested_data_samples = data_samples)

# Script Starting Point
if __name__ == '__main__':
    # Create a Server to Service Remote Procedure Calls (RPCs) w/ Multiple Threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_WorkloadServiceServicer_to_server(WorkloadServiceServicer(), server)

    # Open Server Port for RPCs
    server.add_insecure_port('[::]:50051')

    # Start Server
    server.start()
    server.wait_for_termination()