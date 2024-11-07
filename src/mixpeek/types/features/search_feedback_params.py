# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SearchFeedbackParams"]


class SearchFeedbackParams(TypedDict, total=False):
    feature_id: Required[str]

    is_relevant: Required[bool]

    search_id: Required[str]

    feedback_text: Optional[str]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
