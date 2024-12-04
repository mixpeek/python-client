# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IndexTextParams",
    "AssetUpdate",
    "FeatureExtractors",
    "FeatureExtractorsEmbed",
    "FeatureExtractorsJsonOutput",
    "Percolate",
]


class IndexTextParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    feature_extractors: Optional[FeatureExtractors]
    """Settings for text processing."""

    metadata: object
    """Additional metadata associated with the file.

    Can include any key-value pairs relevant to the file.
    """

    percolate: Optional[Percolate]
    """Settings for percolating the asset against stored queries."""

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


class FeatureExtractors(TypedDict, total=False):
    embed: Iterable[FeatureExtractorsEmbed]
    """List of embedding settings for generating multiple embeddings.

    field_name's provided are how the raw text will be inserted, if not provided,
    the field_name will be auto-generated.
    """

    json_output: Optional[FeatureExtractorsJsonOutput]
    """Settings for structured JSON output of text analysis."""


class Percolate(TypedDict, total=False):
    enabled: bool
    """Whether to enable percolator matching for this request"""

    max_candidates: Optional[int]
    """Maximum number of matching percolators to return in the response"""

    min_score: Optional[float]
    """Minimum similarity score (0-1) required for a match.

    Higher values mean stricter matching.
    """
