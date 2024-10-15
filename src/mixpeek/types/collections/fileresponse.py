# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Fileresponse"]


class Fileresponse(BaseModel):
    collection_id: str
    """The ID of the collection the file belongs to"""

    created_at: Optional[datetime] = None
    """The timestamp when the file was created"""

    file_id: str
    """The unique identifier for the file"""

    status: str
    """The current status of the file processing"""

    error: Optional[str] = None
    """The error message if the file processing failed"""

    media_type: Optional[str] = None
    """The type of media"""

    metadata: Optional[object] = None
    """Additional metadata associated with the file"""

    task_id: Optional[str] = None
    """The task ID"""

    unique_hash: Optional[str] = None
    """The unique hash of the file"""

    updated_at: Optional[datetime] = None
    """The timestamp when the file was last updated"""

    url: Optional[str] = None
    """The URL where the file can be accessed"""
