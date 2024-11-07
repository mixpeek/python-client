# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .feature import Feature
from .._models import BaseModel

__all__ = ["FeatureListResponse", "Pagination"]


class Pagination(BaseModel):
    current_page: int

    next_page: Optional[str] = None

    page_size: int

    previous_page: Optional[str] = None

    total: int

    total_pages: int


class FeatureListResponse(BaseModel):
    pagination: Pagination

    results: List[Feature]
