# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FilterCondition"]


class FilterCondition(BaseModel):
    key: str
    """Field name to filter on"""

    operator: Optional[Literal["eq", "ne", "gt", "lt", "gte", "lte", "in", "nin", "is_null", "text", "exists"]] = None
    """Comparison operator"""

    value: Optional[object] = None
    """Value to compare against"""
