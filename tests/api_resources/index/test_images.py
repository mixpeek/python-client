# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types.index import ImageURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_url(self, client: Mixpeek) -> None:
        image = client.index.images.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: Mixpeek) -> None:
        image = client.index.images.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            image_settings={
                "describe": {
                    "json_output": {},
                    "max_length": 100,
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {
                    "faces": {
                        "confidence_threshold": 0.8,
                        "model_id": "face-detector-v1",
                    },
                    "logos": {
                        "confidence_threshold": 0,
                        "model_id": "logo-detector-v1",
                    },
                },
                "embed": {"model_id": "multimodal-v1"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "colors": ["str"],
                        "objects": ["str"],
                    },
                },
                "read": {
                    "json_output": {},
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            prevent_duplicate=False,
            should_save=True,
            index_id="index-id",
        )
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: Mixpeek) -> None:
        response = client.index.images.with_raw_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: Mixpeek) -> None:
        with client.index.images.with_streaming_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImageURLResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeek) -> None:
        image = await async_client.index.images.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeek) -> None:
        image = await async_client.index.images.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            image_settings={
                "describe": {
                    "json_output": {},
                    "max_length": 100,
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {
                    "faces": {
                        "confidence_threshold": 0.8,
                        "model_id": "face-detector-v1",
                    },
                    "logos": {
                        "confidence_threshold": 0,
                        "model_id": "logo-detector-v1",
                    },
                },
                "embed": {"model_id": "multimodal-v1"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "colors": ["str"],
                        "objects": ["str"],
                    },
                },
                "read": {
                    "json_output": {},
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            prevent_duplicate=False,
            should_save=True,
            index_id="index-id",
        )
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.index.images.with_raw_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(ImageURLResponse, image, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeek) -> None:
        async with async_client.index.images.with_streaming_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImageURLResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True
