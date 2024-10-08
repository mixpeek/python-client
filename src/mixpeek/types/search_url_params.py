# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchURLParams", "Pagination"]


class SearchURLParams(TypedDict, total=False):
    input: Required[str]
    """url, text, or base64 input"""

    filters: object
    """Additional filters for the search"""

    group_by_file: bool
    """Whether to group search results by file"""

    input_type: Optional[str]

    modality: Optional[str]

    model_id: Optional[str]

    pagination: Pagination
    """Pagination parameters"""

    source: Optional[str]

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class Pagination(TypedDict, total=False):
    page: int
    """Page number"""

    page_size: int
    """Number of items per page"""
