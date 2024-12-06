# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.filter_condition import FilterCondition

__all__ = ["AssetSearchParams", "Filters", "FiltersAnd", "FiltersNor", "FiltersOr", "Query"]


class AssetSearchParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    filters: Optional[Filters]
    """Complex nested query filters"""

    query: Optional[Query]
    """
    Structured query object specifying which fields to search in and what to search
    for
    """

    return_url: Optional[bool]
    """
    Return the presigned URL for the asset and preview asset, this will introduce
    additional latency
    """

    select: Optional[List[str]]
    """List of fields to return in results"""

    sort: Optional[SortOption]
    """List of fields to sort by"""

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    Example: 'netflix_prod' or 'spotify_recs_dev'. To create a namespace, use the
    /namespaces endpoint.
    """


FiltersAnd: TypeAlias = Union[FilterCondition, object]

FiltersNor: TypeAlias = Union[FilterCondition, object]

FiltersOr: TypeAlias = Union[FilterCondition, object]


class Filters(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAnd]], PropertyInfo(alias="AND")]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNor]], PropertyInfo(alias="NOR")]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


class Query(TypedDict, total=False):
    key: Required[List[str]]
    """Fields to search in. Can be a list of field names or '\\**' for all fields"""

    value: Required[str]
    """The search term to look for in the specified fields"""
