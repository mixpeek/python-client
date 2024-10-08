# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Embeddingresponse"]


class Embeddingresponse(BaseModel):
    embedding: List[float]
    """The embedding of the processed data."""

    elapsed_time: Optional[float] = None
    """The time taken to process the data."""
