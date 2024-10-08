# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
    "VideoSettings",
    "VideoSettingsDescribe",
    "VideoSettingsDetect",
    "VideoSettingsDetectFaces",
    "VideoSettingsEmbed",
    "VideoSettingsJsonOutput",
    "VideoSettingsRead",
    "VideoSettingsTranscribe",
]


class IndexURLParams(TypedDict, total=False):
    collection_id: Required[str]

    url: Required[str]

    image_settings: Optional[ImageSettings]

    metadata: object
    """Additional metadata associated with the file"""

    should_save: Optional[bool]
    """Whether to upload the processed file to S3"""

    video_settings: Optional[VideoSettings]

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class ImageSettingsDescribe(TypedDict, total=False):
    model_id: Optional[Literal["image-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for image description"""


class ImageSettingsDetectFaces(TypedDict, total=False):
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
    json_format: object
    """JSON format for the response"""

    model_id: Optional[Literal["image-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for reading on-screen text"""


class ImageSettings(TypedDict, total=False):
    describe: Optional[ImageSettingsDescribe]

    detect: Optional[ImageSettingsDetect]

    embed: Optional[ImageSettingsEmbed]

    json_output: Optional[ImageSettingsJsonOutput]

    read: Optional[ImageSettingsRead]


class VideoSettingsDescribe(TypedDict, total=False):
    model_id: Optional[Literal["video-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for video description"""


class VideoSettingsDetectFaces(TypedDict, total=False):
    model_id: Optional[Literal["face-detector-v1"]]
    """Model ID for face detection"""


class VideoSettingsDetect(TypedDict, total=False):
    faces: Optional[VideoSettingsDetectFaces]
    """Settings for face detection"""


class VideoSettingsEmbed(TypedDict, total=False):
    contextual_text: Optional[str]

    model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1"]]


class VideoSettingsJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class VideoSettingsRead(TypedDict, total=False):
    json_format: object
    """JSON format for the response"""

    model_id: Optional[Literal["video-descriptor-v1"]]

    prompt: Optional[str]
    """Prompt for reading on-screen text"""


class VideoSettingsTranscribe(TypedDict, total=False):
    model_id: Optional[Literal["polyglot-v1"]]

    prompt: Optional[str]


class VideoSettings(TypedDict, total=False):
    describe: Optional[VideoSettingsDescribe]

    detect: Optional[VideoSettingsDetect]

    embed: Optional[VideoSettingsEmbed]

    interval_sec: int
    """Interval in seconds for processing video"""

    json_output: Optional[VideoSettingsJsonOutput]

    read: Optional[VideoSettingsRead]

    transcribe: Optional[VideoSettingsTranscribe]
