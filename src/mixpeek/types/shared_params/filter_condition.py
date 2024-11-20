# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FilterCondition"]


class FilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    operator: Literal["eq", "ne", "gt", "lt", "gte", "lte", "in", "nin", "is_null", "text", "exists"]
    """Comparison operator"""

    value: Optional[object]
    """Value to compare against"""
