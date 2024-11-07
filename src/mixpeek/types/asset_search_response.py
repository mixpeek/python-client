# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .asset_response import AssetResponse
from .shared.model_pagination_response import ModelPaginationResponse

__all__ = ["AssetSearchResponse"]


class AssetSearchResponse(BaseModel):
    pagination: ModelPaginationResponse

    results: List[AssetResponse]
