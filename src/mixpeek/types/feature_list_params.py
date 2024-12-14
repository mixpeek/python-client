# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.filter_condition import FilterCondition

__all__ = ["FeatureListParams", "Filters", "FiltersAnd", "FiltersNor", "FiltersOr"]


class FeatureListParams(TypedDict, total=False):
    collections: Required[List[str]]
    """Collection identifiers - can be either collection IDs or collection names"""

    offset_feature_id: Optional[str]
    """The offset id to start returning results from. Used for pagination"""

    page_size: int

    filters: Optional[Filters]
    """Complex nested query filters"""

    return_urls: bool
    """When true, generates presigned URLs for assets"""

    select: Optional[Iterable[object]]
    """List of fields to return in results, supports dot notation.

    Everything else is excluded.
    """

    sort: Optional[SortOption]
    """
    List of fields to sort by, with direction (asc or desc). NOTE: fields will
    require a specialty index to use this, consult with the team.
    """

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    This can be a namespace name or namespace ID. Example: 'netflix_prod' or
    'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
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
