# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types import IndexTextResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndex:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_text(self, client: Mixpeek) -> None:
        index = client.index.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        )
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: Mixpeek) -> None:
        index = client.index.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            text_settings={
                "embed": {"model_id": "multimodal-v1"},
                "fulltext": {"model_id": "splade-v3"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "key_phrases": ["str"],
                        "sentiment": "str",
                    },
                },
            },
            index_id="index-id",
        )
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: Mixpeek) -> None:
        response = client.index.with_raw_response.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: Mixpeek) -> None:
        with client.index.with_streaming_response.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexTextResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndex:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_text(self, async_client: AsyncMixpeek) -> None:
        index = await async_client.index.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        )
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncMixpeek) -> None:
        index = await async_client.index.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            text_settings={
                "embed": {"model_id": "multimodal-v1"},
                "fulltext": {"model_id": "splade-v3"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "key_phrases": ["str"],
                        "sentiment": "str",
                    },
                },
            },
            index_id="index-id",
        )
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.index.with_raw_response.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexTextResponse, index, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncMixpeek) -> None:
        async with async_client.index.with_streaming_response.text(
            collection_id="my_document_collection",
            text="the quick brown fox jumps over the lazy dog",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexTextResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True
