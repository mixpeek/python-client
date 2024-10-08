# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_url(self, client: MixpeekSDK) -> None:
        transcribe = client.transcribe.url(
            url="https://example.com",
        )
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: MixpeekSDK) -> None:
        transcribe = client.transcribe.url(
            url="https://example.com",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: MixpeekSDK) -> None:
        response = client.transcribe.with_raw_response.url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcribe = response.parse()
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: MixpeekSDK) -> None:
        with client.transcribe.with_streaming_response.url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcribe = response.parse()
            assert_matches_type(object, transcribe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscribe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeekSDK) -> None:
        transcribe = await async_client.transcribe.url(
            url="https://example.com",
        )
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        transcribe = await async_client.transcribe.url(
            url="https://example.com",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.transcribe.with_raw_response.url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcribe = await response.parse()
        assert_matches_type(object, transcribe, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.transcribe.with_streaming_response.url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcribe = await response.parse()
            assert_matches_type(object, transcribe, path=["response"])

        assert cast(Any, response.is_closed) is True
