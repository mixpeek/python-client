# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmbedCreateParams"]


class EmbedCreateParams(TypedDict, total=False):
    input: Required[str]
    """The input data to be processed."""

    input_type: Optional[Literal["text", "base64", "url"]]
    """The type of input data. Can be text, base64, or url."""

    modality: Optional[Literal["video", "image"]]
    """The modality of the input data."""

    model_id: Optional[object]
    """The model to be used for processing."""

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
