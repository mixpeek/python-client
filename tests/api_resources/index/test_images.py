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
            feature_extractors={
                "describe": {
                    "enabled": True,
                    "json_output": {},
                    "max_length": 1000,
                    "prompt": "prompt",
                    "vector_index": "image",
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
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "https://example.com/image.jpg",
                    },
                    {
                        "type": "url",
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "lorem ipsum",
                    },
                    {
                        "type": "url",
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "Thing #1",
                    },
                ],
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "colors": ["str"],
                        "objects": ["str"],
                    },
                },
                "read": {
                    "enabled": True,
                    "json_output": {},
                    "prompt": "prompt",
                    "vector_index": "image",
                },
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            percolate={
                "enabled": True,
                "filters": {
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
                "max_candidates": 0,
                "min_relevance": 0.8,
            },
            x_namespace="X-Namespace",
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
            feature_extractors={
                "describe": {
                    "enabled": True,
                    "json_output": {},
                    "max_length": 1000,
                    "prompt": "prompt",
                    "vector_index": "image",
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
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "https://example.com/image.jpg",
                    },
                    {
                        "type": "url",
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "lorem ipsum",
                    },
                    {
                        "type": "url",
                        "vector_index": "image",
                        "field_name": "description",
                        "value": "Thing #1",
                    },
                ],
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {
                        "colors": ["str"],
                        "objects": ["str"],
                    },
                },
                "read": {
                    "enabled": True,
                    "json_output": {},
                    "prompt": "prompt",
                    "vector_index": "image",
                },
            },
            metadata={
                "author": "John Doe",
                "category": "Research Paper",
                "tags": ["AI", "Machine Learning"],
            },
            percolate={
                "enabled": True,
                "filters": {
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
                "max_candidates": 0,
                "min_relevance": 0.8,
            },
            x_namespace="X-Namespace",
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
