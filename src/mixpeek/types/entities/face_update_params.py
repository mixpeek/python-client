# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FaceUpdateParams"]


class FaceUpdateParams(TypedDict, total=False):
    path_face_id: Required[Annotated[str, PropertyInfo(alias="face_id")]]

    collection_id: Required[str]

    body_face_id: Required[Annotated[str, PropertyInfo(alias="face_id")]]

    metadata: Required[object]

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    Example: 'netflix_prod' or 'spotify_recs_dev'. To create a namespace, use the
    /namespaces endpoint.
    """
