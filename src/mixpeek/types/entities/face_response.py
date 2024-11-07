# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FaceResponse"]


class FaceResponse(BaseModel):
    collection_id: str

    face_id: str

    metadata: Optional[object] = None

    url: str
