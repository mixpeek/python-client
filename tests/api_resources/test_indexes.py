# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_face(self, client: MixpeekSDK) -> None:
        index = client.indexes.face(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_method_face_with_all_params(self, client: MixpeekSDK) -> None:
        index = client.indexes.face(
            collection_id="collection_id",
            file=b"raw file contents",
            metadata="metadata",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_face(self, client: MixpeekSDK) -> None:
        response = client.indexes.with_raw_response.face(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_face(self, client: MixpeekSDK) -> None:
        with client.indexes.with_streaming_response.face(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: MixpeekSDK) -> None:
        index = client.indexes.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: MixpeekSDK) -> None:
        index = client.indexes.upload(
            collection_id="collection_id",
            file=b"raw file contents",
            image_settings="image_settings",
            metadata="metadata",
            video_settings="video_settings",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: MixpeekSDK) -> None:
        response = client.indexes.with_raw_response.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: MixpeekSDK) -> None:
        with client.indexes.with_streaming_response.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_url(self, client: MixpeekSDK) -> None:
        index = client.indexes.url(
            collection_id="collection_id",
            url="url",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: MixpeekSDK) -> None:
        index = client.indexes.url(
            collection_id="collection_id",
            url="url",
            image_settings={
                "describe": {
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {"faces": {"model_id": "face-detector-v1"}},
                "embed": {"model_id": "image-embed-v1"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {},
                },
                "read": {
                    "json_format": {},
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
            },
            metadata={},
            should_save=True,
            video_settings={
                "describe": {
                    "model_id": "video-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {"faces": {"model_id": "face-detector-v1"}},
                "embed": {
                    "contextual_text": "contextual_text",
                    "model_id": "vuse-generic-v1",
                },
                "interval_sec": 0,
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {},
                },
                "read": {
                    "json_format": {},
                    "model_id": "video-descriptor-v1",
                    "prompt": "prompt",
                },
                "transcribe": {
                    "model_id": "polyglot-v1",
                    "prompt": "prompt",
                },
            },
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: MixpeekSDK) -> None:
        response = client.indexes.with_raw_response.url(
            collection_id="collection_id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: MixpeekSDK) -> None:
        with client.indexes.with_streaming_response.url(
            collection_id="collection_id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_face(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.face(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_method_face_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.face(
            collection_id="collection_id",
            file=b"raw file contents",
            metadata="metadata",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_face(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.indexes.with_raw_response.face(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_face(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.indexes.with_streaming_response.face(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.upload(
            collection_id="collection_id",
            file=b"raw file contents",
            image_settings="image_settings",
            metadata="metadata",
            video_settings="video_settings",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.indexes.with_raw_response.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.indexes.with_streaming_response.upload(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.url(
            collection_id="collection_id",
            url="url",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        index = await async_client.indexes.url(
            collection_id="collection_id",
            url="url",
            image_settings={
                "describe": {
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {"faces": {"model_id": "face-detector-v1"}},
                "embed": {"model_id": "image-embed-v1"},
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {},
                },
                "read": {
                    "json_format": {},
                    "model_id": "image-descriptor-v1",
                    "prompt": "prompt",
                },
            },
            metadata={},
            should_save=True,
            video_settings={
                "describe": {
                    "model_id": "video-descriptor-v1",
                    "prompt": "prompt",
                },
                "detect": {"faces": {"model_id": "face-detector-v1"}},
                "embed": {
                    "contextual_text": "contextual_text",
                    "model_id": "vuse-generic-v1",
                },
                "interval_sec": 0,
                "json_output": {
                    "prompt": "prompt",
                    "response_shape": {},
                },
                "read": {
                    "json_format": {},
                    "model_id": "video-descriptor-v1",
                    "prompt": "prompt",
                },
                "transcribe": {
                    "model_id": "polyglot-v1",
                    "prompt": "prompt",
                },
            },
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.indexes.with_raw_response.url(
            collection_id="collection_id",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.indexes.with_streaming_response.url(
            collection_id="collection_id",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True
