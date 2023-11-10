# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/privval/types.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass

import betterproto

from .. import crypto as _crypto__
from .. import types as _types__


class Errors(betterproto.Enum):
    ERRORS_UNKNOWN = 0
    ERRORS_UNEXPECTED_RESPONSE = 1
    ERRORS_NO_CONNECTION = 2
    ERRORS_CONNECTION_TIMEOUT = 3
    ERRORS_READ_TIMEOUT = 4
    ERRORS_WRITE_TIMEOUT = 5


@dataclass(eq=False, repr=False)
class RemoteSignerError(betterproto.Message):
    code: int = betterproto.int32_field(1)
    description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class PubKeyRequest(betterproto.Message):
    """PubKeyRequest requests the consensus public key from the remote signer."""

    chain_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PubKeyResponse(betterproto.Message):
    """PubKeyResponse is a response message containing the public key."""

    pub_key: "_crypto__.PublicKey" = betterproto.message_field(1)
    error: "RemoteSignerError" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class SignVoteRequest(betterproto.Message):
    """SignVoteRequest is a request to sign a vote"""

    vote: "_types__.Vote" = betterproto.message_field(1)
    chain_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SignedVoteResponse(betterproto.Message):
    """SignedVoteResponse is a response containing a signed vote or an error"""

    vote: "_types__.Vote" = betterproto.message_field(1)
    error: "RemoteSignerError" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class SignProposalRequest(betterproto.Message):
    """SignProposalRequest is a request to sign a proposal"""

    proposal: "_types__.Proposal" = betterproto.message_field(1)
    chain_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SignedProposalResponse(betterproto.Message):
    """SignedProposalResponse is response containing a signed proposal or an error"""

    proposal: "_types__.Proposal" = betterproto.message_field(1)
    error: "RemoteSignerError" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class SignRevealRequest(betterproto.Message):
    """SignRevealRequest is a request to sign a reveal"""

    reveal: "_types__.Reveal" = betterproto.message_field(1)
    chain_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SignedRevealResponse(betterproto.Message):
    """SignedRevealResponse is response containing a signed reveal or an error"""

    reveal: "_types__.Reveal" = betterproto.message_field(1)
    error: "RemoteSignerError" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class PingRequest(betterproto.Message):
    """PingRequest is a request to confirm that the connection is alive."""

    pass


@dataclass(eq=False, repr=False)
class PingResponse(betterproto.Message):
    """PingResponse is a response to confirm that the connection is alive."""

    pass


@dataclass(eq=False, repr=False)
class Message(betterproto.Message):
    pub_key_request: "PubKeyRequest" = betterproto.message_field(1, group="sum")
    pub_key_response: "PubKeyResponse" = betterproto.message_field(2, group="sum")
    sign_vote_request: "SignVoteRequest" = betterproto.message_field(3, group="sum")
    signed_vote_response: "SignedVoteResponse" = betterproto.message_field(4, group="sum")
    sign_proposal_request: "SignProposalRequest" = betterproto.message_field(5, group="sum")
    signed_proposal_response: "SignedProposalResponse" = betterproto.message_field(6, group="sum")
    sign_reveal_request: "SignRevealRequest" = betterproto.message_field(7, group="sum")
    sign_reveal_response: "SignedRevealResponse" = betterproto.message_field(8, group="sum")
    ping_request: "PingRequest" = betterproto.message_field(9, group="sum")
    ping_response: "PingResponse" = betterproto.message_field(10, group="sum")
