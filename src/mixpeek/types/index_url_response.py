# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .collections.fileresponse import Fileresponse

__all__ = ["IndexURLResponse", "DBModelTaskResponse"]


class DBModelTaskResponse(BaseModel):
    message: str
    """A message describing the status of the task"""

    task_id: str
    """The unique identifier for the processing task"""


IndexURLResponse: TypeAlias = Union[Fileresponse, DBModelTaskResponse]
