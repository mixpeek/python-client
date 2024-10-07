# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    prompt: Required[str]

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
