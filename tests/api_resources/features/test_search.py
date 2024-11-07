# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: Mixpeek) -> None:
        search = client.features.search.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_feedback_with_all_params(self, client: Mixpeek) -> None:
        search = client.features.search.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
            feedback_text="feedback_text",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Mixpeek) -> None:
        response = client.features.search.with_raw_response.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Mixpeek) -> None:
        with client.features.search.with_streaming_response.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_file(self, client: Mixpeek) -> None:
        search = client.features.search.file(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_file_with_all_params(self, client: Mixpeek) -> None:
        search = client.features.search.file(
            file=b"raw file contents",
            offset_position=0,
            page_size=1,
            filters="filters",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_file(self, client: Mixpeek) -> None:
        response = client.features.search.with_raw_response.file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_file(self, client: Mixpeek) -> None:
        with client.features.search.with_streaming_response.file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_text(self, client: Mixpeek) -> None:
        search = client.features.search.text(
            collection_ids=["collection1", "collection2"],
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: Mixpeek) -> None:
        search = client.features.search.text(
            collection_ids=["collection1", "collection2"],
            offset_position=0,
            page_size=1,
            filters={"case_sensitive": True},
            group_by={
                "field": "file_id",
                "max_features": 10,
                "sort": {
                    "direction": "asc",
                    "field": "metadata.field_name",
                },
            },
            model_id="vuse-generic-v1",
            query="query",
            search_type="semantic",
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "relevance",
            },
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: Mixpeek) -> None:
        response = client.features.search.with_raw_response.text(
            collection_ids=["collection1", "collection2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: Mixpeek) -> None:
        with client.features.search.with_streaming_response.text(
            collection_ids=["collection1", "collection2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_url(self, client: Mixpeek) -> None:
        search = client.features.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: Mixpeek) -> None:
        search = client.features.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
            offset_position=0,
            page_size=1,
            filters={"case_sensitive": True},
            group_by={
                "field": "file_id",
                "max_features": 10,
                "sort": {
                    "direction": "asc",
                    "field": "metadata.field_name",
                },
            },
            model_id="vuse-generic-v1",
            search_type="semantic",
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "relevance",
            },
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: Mixpeek) -> None:
        response = client.features.search.with_raw_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: Mixpeek) -> None:
        with client.features.search.with_streaming_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_feedback_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
            feedback_text="feedback_text",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.search.with_raw_response.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.search.with_streaming_response.feedback(
            feature_id="feature_id",
            is_relevant=True,
            search_id="search_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_file(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.file(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_file_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.file(
            file=b"raw file contents",
            offset_position=0,
            page_size=1,
            filters="filters",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_file(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.search.with_raw_response.file(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_file(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.search.with_streaming_response.file(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_text(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.text(
            collection_ids=["collection1", "collection2"],
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.text(
            collection_ids=["collection1", "collection2"],
            offset_position=0,
            page_size=1,
            filters={"case_sensitive": True},
            group_by={
                "field": "file_id",
                "max_features": 10,
                "sort": {
                    "direction": "asc",
                    "field": "metadata.field_name",
                },
            },
            model_id="vuse-generic-v1",
            query="query",
            search_type="semantic",
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "relevance",
            },
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.search.with_raw_response.text(
            collection_ids=["collection1", "collection2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.search.with_streaming_response.text(
            collection_ids=["collection1", "collection2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.features.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
            offset_position=0,
            page_size=1,
            filters={"case_sensitive": True},
            group_by={
                "field": "file_id",
                "max_features": 10,
                "sort": {
                    "direction": "asc",
                    "field": "metadata.field_name",
                },
            },
            model_id="vuse-generic-v1",
            search_type="semantic",
            select=["title", "content", "metadata.author", "metadata.publication_date"],
            sort={
                "direction": "asc",
                "field": "relevance",
            },
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.search.with_raw_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.search.with_streaming_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True
