# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Taskresponse"]


class Taskresponse(BaseModel):
    file_id: str

    status: Literal["DONE", "FAILED", "PROCESSING", "DOWNLOADING", "INITIALIZING"]

    task_id: str
