# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["SearchFileParams"]


class SearchFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    offset_position: Optional[int]
    """The position to start returning results from.

    Used for pagination. Does not work with group_by
    """

    page_size: int
    """Number of results to return per page."""

    filters: str

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
