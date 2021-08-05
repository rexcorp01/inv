# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src import am_sma_pb2 as src_dot_am__sma__pb2
from src import backtest_pb2 as src_dot_backtest__pb2
from src import brinson_pb2 as src_dot_brinson__pb2


class MicroServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BrinsonHandler = channel.unary_unary(
                '/src.MicroService/BrinsonHandler',
                request_serializer=src_dot_brinson__pb2.Request.SerializeToString,
                response_deserializer=src_dot_brinson__pb2.Response.FromString,
                )
        self.SMAPortfolio = channel.unary_stream(
                '/src.MicroService/SMAPortfolio',
                request_serializer=src_dot_am__sma__pb2.NULL.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Portfolio.FromString,
                )
        self.SMABalance = channel.unary_stream(
                '/src.MicroService/SMABalance',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Balance.FromString,
                )
        self.SMABalanceExpanded = channel.unary_stream(
                '/src.MicroService/SMABalanceExpanded',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.BalanceExpanded.FromString,
                )
        self.SMAIncome = channel.unary_stream(
                '/src.MicroService/SMAIncome',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Income.FromString,
                )
        self.SMAIncomeAsset = channel.unary_stream(
                '/src.MicroService/SMAIncomeAsset',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.IncomeAsset.FromString,
                )
        self.SMAHolding = channel.unary_stream(
                '/src.MicroService/SMAHolding',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Holding.FromString,
                )
        self.SMATransaction = channel.unary_stream(
                '/src.MicroService/SMATransaction',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Transaction.FromString,
                )
        self.SMADetailFee = channel.unary_stream(
                '/src.MicroService/SMADetailFee',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.DetailFee.FromString,
                )
        self.SMASecurity = channel.unary_stream(
                '/src.MicroService/SMASecurity',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Security.FromString,
                )
        self.SMASecurityQuote = channel.unary_stream(
                '/src.MicroService/SMASecurityQuote',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.SecurityQuote.FromString,
                )
        self.SMABenchmark = channel.unary_stream(
                '/src.MicroService/SMABenchmark',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.Benchmark.FromString,
                )
        self.SMAInterestTax = channel.unary_stream(
                '/src.MicroService/SMAInterestTax',
                request_serializer=src_dot_am__sma__pb2.Request.SerializeToString,
                response_deserializer=src_dot_am__sma__pb2.InterestTax.FromString,
                )
        self.Backtest = channel.unary_unary(
                '/src.MicroService/Backtest',
                request_serializer=src_dot_backtest__pb2.Request.SerializeToString,
                response_deserializer=src_dot_backtest__pb2.Response.FromString,
                )


class MicroServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BrinsonHandler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMAPortfolio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMABalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMABalanceExpanded(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMAIncome(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMAIncomeAsset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMAHolding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMATransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMADetailFee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMASecurity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMASecurityQuote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMABenchmark(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SMAInterestTax(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Backtest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MicroServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BrinsonHandler': grpc.unary_unary_rpc_method_handler(
                    servicer.BrinsonHandler,
                    request_deserializer=src_dot_brinson__pb2.Request.FromString,
                    response_serializer=src_dot_brinson__pb2.Response.SerializeToString,
            ),
            'SMAPortfolio': grpc.unary_stream_rpc_method_handler(
                    servicer.SMAPortfolio,
                    request_deserializer=src_dot_am__sma__pb2.NULL.FromString,
                    response_serializer=src_dot_am__sma__pb2.Portfolio.SerializeToString,
            ),
            'SMABalance': grpc.unary_stream_rpc_method_handler(
                    servicer.SMABalance,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Balance.SerializeToString,
            ),
            'SMABalanceExpanded': grpc.unary_stream_rpc_method_handler(
                    servicer.SMABalanceExpanded,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.BalanceExpanded.SerializeToString,
            ),
            'SMAIncome': grpc.unary_stream_rpc_method_handler(
                    servicer.SMAIncome,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Income.SerializeToString,
            ),
            'SMAIncomeAsset': grpc.unary_stream_rpc_method_handler(
                    servicer.SMAIncomeAsset,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.IncomeAsset.SerializeToString,
            ),
            'SMAHolding': grpc.unary_stream_rpc_method_handler(
                    servicer.SMAHolding,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Holding.SerializeToString,
            ),
            'SMATransaction': grpc.unary_stream_rpc_method_handler(
                    servicer.SMATransaction,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Transaction.SerializeToString,
            ),
            'SMADetailFee': grpc.unary_stream_rpc_method_handler(
                    servicer.SMADetailFee,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.DetailFee.SerializeToString,
            ),
            'SMASecurity': grpc.unary_stream_rpc_method_handler(
                    servicer.SMASecurity,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Security.SerializeToString,
            ),
            'SMASecurityQuote': grpc.unary_stream_rpc_method_handler(
                    servicer.SMASecurityQuote,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.SecurityQuote.SerializeToString,
            ),
            'SMABenchmark': grpc.unary_stream_rpc_method_handler(
                    servicer.SMABenchmark,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.Benchmark.SerializeToString,
            ),
            'SMAInterestTax': grpc.unary_stream_rpc_method_handler(
                    servicer.SMAInterestTax,
                    request_deserializer=src_dot_am__sma__pb2.Request.FromString,
                    response_serializer=src_dot_am__sma__pb2.InterestTax.SerializeToString,
            ),
            'Backtest': grpc.unary_unary_rpc_method_handler(
                    servicer.Backtest,
                    request_deserializer=src_dot_backtest__pb2.Request.FromString,
                    response_serializer=src_dot_backtest__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'src.MicroService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MicroService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BrinsonHandler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/src.MicroService/BrinsonHandler',
            src_dot_brinson__pb2.Request.SerializeToString,
            src_dot_brinson__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMAPortfolio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMAPortfolio',
            src_dot_am__sma__pb2.NULL.SerializeToString,
            src_dot_am__sma__pb2.Portfolio.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMABalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMABalance',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Balance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMABalanceExpanded(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMABalanceExpanded',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.BalanceExpanded.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMAIncome(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMAIncome',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Income.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMAIncomeAsset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMAIncomeAsset',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.IncomeAsset.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMAHolding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMAHolding',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Holding.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMATransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMATransaction',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Transaction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMADetailFee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMADetailFee',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.DetailFee.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMASecurity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMASecurity',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Security.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMASecurityQuote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMASecurityQuote',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.SecurityQuote.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMABenchmark(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMABenchmark',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.Benchmark.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SMAInterestTax(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/src.MicroService/SMAInterestTax',
            src_dot_am__sma__pb2.Request.SerializeToString,
            src_dot_am__sma__pb2.InterestTax.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Backtest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/src.MicroService/Backtest',
            src_dot_backtest__pb2.Request.SerializeToString,
            src_dot_backtest__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
