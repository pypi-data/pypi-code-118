# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from common.api.services.common import common_pb2 as services_dot_common_dot_common__pb2
from common.api.services.explore import explore_pb2 as services_dot_explore_dot_explore__pb2
from common.api.services.post import post_pb2 as services_dot_post_dot_post__pb2


class ExploreServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/social.explore.ExploreService/Ping',
                request_serializer=services_dot_common_dot_common__pb2.Empty.SerializeToString,
                response_deserializer=services_dot_common_dot_common__pb2.Pong.FromString,
                )
        self.GetFeed = channel.unary_unary(
                '/social.explore.ExploreService/GetFeed',
                request_serializer=services_dot_common_dot_common__pb2.Pagination.SerializeToString,
                response_deserializer=services_dot_post_dot_post__pb2.PostListResponse.FromString,
                )
        self.GeoSearch = channel.unary_unary(
                '/social.explore.ExploreService/GeoSearch',
                request_serializer=services_dot_explore_dot_explore__pb2.GeoSearchRequest.SerializeToString,
                response_deserializer=services_dot_explore_dot_explore__pb2.GeoSearchResponse.FromString,
                )


class ExploreServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeoSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExploreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=services_dot_common_dot_common__pb2.Empty.FromString,
                    response_serializer=services_dot_common_dot_common__pb2.Pong.SerializeToString,
            ),
            'GetFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeed,
                    request_deserializer=services_dot_common_dot_common__pb2.Pagination.FromString,
                    response_serializer=services_dot_post_dot_post__pb2.PostListResponse.SerializeToString,
            ),
            'GeoSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.GeoSearch,
                    request_deserializer=services_dot_explore_dot_explore__pb2.GeoSearchRequest.FromString,
                    response_serializer=services_dot_explore_dot_explore__pb2.GeoSearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'social.explore.ExploreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExploreService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/social.explore.ExploreService/Ping',
            services_dot_common_dot_common__pb2.Empty.SerializeToString,
            services_dot_common_dot_common__pb2.Pong.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/social.explore.ExploreService/GetFeed',
            services_dot_common_dot_common__pb2.Pagination.SerializeToString,
            services_dot_post_dot_post__pb2.PostListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeoSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/social.explore.ExploreService/GeoSearch',
            services_dot_explore_dot_explore__pb2.GeoSearchRequest.SerializeToString,
            services_dot_explore_dot_explore__pb2.GeoSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
