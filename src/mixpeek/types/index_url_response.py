# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["IndexURLResponse", "AssetResponse", "DBModelTaskResponse"]


class AssetResponse(BaseModel):
    asset_id: str
    """The unique identifier for the asset"""

    collection_id: str
    """The ID of the collection the asset belongs to"""

    status: str
    """The current status of the asset processing"""

    created_at: Optional[datetime] = None
    """MongoDB datetime format"""

    error: Optional[str] = None
    """The error message if the asset processing failed"""

    metadata: Optional[object] = None
    """Additional metadata associated with the asset"""

    modality: Optional[str] = None
    """The type of media"""

    task_id: Optional[str] = None
    """The task ID"""

    unique_hash: Optional[str] = None
    """The unique hash of the asset"""

    updated_at: Optional[datetime] = None
    """MongoDB datetime format"""

    url: Optional[str] = None
    """The URL where the asset can be accessed"""


class DBModelTaskResponse(BaseModel):
    message: str
    """A message describing the status of the task"""

    task_id: str
    """The unique identifier for the processing task"""


IndexURLResponse: TypeAlias = Union[AssetResponse, DBModelTaskResponse]
