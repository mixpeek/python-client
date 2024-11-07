# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LabelResponse", "Label"]


class Label(BaseModel):
    created_at: datetime

    description: str

    index_id: str

    label: str

    label_id: str

    metadata: Optional[object] = None

    updated_at: datetime


class LabelResponse(BaseModel):
    label: Label

    message: str
