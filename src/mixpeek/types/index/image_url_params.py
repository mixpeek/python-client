# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ImageURLParams",
    "AssetUpdate",
    "ImageSettings",
    "ImageSettingsDescribe",
    "ImageSettingsDetect",
    "ImageSettingsDetectFaces",
    "ImageSettingsDetectLogos",
    "ImageSettingsEmbed",
    "ImageSettingsJsonOutput",
    "ImageSettingsRead",
]


class ImageURLParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    url: Required[str]
    """The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    image_settings: Optional[ImageSettings]
    """Settings for image processing.

    Only applicable if the URL points to an image file.
    """

    metadata: object
    """Additional metadata associated with the asset.

    Can include any key-value pairs relevant to the asset.
    """

    prevent_duplicate: Optional[bool]
    """Indicates whether to prevent duplicate processing of the same URL."""

    should_save: Optional[bool]
    """Indicates whether the processed asset should be uploaded to S3 storage."""

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class AssetUpdate(TypedDict, total=False):
    asset_id: Required[str]
    """Unique identifier for the asset to be updated"""

    mode: Required[Literal["replace", "append"]]
    """Update mode: 'replace' or 'append'"""


class ImageSettingsDescribe(TypedDict, total=False):
    json_output: object
    """JSON format for the response"""

    max_length: Optional[int]
    """Maximum length of the description"""

    model_id: Optional[Literal["image-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for image description"""


class ImageSettingsDetectFaces(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected objects"""

    model_id: Optional[Literal["face-detector-v1"]]
    """Model ID for face detection"""


class ImageSettingsDetectLogos(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected logos"""

    model_id: Optional[Literal["logo-detector-v1"]]
    """Model ID for logo detection"""


class ImageSettingsDetect(TypedDict, total=False):
    faces: Optional[ImageSettingsDetectFaces]
    """Settings for face detection"""

    logos: Optional[ImageSettingsDetectLogos]
    """Settings for logo detection"""


class ImageSettingsEmbed(TypedDict, total=False):
    model_id: Optional[Literal["multimodal-v1"]]


class ImageSettingsJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class ImageSettingsRead(TypedDict, total=False):
    json_output: object
    """JSON format for the response"""

    model_id: Optional[Literal["image-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for reading on-screen text"""


class ImageSettings(TypedDict, total=False):
    describe: Optional[ImageSettingsDescribe]
    """Settings for generating image descriptions."""

    detect: Optional[ImageSettingsDetect]
    """Settings for object detection in images."""

    embed: Optional[ImageSettingsEmbed]
    """Settings for generating image embeddings."""

    json_output: Optional[ImageSettingsJsonOutput]
    """Settings for structured JSON output of image analysis."""

    read: Optional[ImageSettingsRead]
    """Settings for reading and analyzing image content."""
