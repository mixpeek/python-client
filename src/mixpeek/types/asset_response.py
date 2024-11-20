# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AssetResponse", "Metadata"]


class Metadata(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class AssetResponse(BaseModel):
    asset_id: Optional[str] = None
    """The unique identifier for the asset"""

    collection_id: Optional[str] = None
    """The ID of the collection the asset belongs to"""

    created_at: Optional[datetime] = None
    """MongoDB datetime format"""

    error: Optional[str] = None
    """The error message if the asset processing failed"""

    metadata: Optional[Metadata] = None
    """Additional metadata associated with the asset"""

    modality: Optional[str] = None
    """The type of media"""

    score: Optional[float] = None
    """The relevance score of the asset"""

    status: Optional[str] = None
    """The current status of the asset processing"""

    task_id: Optional[str] = None
    """The task ID"""

    unique_hash: Optional[str] = None
    """The unique hash of the asset"""

    updated_at: Optional[datetime] = None
    """MongoDB datetime format"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""
