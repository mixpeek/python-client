# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LogicalOperator"]


class LogicalOperator(BaseModel):
    case_sensitive: Optional[bool] = None
    """Whether to perform case-sensitive matching"""
