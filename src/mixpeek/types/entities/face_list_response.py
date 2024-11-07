# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .face_response import FaceResponse
from ..shared.model_pagination_response import ModelPaginationResponse

__all__ = ["FaceListResponse"]


class FaceListResponse(BaseModel):
    pagination: ModelPaginationResponse

    results: List[FaceResponse]
