# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VideoURLParams",
    "AssetUpdate",
    "FeatureExtractor",
    "FeatureExtractorDescribe",
    "FeatureExtractorDetect",
    "FeatureExtractorDetectFaces",
    "FeatureExtractorDetectLogos",
    "FeatureExtractorEmbed",
    "FeatureExtractorJsonOutput",
    "FeatureExtractorRead",
    "FeatureExtractorTranscribe",
]


class VideoURLParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    url: Required[str]
    """The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    feature_extractors: Optional[Iterable[FeatureExtractor]]
    """Settings for video processing.

    Only applicable if the URL points to a video file.
    """

    metadata: object
    """Additional metadata associated with the asset.

    Can include any key-value pairs relevant to the asset.
    """

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    Example: 'netflix_prod' or 'spotify_recs_dev'. To create a namespace, use the
    /namespaces endpoint.
    """


class AssetUpdate(TypedDict, total=False):
    asset_id: Required[str]
    """Unique identifier for the asset to be updated"""

    mode: Required[Literal["replace", "append"]]
    """Update mode: 'replace' or 'append'"""


class FeatureExtractorDescribe(TypedDict, total=False):
    enabled: bool
    """Enable video description"""

    json_output: object
    """JSON format for the response"""

    max_length: Optional[int]
    """Maximum length of the description"""

    prompt: Optional[str]
    """Prompt for video description"""

    vector_index: Optional[Literal["image_vector", "multimodal_vector", "text_vector", "keyword_vector"]]
    """Name of the vector model to use for embedding the text output.

    If vector_index is duplicated, the vector will be overwritten.
    """


class FeatureExtractorDetectFaces(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected objects"""

    enabled: bool
    """Enable face detection"""


class FeatureExtractorDetectLogos(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected logos"""

    enabled: bool
    """Enable logo detection"""


class FeatureExtractorDetect(TypedDict, total=False):
    faces: Optional[FeatureExtractorDetectFaces]
    """Settings for face detection"""

    logos: Optional[FeatureExtractorDetectLogos]
    """Settings for logo detection"""


class FeatureExtractorEmbed(TypedDict, total=False):
    type: Required[Literal["url", "text", "file", "base64"]]
    """Type of input to embed"""

    vector_index: Required[Literal["image_vector", "multimodal_vector", "text_vector", "keyword_vector"]]
    """Name of the vector index to use for embedding"""

    field_name: Optional[str]
    """
    Field name to insert into the database, if not provided, the embedding will be
    inserted into the default field
    """

    value: Optional[str]
    """The input content to embed.

    Could be a URL, text content, file path, or base64 encoded string
    """


class FeatureExtractorJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class FeatureExtractorRead(TypedDict, total=False):
    enabled: bool
    """Enable video reading"""

    json_output: object
    """JSON format for the response"""

    prompt: Optional[str]
    """Prompt for reading on-screen text"""

    vector_index: Optional[Literal["image_vector", "multimodal_vector", "text_vector", "keyword_vector"]]
    """Name of the vector model to use for embedding the text output.

    If vector_index is duplicated, the vector will be overwritten.
    """


class FeatureExtractorTranscribe(TypedDict, total=False):
    enabled: bool
    """Enable video transcription"""

    json_output: object
    """JSON format for the response"""

    prompt: Optional[str]

    vector_index: Optional[Literal["image_vector", "multimodal_vector", "text_vector", "keyword_vector"]]
    """Name of the vector model to use for embedding the text output.

    If vector_index is duplicated, the vector will be overwritten.
    """


class FeatureExtractor(TypedDict, total=False):
    describe: Optional[FeatureExtractorDescribe]
    """Settings for generating video descriptions."""

    detect: Optional[FeatureExtractorDetect]
    """Settings for object detection in video frames."""

    embed: Iterable[FeatureExtractorEmbed]
    """List of embedding settings for generating multiple embeddings.

    For now, if url is provided, value must be None.
    """

    interval_sec: int
    """Interval in seconds for processing video.

    Must be greater than or equal to 5, less than 120.
    """

    json_output: Optional[FeatureExtractorJsonOutput]
    """Settings for structured JSON output of video analysis."""

    read: Optional[FeatureExtractorRead]
    """Settings for reading and analyzing video content."""

    transcribe: Optional[FeatureExtractorTranscribe]
    """Settings for transcribing video audio."""
