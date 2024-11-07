# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ModelPaginationResponse"]


class ModelPaginationResponse(BaseModel):
    next_page: Optional[str] = None

    page: int

    page_size: int

    previous_page: Optional[str] = None

    total: int

    total_pages: int
