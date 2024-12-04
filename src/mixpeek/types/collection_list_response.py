# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.model_pagination_response import ModelPaginationResponse

__all__ = ["CollectionListResponse", "Result"]


class Result(BaseModel):
    collection_id: str

    count: int

    last_updated: datetime
    """MongoDB datetime format"""

    size_bytes: int

    metadata: Optional[object] = None

    preview_url: Optional[str] = None


class CollectionListResponse(BaseModel):
    pagination: ModelPaginationResponse

    results: List[Result]
