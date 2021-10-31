import grpc 
import csv
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

        print("Request Received! Perfoming Request ...")
        print(request)

        # Convert Numbers to Actual Values
        if benchmark_type == True:
            benchmark_type = "DVD"
        else: 
            benchmark_type = "NDBench"

        if data_type == True:
            data_type = "training"
        else: 
            data_type = "testing"

        # Get File to Read
        fileName = f"../data/{benchmark_type}-{data_type}.csv"

        data_samples = []
        # Read File Line By Line
        with open(fileName, mode = 'r') as file:
            csvReader = csv.reader(file)

            # Convert to List to Access Rows and Columns
            csvRows = list(csvReader)
            
            # Number of Batches = Number of Samples / Batch Unit
            numSamples = csvReader.line_num - 1
            numBatches = numSamples/batch_unit

            startRecord = batch_id * batch_unit
            endRecord = startRecord + batch_size * batch_unit - 1

            workload_metric_index = workload_metric - 1

            for record_index in range(startRecord, endRecord): 
                data_samples.append(float(csvRows[record_index][workload_metric_index]))

        last_batch_id = batch_id + batch_size - 1

        # Return Response
        return pb.WorkloadRFD(rfw_id = rfw_id, last_batch_id = last_batch_id, requested_data_samples = data_samples)

# Code From GRPC Python Guide Repo (https://github.com/grpc/grpc/blob/v1.30.0/examples/python/route_guide/route_guide_server.py) 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_WorkloadServiceServicer_to_server( WorkloadServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
