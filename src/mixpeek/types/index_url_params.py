# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IndexURLParams",
    "ImageSettings",
    "ImageSettingsDescribe",
    "ImageSettingsDetect",
    "ImageSettingsDetectFaces",
    "ImageSettingsEmbed",
    "ImageSettingsJsonOutput",
    "ImageSettingsRead",
    "VideoSetting",
    "VideoSettingDescribe",
    "VideoSettingDetect",
    "VideoSettingDetectFaces",
    "VideoSettingEmbed",
    "VideoSettingJsonOutput",
    "VideoSettingRead",
    "VideoSettingTranscribe",
]


class IndexURLParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed file will be stored."""

    url: Required[str]
    """The URL of the file to be processed. Must be a valid HTTP or HTTPS URL."""

    image_settings: Optional[ImageSettings]
    """Settings for image processing.

    Only applicable if the URL points to an image file.
    """

    metadata: object
    """Additional metadata associated with the file.

    Can include any key-value pairs relevant to the file.
    """

    prevent_duplicate: Optional[bool]
    """Indicates whether to prevent duplicate processing of the same URL."""

    should_save: Optional[bool]
    """Indicates whether the processed file should be uploaded to S3 storage."""

    video_settings: Optional[Iterable[VideoSetting]]
    """Settings for video processing.

    Only applicable if the URL points to a video file.
    """

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


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


class ImageSettingsDetect(TypedDict, total=False):
    faces: Optional[ImageSettingsDetectFaces]
    """Settings for face detection"""


class ImageSettingsEmbed(TypedDict, total=False):
    model_id: Optional[Literal["image-embed-v1", "multimodal-v1"]]


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


class VideoSettingDetect(TypedDict, total=False):
    faces: Optional[VideoSettingDetectFaces]
    """Settings for face detection"""


class VideoSettingEmbed(TypedDict, total=False):
    contextual_text: Optional[str]

    model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1"]]


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
