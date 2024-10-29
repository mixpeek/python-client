# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    page: Optional[int]

    page_size: int

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
