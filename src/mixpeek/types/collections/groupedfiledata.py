# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Groupedfiledata", "ImageDetails"]


class ImageDetails(BaseModel):
    caption: Optional[str] = None

    description: Optional[str] = None

    detect: Optional[object] = None

    text: Optional[str] = None


class Groupedfiledata(BaseModel):
    collection_id: str

    created_at: datetime

    file_id: str

    index_id: str

    metadata: object

    status: str

    url: str

    image_details: Optional[ImageDetails] = None

    video_segments: Optional[List[Dict[str, object]]] = None
