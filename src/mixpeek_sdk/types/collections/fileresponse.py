# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Fileresponse"]


class Fileresponse(BaseModel):
    collection_id: str

    created_at: datetime

    file_id: str

    index_id: str

    metadata: object

    status: str

    url: str
