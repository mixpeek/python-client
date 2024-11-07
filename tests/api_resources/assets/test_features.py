# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types import GroupedAssetData

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Mixpeek) -> None:
        feature = client.assets.features.list(
            asset_id="asset_id",
        )
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixpeek) -> None:
        feature = client.assets.features.list(
            asset_id="asset_id",
            index_id="index-id",
        )
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixpeek) -> None:
        response = client.assets.features.with_raw_response.list(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixpeek) -> None:
        with client.assets.features.with_streaming_response.list(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(GroupedAssetData, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.features.with_raw_response.list(
                asset_id="",
            )


class TestAsyncFeatures:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.assets.features.list(
            asset_id="asset_id",
        )
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.assets.features.list(
            asset_id="asset_id",
            index_id="index-id",
        )
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.features.with_raw_response.list(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(GroupedAssetData, feature, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.features.with_streaming_response.list(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(GroupedAssetData, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.features.with_raw_response.list(
                asset_id="",
            )
