# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import marketdata_pb2 as tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2


class MarketDataServiceStub(object):
    """Сервис получения биржевой информации:</br> **1**. свечи;</br> **2**. стаканы;</br> **3**. торговые статусы;</br> **4**. лента сделок.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCandles = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesResponse.FromString,
                )
        self.GetLastPrices = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetLastPrices',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesResponse.FromString,
                )
        self.GetOrderBook = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetOrderBook',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookResponse.FromString,
                )
        self.GetTradingStatus = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetTradingStatus',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusResponse.FromString,
                )
        self.GetLastTrades = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetLastTrades',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesResponse.FromString,
                )


class MarketDataServiceServicer(object):
    """Сервис получения биржевой информации:</br> **1**. свечи;</br> **2**. стаканы;</br> **3**. торговые статусы;</br> **4**. лента сделок.
    """

    def GetCandles(self, request, context):
        """Метод запроса исторических свечей по инструменту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastPrices(self, request, context):
        """Метод запроса последних цен по инструментам.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderBook(self, request, context):
        """Метод получения стакана по инструменту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTradingStatus(self, request, context):
        """Метод запроса статуса торгов по инструментам.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastTrades(self, request, context):
        """Метод запроса последних обезличенных сделок по инструменту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCandles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCandles,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesResponse.SerializeToString,
            ),
            'GetLastPrices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastPrices,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesResponse.SerializeToString,
            ),
            'GetOrderBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderBook,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookResponse.SerializeToString,
            ),
            'GetTradingStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTradingStatus,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusResponse.SerializeToString,
            ),
            'GetLastTrades': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastTrades,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.MarketDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketDataService(object):
    """Сервис получения биржевой информации:</br> **1**. свечи;</br> **2**. стаканы;</br> **3**. торговые статусы;</br> **4**. лента сделок.
    """

    @staticmethod
    def GetCandles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetCandlesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetLastPrices',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastPricesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetOrderBook',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetOrderBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTradingStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetTradingStatus',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetTradingStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastTrades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.MarketDataService/GetLastTrades',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.GetLastTradesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MarketDataStreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MarketDataStream = channel.stream_stream(
                '/tinkoff.public.invest.api.contract.v1.MarketDataStreamService/MarketDataStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataResponse.FromString,
                )


class MarketDataStreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MarketDataStream(self, request_iterator, context):
        """Bi-directional стрим предоставления биржевой информации.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketDataStreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MarketDataStream': grpc.stream_stream_rpc_method_handler(
                    servicer.MarketDataStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.MarketDataStreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketDataStreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MarketDataStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tinkoff.public.invest.api.contract.v1.MarketDataStreamService/MarketDataStream',
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_marketdata__pb2.MarketDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
