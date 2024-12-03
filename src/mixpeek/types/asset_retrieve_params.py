# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetRetrieveParams"]


class AssetRetrieveParams(TypedDict, total=False):
    return_url: bool
    """Whether to generate and return presigned S3 URLs for the asset and preview.

    Set to false to improve performance when URLs aren't needed
    """

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    Example: 'netflix_prod' or 'spotify_recs_dev'. To create a namespace, use the
    /namespaces endpoint.
    """