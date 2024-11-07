# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FaceCreateParams"]


class FaceCreateParams(TypedDict, total=False):
    collection_id: Required[str]

    file: Required[FileTypes]

    metadata: str

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
