# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LogicalOperator"]


class LogicalOperator(TypedDict, total=False):
    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""
