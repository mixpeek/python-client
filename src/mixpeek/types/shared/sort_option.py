# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SortOption"]


class SortOption(BaseModel):
    direction: Literal["asc", "desc"]
    """Sort direction"""

    field: str
    """Field to sort by, supports dot notation for nested fields"""
