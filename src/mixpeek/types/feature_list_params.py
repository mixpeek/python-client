# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.logical_operator import LogicalOperator

__all__ = ["FeatureListParams"]


class FeatureListParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """Collection IDs to filter features"""

    offset_feature_id: Optional[str]
    """The offset id to start returning results from. Used for pagination"""

    page_size: int

    filters: Optional[LogicalOperator]
    """Complex nested query filters"""

    select: Optional[Iterable[object]]
    """List of fields to return in results, supports dot notation."""

    sort: Optional[SortOption]
    """
    List of fields to sort by, with direction (asc or desc). NOTE: fields will
    require a specialty index to use this, consult with the team.
    """

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
