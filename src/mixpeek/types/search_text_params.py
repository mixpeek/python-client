# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchTextParams", "Filters"]


class SearchTextParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    query: Required[str]

    filters: Optional[Filters]
    """Complex nested query filters"""

    group_by_file: bool
    """Whether to group search results by file"""

    input_type: Optional[Literal["text", "url", "base64"]]

    model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]]
    """Embedding model to use"""

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class Filters(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[object]], PropertyInfo(alias="AND")]
    """List of conditions that must all be true"""

    nor: Annotated[Optional[Iterable[object]], PropertyInfo(alias="NOR")]
    """List of conditions that must all be false"""

    or_: Annotated[Optional[Iterable[object]], PropertyInfo(alias="OR")]
    """List of conditions where at least one must be true"""
