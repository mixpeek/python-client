# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LabelListResponse", "Result"]


class Result(BaseModel):
    created_at: datetime

    description: str

    index_id: str

    label: str

    label_id: str

    metadata: Optional[object] = None

    updated_at: datetime


class LabelListResponse(BaseModel):
    pagination: object

    results: List[Result]
