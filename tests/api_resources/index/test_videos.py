# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types.index import VideoURLResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVideos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_url(self, client: Mixpeek) -> None:
        video = client.index.videos.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: Mixpeek) -> None:
        video = client.index.videos.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            feature_extractors=[
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
            ],
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: Mixpeek) -> None:
        response = client.index.videos.with_raw_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = response.parse()
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: Mixpeek) -> None:
        with client.index.videos.with_streaming_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = response.parse()
            assert_matches_type(VideoURLResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVideos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeek) -> None:
        video = await async_client.index.videos.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeek) -> None:
        video = await async_client.index.videos.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
            asset_update={
                "asset_id": "asset_id",
                "mode": "replace",
            },
            feature_extractors=[
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
                {
                    "describe": {
                        "enabled": True,
                        "json_output": {},
                        "max_length": 0,
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "detect": {
                        "faces": {
                            "confidence_threshold": 0.8,
                            "enabled": True,
                        },
                        "logos": {
                            "confidence_threshold": 0,
                            "enabled": True,
                        },
                    },
                    "embed": [
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "https://example.com/image.jpg",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "lorem ipsum",
                        },
                        {
                            "type": "url",
                            "vector_index": "image_vector",
                            "field_name": "description",
                            "value": "Thing #1",
                        },
                    ],
                    "interval_sec": 15,
                    "json_output": {
                        "prompt": "prompt",
                        "response_shape": {
                            "objects": ["str"],
                            "scenes": ["str"],
                        },
                    },
                    "read": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                    "transcribe": {
                        "enabled": True,
                        "json_output": {},
                        "prompt": "prompt",
                        "vector_index": "image_vector",
                    },
                },
            ],
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            x_namespace="X-Namespace",
        )
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.index.videos.with_raw_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        video = await response.parse()
        assert_matches_type(VideoURLResponse, video, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeek) -> None:
        async with async_client.index.videos.with_streaming_response.url(
            collection_id="my_document_collection",
            url="https://example.com/sample-video.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            video = await response.parse()
            assert_matches_type(VideoURLResponse, video, path=["response"])

        assert cast(Any, response.is_closed) is True
