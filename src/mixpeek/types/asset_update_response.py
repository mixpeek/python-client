# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .asset_response import AssetResponse
from .grouped_asset_data import GroupedAssetData

__all__ = ["AssetUpdateResponse"]

AssetUpdateResponse: TypeAlias = Union[AssetResponse, GroupedAssetData]
