# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeatureUpdateParams"]


class FeatureUpdateParams(TypedDict, total=False):
    metadata: Required[object]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
