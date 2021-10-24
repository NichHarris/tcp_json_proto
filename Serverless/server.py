# Serverless Architecture - Function Based
class WorkloadServicer(pb_grpc.WorkloadServiceServicer):
    def Workload(self, request, context):
        # Request For Workload
        rfw_id = request.rfw_id
        benchmark_type = request.benchmark_type
        workload_metric = request.workload_metric
        batch_id = request.batch_id
        batch_size = request.batch_seize
        data_type = request.data_type

        # TODO: Write Method to Take the Response Arguments to Get RFD Arguments
    
        # Expected Return Response
        # return pb.WorkloadRFD(rfw_id, last_batch_id, requested_data_samples)
        
        # Since Method to Get RFD Arguments Not in Place, Return Back the RFW for Now
        return pb.WorkloadRFW(rfw_id, benchmark_type, workload_metric, batch_id, batch_size, data_type)