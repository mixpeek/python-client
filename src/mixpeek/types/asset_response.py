# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AssetResponse"]


class AssetResponse(BaseModel):
    asset_id: Optional[str] = None
    """The unique identifier for the asset"""

    collection_id: Optional[str] = None
    """The ID of the collection the asset belongs to"""

    created_at: Optional[datetime] = None
    """MongoDB datetime format"""

    duplicate_of: Optional[str] = None
    """The asset_id of the asset that this asset is a duplicate of"""

    error: Optional[object] = None
    """The error message if the asset processing failed"""

    file_data: Optional[object] = None
    """File data associated with the asset"""

    file_hash: Optional[str] = None
    """The unique hash of the"""

    metadata: Optional[object] = None
    """Additional metadata associated with the asset"""

    modality: Optional[str] = None
    """The type of media"""

    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    score: Optional[float] = None
    """The relevance score of the asset"""

    status: Optional[str] = None
    """The current status of the asset processing"""

    task_id: Optional[str] = None
    """The task ID"""

    updated_at: Optional[datetime] = None
    """MongoDB datetime format"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""
