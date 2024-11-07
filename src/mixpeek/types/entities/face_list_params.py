# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FaceListParams"]


class FaceListParams(TypedDict, total=False):
    page: int

    page_size: int

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
