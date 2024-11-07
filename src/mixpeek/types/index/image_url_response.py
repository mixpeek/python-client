# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..asset_response import AssetResponse

__all__ = ["ImageURLResponse", "DBModelTaskResponse"]


class DBModelTaskResponse(BaseModel):
    message: str
    """A message describing the status of the task"""

    task_id: str
    """The unique identifier for the processing task"""


ImageURLResponse: TypeAlias = Union[AssetResponse, DBModelTaskResponse]
