# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import digestor_pb2 as digestor__pb2


class DigestorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDigestor = channel.unary_unary(
                '/digestor.Digestor/GetDigestor',
                request_serializer=digestor__pb2.DigestMessage.SerializeToString,
                response_deserializer=digestor__pb2.DigestedMessage.FromString,
                )


class DigestorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDigestor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DigestorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDigestor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDigestor,
                    request_deserializer=digestor__pb2.DigestMessage.FromString,
                    response_serializer=digestor__pb2.DigestedMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'digestor.Digestor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Digestor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDigestor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/digestor.Digestor/GetDigestor',
            digestor__pb2.DigestMessage.SerializeToString,
            digestor__pb2.DigestedMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
