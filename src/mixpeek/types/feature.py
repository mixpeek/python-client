# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Feature"]


class Feature(BaseModel):
    asset_id: Optional[str] = None

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    detect: Optional[object] = None

    feature_id: Optional[str] = None

    json_output: Optional[object] = None

    metadata: Optional[object] = None

    modality: Optional[str] = None

    text: Optional[str] = None

    transcription: Optional[str] = None

    vectors: Optional[object] = None
