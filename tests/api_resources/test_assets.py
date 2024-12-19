# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types import (
    AssetResponse,
    AssetCreateResponse,
    AssetSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixpeek) -> None:
        asset = client.assets.create(
            collections=["col_123", "my_collection"],
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixpeek) -> None:
        asset = client.assets.create(
            collections=["col_123", "my_collection"],
            page=0,
            page_size=0,
            filters={
                "and": [
                    {
                        "key": "name",
                        "operator": "eq",
                        "value": "John",
                    },
                    {
                        "key": "age",
                        "operator": "eq",
                        "value": 30,
                    },
                ],
                "case_sensitive": True,
                "nor": [
                    {
                        "key": "department",
                        "operator": "eq",
                        "value": "HR",
                    },
                    {
                        "key": "location",
                        "operator": "eq",
                        "value": "remote",
                    },
                ],
                "or": [
                    {
                        "key": "status",
                        "operator": "eq",
                        "value": "active",
                    },
                    {
                        "key": "role",
                        "operator": "eq",
                        "value": "admin",
                    },
                ],
            },
            group_by={
                "field": "asset_id",
                "max_assets": 10,
                "sort": {
                    "direction": "asc",
                    "field": "score",
                },
            },
            return_url=True,
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "score",
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixpeek) -> None:
        response = client.assets.with_raw_response.create(
            collections=["col_123", "my_collection"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixpeek) -> None:
        with client.assets.with_streaming_response.create(
            collections=["col_123", "my_collection"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mixpeek) -> None:
        asset = client.assets.retrieve(
            asset_id="ast_123",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mixpeek) -> None:
        asset = client.assets.retrieve(
            asset_id="ast_123",
            return_url=True,
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixpeek) -> None:
        response = client.assets.with_raw_response.retrieve(
            asset_id="ast_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixpeek) -> None:
        with client.assets.with_streaming_response.retrieve(
            asset_id="ast_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.retrieve(
                asset_id="",
            )

    @parametrize
    def test_method_update(self, client: Mixpeek) -> None:
        asset = client.assets.update(
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixpeek) -> None:
        asset = client.assets.update(
            asset_id="asset_id",
            metadata={
                "description": "A new description",
                "title": "New Title",
            },
            propagate_features=True,
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixpeek) -> None:
        response = client.assets.with_raw_response.update(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixpeek) -> None:
        with client.assets.with_streaming_response.update(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.update(
                asset_id="",
            )

    @parametrize
    def test_method_delete(self, client: Mixpeek) -> None:
        asset = client.assets.delete(
            asset_id="asset_id",
        )
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Mixpeek) -> None:
        asset = client.assets.delete(
            asset_id="asset_id",
            x_namespace="X-Namespace",
        )
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixpeek) -> None:
        response = client.assets.with_raw_response.delete(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixpeek) -> None:
        with client.assets.with_streaming_response.delete(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(object, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.delete(
                asset_id="",
            )

    @parametrize
    def test_method_search(self, client: Mixpeek) -> None:
        asset = client.assets.search(
            collections=["col_123", "my_collection"],
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Mixpeek) -> None:
        asset = client.assets.search(
            collections=["col_123", "my_collection"],
            filters={
                "and": [
                    {
                        "key": "name",
                        "operator": "eq",
                        "value": "John",
                    },
                    {
                        "key": "age",
                        "operator": "eq",
                        "value": 30,
                    },
                ],
                "case_sensitive": True,
                "nor": [
                    {
                        "key": "department",
                        "operator": "eq",
                        "value": "HR",
                    },
                    {
                        "key": "location",
                        "operator": "eq",
                        "value": "remote",
                    },
                ],
                "or": [
                    {
                        "key": "status",
                        "operator": "eq",
                        "value": "active",
                    },
                    {
                        "key": "role",
                        "operator": "eq",
                        "value": "admin",
                    },
                ],
            },
            query={
                "key": ["title", "description"],
                "value": "search term",
            },
            return_url=True,
            select=["string"],
            sort={
                "direction": "asc",
                "field": "score",
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Mixpeek) -> None:
        response = client.assets.with_raw_response.search(
            collections=["col_123", "my_collection"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Mixpeek) -> None:
        with client.assets.with_streaming_response.search(
            collections=["col_123", "my_collection"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetSearchResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.create(
            collections=["col_123", "my_collection"],
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.create(
            collections=["col_123", "my_collection"],
            page=0,
            page_size=0,
            filters={
                "and": [
                    {
                        "key": "name",
                        "operator": "eq",
                        "value": "John",
                    },
                    {
                        "key": "age",
                        "operator": "eq",
                        "value": 30,
                    },
                ],
                "case_sensitive": True,
                "nor": [
                    {
                        "key": "department",
                        "operator": "eq",
                        "value": "HR",
                    },
                    {
                        "key": "location",
                        "operator": "eq",
                        "value": "remote",
                    },
                ],
                "or": [
                    {
                        "key": "status",
                        "operator": "eq",
                        "value": "active",
                    },
                    {
                        "key": "role",
                        "operator": "eq",
                        "value": "admin",
                    },
                ],
            },
            group_by={
                "field": "asset_id",
                "max_assets": 10,
                "sort": {
                    "direction": "asc",
                    "field": "score",
                },
            },
            return_url=True,
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "score",
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.with_raw_response.create(
            collections=["col_123", "my_collection"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.with_streaming_response.create(
            collections=["col_123", "my_collection"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.retrieve(
            asset_id="ast_123",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.retrieve(
            asset_id="ast_123",
            return_url=True,
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.with_raw_response.retrieve(
            asset_id="ast_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.with_streaming_response.retrieve(
            asset_id="ast_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.retrieve(
                asset_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.update(
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.update(
            asset_id="asset_id",
            metadata={
                "description": "A new description",
                "title": "New Title",
            },
            propagate_features=True,
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.with_raw_response.update(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.with_streaming_response.update(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.update(
                asset_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.delete(
            asset_id="asset_id",
        )
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.delete(
            asset_id="asset_id",
            x_namespace="X-Namespace",
        )
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.with_raw_response.delete(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(object, asset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.with_streaming_response.delete(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(object, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.delete(
                asset_id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.search(
            collections=["col_123", "my_collection"],
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixpeek) -> None:
        asset = await async_client.assets.search(
            collections=["col_123", "my_collection"],
            filters={
                "and": [
                    {
                        "key": "name",
                        "operator": "eq",
                        "value": "John",
                    },
                    {
                        "key": "age",
                        "operator": "eq",
                        "value": 30,
                    },
                ],
                "case_sensitive": True,
                "nor": [
                    {
                        "key": "department",
                        "operator": "eq",
                        "value": "HR",
                    },
                    {
                        "key": "location",
                        "operator": "eq",
                        "value": "remote",
                    },
                ],
                "or": [
                    {
                        "key": "status",
                        "operator": "eq",
                        "value": "active",
                    },
                    {
                        "key": "role",
                        "operator": "eq",
                        "value": "admin",
                    },
                ],
            },
            query={
                "key": ["title", "description"],
                "value": "search term",
            },
            return_url=True,
            select=["string"],
            sort={
                "direction": "asc",
                "field": "score",
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.assets.with_raw_response.search(
            collections=["col_123", "my_collection"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixpeek) -> None:
        async with async_client.assets.with_streaming_response.search(
            collections=["col_123", "my_collection"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetSearchResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
