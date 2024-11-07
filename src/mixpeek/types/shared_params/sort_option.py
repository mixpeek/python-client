# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SortOption"]


class SortOption(TypedDict, total=False):
    direction: Required[Literal["asc", "desc"]]
    """Sort direction"""

    field: Required[str]
    """Field to sort by, supports dot notation for nested fields"""
