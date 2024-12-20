# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskResponse"]


class TaskResponse(BaseModel):
    inputs: List[object]

    outputs: List[object]

    status: Literal[
        "DONE", "FAILED", "SKIPPED", "CANCELLED", "PROCESSING", "DOWNLOADING", "INITIALIZING", "UPLOADING", "QUEUED"
    ]

    task_id: str
