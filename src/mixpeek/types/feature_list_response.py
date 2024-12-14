# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional

from .._models import BaseModel

__all__ = ["FeatureListResponse", "Pagination", "Result"]


class Pagination(BaseModel):
    current_page: int

    next_page: Optional[str] = None

    page_size: int

    previous_page: Optional[str] = None

    total: int

    total_pages: int


class Result(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FeatureListResponse(BaseModel):
    pagination: Pagination

    results: List[Result]
