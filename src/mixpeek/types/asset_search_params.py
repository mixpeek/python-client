# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.logical_operator import LogicalOperator

__all__ = ["AssetSearchParams", "Query"]


class AssetSearchParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    filters: Optional[LogicalOperator]
    """Complex nested query filters"""

    query: Optional[Query]
    """
    Structured query object specifying which fields to search in and what to search
    for
    """

    select: Optional[List[str]]
    """List of fields to return in results"""

    sort: Optional[SortOption]
    """List of fields to sort by"""

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class Query(TypedDict, total=False):
    key: Required[List[str]]
    """Fields to search in. Can be a list of field names or '\\**' for all fields"""

    value: Required[str]
    """The search term to look for in the specified fields"""
