# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/rpc/grpc/types.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ... import abci as __abci__

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class RequestPing(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class RequestBroadcastTx(betterproto.Message):
    tx: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class ResponsePing(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ResponseBroadcastTx(betterproto.Message):
    check_tx: "__abci__.ResponseCheckTx" = betterproto.message_field(1)
    deliver_tx: "__abci__.ResponseDeliverTx" = betterproto.message_field(2)


class BroadcastApiStub(betterproto.ServiceStub):
    async def ping(
        self,
        request_ping: "RequestPing",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ResponsePing":
        return await self._unary_unary(
            "/tendermint.rpc.grpc.BroadcastAPI/Ping",
            request_ping,
            ResponsePing,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def broadcast_tx(
        self,
        request_broadcast_tx: "RequestBroadcastTx",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ResponseBroadcastTx":
        return await self._unary_unary(
            "/tendermint.rpc.grpc.BroadcastAPI/BroadcastTx",
            request_broadcast_tx,
            ResponseBroadcastTx,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class BroadcastApiBase(ServiceBase):
    async def ping(self, request_ping: "RequestPing") -> "ResponsePing":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def broadcast_tx(self, request_broadcast_tx: "RequestBroadcastTx") -> "ResponseBroadcastTx":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_ping(self, stream: "grpclib.server.Stream[RequestPing, ResponsePing]") -> None:
        request = await stream.recv_message()
        response = await self.ping(request)
        await stream.send_message(response)

    async def __rpc_broadcast_tx(
        self, stream: "grpclib.server.Stream[RequestBroadcastTx, ResponseBroadcastTx]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.broadcast_tx(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/tendermint.rpc.grpc.BroadcastAPI/Ping": grpclib.const.Handler(
                self.__rpc_ping,
                grpclib.const.Cardinality.UNARY_UNARY,
                RequestPing,
                ResponsePing,
            ),
            "/tendermint.rpc.grpc.BroadcastAPI/BroadcastTx": grpclib.const.Handler(
                self.__rpc_broadcast_tx,
                grpclib.const.Cardinality.UNARY_UNARY,
                RequestBroadcastTx,
                ResponseBroadcastTx,
            ),
        }