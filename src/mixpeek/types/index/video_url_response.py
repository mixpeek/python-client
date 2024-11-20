# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["VideoURLResponse"]


class VideoURLResponse(BaseModel):
    message: str
    """A message describing the status of the task"""

    task_id: str
    """The unique identifier for the processing task"""
