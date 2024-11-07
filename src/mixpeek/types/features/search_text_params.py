# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.sort_option import SortOption
from ..shared_params.logical_operator import LogicalOperator

__all__ = ["SearchTextParams", "GroupBy"]


class SearchTextParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    offset_position: Optional[int]
    """The position to start returning results from.

    Used for pagination. Does not work with group_by
    """

    page_size: int
    """Number of results to return per page."""

    filters: Optional[LogicalOperator]
    """Complex nested query filters"""

    group_by: Optional[GroupBy]
    """Grouping options for search results"""

    model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]]
    """Embedding model to use"""

    query: Optional[str]
    """Text query for the search"""

    search_type: Literal["semantic", "fulltext"]
    """Type of search to perform"""

    select: Optional[List[str]]
    """List of fields to return in results, supports dot notation.

    If None, all fields are returned.
    """

    sort: Optional[SortOption]
    """List of fields to sort by, with direction (asc or desc).

    Supports dot notation for nested fields.
    """

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class GroupBy(TypedDict, total=False):
    field: Optional[str]
    """Field to group by

            Note: We currently do not support ad-hoc grouping.
            This means the field must be indexed separately.
            Please contact us to add additional fields for grouping.
    """

    max_features: Optional[int]
    """Maximum number of features to group"""

    sort: Optional[SortOption]
    """Sort options for ordering the inside of the groups"""
