# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionSearchParams"]


class CollectionSearchParams(TypedDict, total=False):
    collection_id: Required[str]

    query: Required[str]

    page: int

    page_size: int

    sort_by: Optional[str]

    sort_order: Optional[Literal["asc", "desc"]]

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
