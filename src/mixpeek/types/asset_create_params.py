# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.filter_condition import FilterCondition

__all__ = ["AssetCreateParams", "Filters", "FiltersAnd", "FiltersNor", "FiltersOr", "GroupBy"]


class AssetCreateParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    page: Optional[int]

    page_size: int

    filters: Optional[Filters]
    """Used for filtering across all indexes"""

    group_by: Optional[GroupBy]
    """Grouping options for search results"""

    return_url: Optional[bool]
    """
    Return the presigned URL for the asset and preview asset, this will introduce
    additional latency
    """

    select: Optional[List[str]]
    """List of fields to return in results, supports dot notation.

    If None, all fields are returned.
    """

    sort: Optional[SortOption]
    """List of fields to sort by, with direction (asc or desc).

    Supports dot notation for nested fields.
    """

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


class GroupBy(TypedDict, total=False):
    field: Optional[str]
    """Field to group by

            Note: We currently do not support ad-hoc grouping.
            This means the field must be indexed separately.
            Please contact us to add additional fields for grouping.
    """

    max_assets: Optional[int]
    """Maximum number of assets to group"""

    sort: Optional[SortOption]
    """Sort options for ordering the inside of the groups"""
