# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrivateUpdateParams", "APIKey"]


class PrivateUpdateParams(TypedDict, total=False):
    api_keys: Optional[Iterable[APIKey]]

    metadata: Optional[object]


class APIKey(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    key: str

    name: str
