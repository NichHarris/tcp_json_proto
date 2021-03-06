# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import workload_pb2 as workload__pb2


class WorkloadServiceStub(object):
    """Define Service with Remote Procedure Call (RPC) 
    Workload Method Takes in Request for Workload (RFW) And Returns Response for Data (RFD)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Workload = channel.unary_unary(
                '/WorkloadService/Workload',
                request_serializer=workload__pb2.WorkloadRFW.SerializeToString,
                response_deserializer=workload__pb2.WorkloadRFD.FromString,
                )


class WorkloadServiceServicer(object):
    """Define Service with Remote Procedure Call (RPC) 
    Workload Method Takes in Request for Workload (RFW) And Returns Response for Data (RFD)
    """

    def Workload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkloadServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Workload': grpc.unary_unary_rpc_method_handler(
                    servicer.Workload,
                    request_deserializer=workload__pb2.WorkloadRFW.FromString,
                    response_serializer=workload__pb2.WorkloadRFD.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WorkloadService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkloadService(object):
    """Define Service with Remote Procedure Call (RPC) 
    Workload Method Takes in Request for Workload (RFW) And Returns Response for Data (RFD)
    """

    @staticmethod
    def Workload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WorkloadService/Workload',
            workload__pb2.WorkloadRFW.SerializeToString,
            workload__pb2.WorkloadRFD.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
