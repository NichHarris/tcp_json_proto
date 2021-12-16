import grpc 
import csv
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

# Parallel Threads
from concurrent import futures 

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

        print("Request Received! Perfoming Request ...")
        print(request)

        # Convert Boolean to Actual Values
        benchmark_type = "DVD" if benchmark_type else "NDBench"
        data_type = "training" if data_type else "testing"

        # Get File to Read
        file_name = f"../data/{benchmark_type}-{data_type}.csv"

        # Read File Line By Line
        data_samples = []
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

        last_batch_id = batch_id + batch_size - 1

        # Return Response
        return pb.WorkloadRFD(rfw_id = rfw_id, last_batch_id = last_batch_id, requested_data_samples = data_samples)

# Serverless Architecture - Function Based
# Code from GRPC Python Guide Repo 
# (https://github.com/grpc/grpc/blob/v1.30.0/examples/python/route_guide/route_guide_server.py) 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_WorkloadServiceServicer_to_server(WorkloadServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Script Starting Point
if __name__ == '__main__':
    serve()
