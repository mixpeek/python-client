# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MixpeekSDK) -> None:
        collection = client.collections.list()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MixpeekSDK) -> None:
        collection = client.collections.list(
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MixpeekSDK) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MixpeekSDK) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: MixpeekSDK) -> None:
        collection = client.collections.delete(
            collection_id="collection_id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: MixpeekSDK) -> None:
        collection = client.collections.delete(
            collection_id="collection_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: MixpeekSDK) -> None:
        response = client.collections.with_raw_response.delete(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: MixpeekSDK) -> None:
        with client.collections.with_streaming_response.delete(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.collections.with_raw_response.delete(
                collection_id="",
            )

    @parametrize
    def test_method_search(self, client: MixpeekSDK) -> None:
        collection = client.collections.search(
            collection_id="collection_id",
            query="query",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: MixpeekSDK) -> None:
        collection = client.collections.search(
            collection_id="collection_id",
            query="query",
            page=1,
            page_size=1,
            sort_by="sort_by",
            sort_order="asc",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: MixpeekSDK) -> None:
        response = client.collections.with_raw_response.search(
            collection_id="collection_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: MixpeekSDK) -> None:
        with client.collections.with_streaming_response.search(
            collection_id="collection_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.list(
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.delete(
            collection_id="collection_id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.delete(
            collection_id="collection_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.with_raw_response.delete(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.with_streaming_response.delete(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.collections.with_raw_response.delete(
                collection_id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.search(
            collection_id="collection_id",
            query="query",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        collection = await async_client.collections.search(
            collection_id="collection_id",
            query="query",
            page=1,
            page_size=1,
            sort_by="sort_by",
            sort_order="asc",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.with_raw_response.search(
            collection_id="collection_id",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.with_streaming_response.search(
            collection_id="collection_id",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True
