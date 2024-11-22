# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["GroupedAssetData", "Features", "FeaturesAudio", "FeaturesImage", "FeaturesText", "FeaturesVideo"]


class FeaturesAudio(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FeaturesImage(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FeaturesText(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class FeaturesVideo(BaseModel):
    preview_url: Optional[str] = None
    """The presigned URL for accessing the asset preview"""

    url: Optional[str] = None
    """The presigned URL for accessing the asset"""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Features(BaseModel):
    audio: Optional[List[FeaturesAudio]] = None

    image: Optional[List[FeaturesImage]] = None

    text: Optional[List[FeaturesText]] = None

    video: Optional[List[FeaturesVideo]] = None


class GroupedAssetData(BaseModel):
    asset: AssetResponse

    features: Features
