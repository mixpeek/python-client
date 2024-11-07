# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["GroupedAssetData", "Features"]


class Features(BaseModel):
    audio: Optional[List[Dict[str, object]]] = None

    image: Optional[List[Dict[str, object]]] = None

    text: Optional[List[Dict[str, object]]] = None

    video: Optional[List[Dict[str, object]]] = None


class GroupedAssetData(BaseModel):
    asset: AssetResponse

    features: Features
