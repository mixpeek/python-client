# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from .._models import BaseModel

__all__ = ["FeatureRetrieveResponse"]


class FeatureRetrieveResponse(BaseModel):
    duplicate_of: Optional[str] = None
    """The asset_id of the asset that this asset is a duplicate of"""

    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
