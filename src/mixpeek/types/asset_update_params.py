# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    metadata: object
    """Updated metadata for the asset.

    This can include any key-value pairs that should be updated or added to the
    asset's metadata.
    """

    propagate_features: Optional[bool]
    """If True, the features will be propagated to all assets with the same asset_id"""

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""
