# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["User", "APIKey"]


class APIKey(BaseModel):
    created_at: Optional[datetime] = None

    key: Optional[str] = None

    name: Optional[str] = None


class User(BaseModel):
    email: str

    account_type: Optional[str] = None

    api_keys: Optional[List[APIKey]] = None

    credit_count: Optional[int] = None

    index_ids: Optional[List[str]] = None

    metadata: Optional[object] = None

    user_id: Optional[str] = None
