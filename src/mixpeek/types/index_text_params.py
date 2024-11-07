# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "IndexTextParams",
    "AssetUpdate",
    "TextSettings",
    "TextSettingsEmbed",
    "TextSettingsFulltext",
    "TextSettingsJsonOutput",
]


class IndexTextParams(TypedDict, total=False):
    collection_id: Required[str]
    """Unique identifier for the collection where the processed asset will be stored."""

    text: Required[str]
    """The text to be processed."""

    asset_update: Optional[AssetUpdate]
    """Asset update information for existing assets"""

    metadata: object
    """Additional metadata associated with the file.

    Can include any key-value pairs relevant to the file.
    """

    text_settings: Optional[TextSettings]
    """Settings for text processing."""

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class AssetUpdate(TypedDict, total=False):
    asset_id: Required[str]
    """Unique identifier for the asset to be updated"""

    mode: Required[Literal["replace", "append"]]
    """Update mode: 'replace' or 'append'"""


class TextSettingsEmbed(TypedDict, total=False):
    model_id: Optional[Literal["multimodal-v1"]]


class TextSettingsFulltext(TypedDict, total=False):
    model_id: Literal["splade-v3"]
    """Model ID for fulltext indexing. Only 'splade-v3' is currently supported."""


class TextSettingsJsonOutput(TypedDict, total=False):
    prompt: Optional[str]

    response_shape: Optional[object]


class TextSettings(TypedDict, total=False):
    embed: Optional[TextSettingsEmbed]
    """Settings for generating text embeddings. Only multimodal-v1 is supported."""

    fulltext: Optional[TextSettingsFulltext]
    """Field names to be used for fulltext indexing.

    Only one field is supported initially.
    """

    json_output: Optional[TextSettingsJsonOutput]
    """Settings for structured JSON output of text analysis."""
