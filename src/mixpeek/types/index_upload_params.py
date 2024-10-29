# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["IndexUploadParams"]


class IndexUploadParams(TypedDict, total=False):
    asset: Required[FileTypes]

    collection_id: Required[str]

    image_settings: str

    metadata: str

    video_settings: str

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
