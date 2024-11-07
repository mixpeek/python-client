# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeatureRetrieveParams"]


class FeatureRetrieveParams(TypedDict, total=False):
    include_vectors: Optional[bool]
    """When true, includes the feature's vector embeddings in the response"""

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
