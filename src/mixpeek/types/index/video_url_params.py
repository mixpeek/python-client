# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VideoURLParams",
    "AssetUpdate",
    "VideoSetting",
    "VideoSettingDescribe",
    "VideoSettingDetect",
    "VideoSettingDetectFaces",
    "VideoSettingDetectLogos",
    "VideoSettingEmbed",
    "VideoSettingJsonOutput",
    "VideoSettingRead",
    "VideoSettingTranscribe",
]


class VideoURLParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    url: Required[str]
    """The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    metadata: object
    """Additional metadata associated with the asset.

    Can include any key-value pairs relevant to the asset.
    """

    prevent_duplicate: Optional[bool]
    """Indicates whether to prevent duplicate processing of the same URL."""

    should_save: Optional[bool]
    """Indicates whether the processed asset should be uploaded to S3 storage."""

    video_settings: Optional[Iterable[VideoSetting]]
    """Settings for video processing.

    Only applicable if the URL points to a video file.
    """

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class AssetUpdate(TypedDict, total=False):
    asset_id: Required[str]
    """Unique identifier for the asset to be updated"""

    mode: Required[Literal["replace", "append"]]
    """Update mode: 'replace' or 'append'"""


class VideoSettingDescribe(TypedDict, total=False):
    json_output: object
    """JSON format for the response"""

    max_length: Optional[int]
    """Maximum length of the description"""

    model_id: Optional[Literal["video-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for video description"""


class VideoSettingDetectFaces(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected objects"""

    model_id: Optional[Literal["face-detector-v1"]]
    """Model ID for face detection"""


class VideoSettingDetectLogos(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected logos"""

    model_id: Optional[Literal["logo-detector-v1"]]
    """Model ID for logo detection"""


class VideoSettingDetect(TypedDict, total=False):
    faces: Optional[VideoSettingDetectFaces]
    """Settings for face detection"""

    logos: Optional[VideoSettingDetectLogos]
    """Settings for logo detection"""


class VideoSettingEmbed(TypedDict, total=False):
    model_id: Optional[Literal["multimodal-v1"]]


class VideoSettingJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class VideoSettingRead(TypedDict, total=False):
    json_output: object
    """JSON format for the response"""

    model_id: Optional[Literal["video-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for reading on-screen text"""


class VideoSettingTranscribe(TypedDict, total=False):
    json_output: object
    """JSON format for the response"""

    model_id: Optional[Literal["polyglot-v1"]]

    prompt: Optional[str]


class VideoSetting(TypedDict, total=False):
    describe: Optional[VideoSettingDescribe]
    """Settings for generating video descriptions."""

    detect: Optional[VideoSettingDetect]
    """Settings for object detection in video frames."""

    embed: Optional[VideoSettingEmbed]
    """Settings for generating video embeddings."""

    interval_sec: int
    """Interval in seconds for processing video.

    Must be greater than or equal to 5, less than 120.
    """

    json_output: Optional[VideoSettingJsonOutput]
    """Settings for structured JSON output of video analysis."""

    read: Optional[VideoSettingRead]
    """Settings for reading and analyzing video content."""

    transcribe: Optional[VideoSettingTranscribe]
    """Settings for transcribing video audio."""
