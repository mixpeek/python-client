# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ImageURLParams",
    "AssetUpdate",
    "FeatureExtractors",
    "FeatureExtractorsDescribe",
    "FeatureExtractorsDetect",
    "FeatureExtractorsDetectFaces",
    "FeatureExtractorsDetectLogos",
    "FeatureExtractorsEmbed",
    "FeatureExtractorsJsonOutput",
    "FeatureExtractorsRead",
    "Percolate",
]


class ImageURLParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    url: Required[str]
    """The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    feature_extractors: Optional[FeatureExtractors]
    """Settings for image processing.

    Only applicable if the URL points to an image file.
    """

    metadata: object
    """Additional metadata associated with the asset.

    Can include any key-value pairs relevant to the asset.
    """

    percolate: Optional[Percolate]
    """Settings for percolating the asset against stored queries."""

    skip_duplicate: Optional[bool]
    """
    Skips processing when a duplicate hash is found and stores an error by the
    task_id with the existing asset_id
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


class FeatureExtractorsDescribe(TypedDict, total=False):
    enabled: bool
    """Enable image description"""

    json_output: object
    """JSON format for the response"""

    max_length: Optional[int]
    """Maximum length of the description"""

    prompt: Optional[str]
    """Prompt for image description"""

    vector_index: Optional[Literal["image", "multimodal", "text", "keyword"]]
    """Name of the vector model to use for embedding the text output.

    If vector_index is duplicated, the vector will be overwritten.
    """


class FeatureExtractorsDetectFaces(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected objects"""

    enabled: bool
    """Enable face detection"""


class FeatureExtractorsDetectLogos(TypedDict, total=False):
    confidence_threshold: Optional[float]
    """Minimum confidence threshold for detected logos"""

    enabled: bool
    """Enable logo detection"""


class FeatureExtractorsDetect(TypedDict, total=False):
    faces: Optional[FeatureExtractorsDetectFaces]
    """Settings for face detection"""

    logos: Optional[FeatureExtractorsDetectLogos]
    """Settings for logo detection"""


class FeatureExtractorsEmbed(TypedDict, total=False):
    type: Required[Literal["url", "text", "file", "base64"]]
    """Type of input to embed"""

    vector_index: Required[Literal["image", "multimodal", "text", "keyword"]]
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


class FeatureExtractorsJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class FeatureExtractorsRead(TypedDict, total=False):
    enabled: bool
    """Enable image reading"""

    json_output: object
    """JSON format for the response"""

    prompt: Optional[str]
    """Prompt for reading on-screen text"""

    vector_index: Optional[Literal["image", "multimodal", "text", "keyword"]]
    """Name of the vector model to use for embedding the text output.

    If vector_index is duplicated, the vector will be overwritten.
    """


class FeatureExtractors(TypedDict, total=False):
    describe: Optional[FeatureExtractorsDescribe]
    """Settings for generating image descriptions."""

    detect: Optional[FeatureExtractorsDetect]
    """Settings for object detection in images."""

    embed: Iterable[FeatureExtractorsEmbed]
    """List of embedding settings for generating multiple embeddings.

    For now, if url is provided, value must be None.
    """

    json_output: Optional[FeatureExtractorsJsonOutput]
    """Settings for structured JSON output of image analysis."""

    read: Optional[FeatureExtractorsRead]
    """Settings for reading and analyzing image content."""


class Percolate(TypedDict, total=False):
    enabled: bool
    """Whether to enable percolator matching for this request"""

    max_candidates: Optional[int]
    """Maximum number of matching percolators to return in the response"""

    min_score: Optional[float]
    """Minimum similarity score (0-1) required for a match.

    Higher values mean stricter matching.
    """
