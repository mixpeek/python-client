# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskResponse"]


class TaskResponse(BaseModel):
    asset_id: str

    status: Literal[
        "DONE", "FAILED", "PROCESSING", "DOWNLOADING", "INITIALIZING", "UPLOADING", "QUEUED", "SKIPPED", "CANCELLED"
    ]

    task_id: str
