# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    path_label_id: Required[Annotated[str, PropertyInfo(alias="label_id")]]

    body_label_id: Required[Annotated[str, PropertyInfo(alias="label_id")]]

    metadata: Required[Optional[object]]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
