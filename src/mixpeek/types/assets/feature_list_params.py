# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeatureListParams"]


class FeatureListParams(TypedDict, total=False):
    return_url: bool
    """Whether to generate and return presigned S3 URLs for the asset and preview.

    Set to false to improve performance when URLs aren't needed
    """

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    This can be a namespace name or namespace ID. Example: 'netflix_prod' or
    'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
    """
