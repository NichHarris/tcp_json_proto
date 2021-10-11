import grpc
import workload_pb2 as pb
import workload_pb2_grpc as pb_grpc

class WorkloadServicer(pb_grpc.WorkloadServiceServicer):
    def Workload(self, request, context):
        # Request For Workload
        rfw_id = request.rfw_id
        benchmark_type = request.benchmark_type
        workload_metric = request.workload_metric
        batch_id = request.batch_id
        batch_size = request.batch_seize
        data_type = request.data_type

        # Response For Data Like This in Comment - Not Sure What to do In Between So Far Will Just Return the Request
        # return pb.WorkloadRFD(rfd_id, last_batch_id, requested_data_samples)
        return pb.WorkloadRFW(rfw_id, benchmark_type, workload_metric, batch_id, batch_size, data_type)