# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.model_pagination_response import ModelPaginationResponse

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    pagination: ModelPaginationResponse

    results: List[object]
