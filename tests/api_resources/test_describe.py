# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDescribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upload(self, client: MixpeekSDK) -> None:
        describe = client.describe.upload(
            file=b"raw file contents",
            prompt="prompt",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: MixpeekSDK) -> None:
        describe = client.describe.upload(
            file=b"raw file contents",
            prompt="prompt",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: MixpeekSDK) -> None:
        response = client.describe.with_raw_response.upload(
            file=b"raw file contents",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        describe = response.parse()
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: MixpeekSDK) -> None:
        with client.describe.with_streaming_response.upload(
            file=b"raw file contents",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            describe = response.parse()
            assert_matches_type(object, describe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_url(self, client: MixpeekSDK) -> None:
        describe = client.describe.url(
            prompt="prompt",
            url="https://example.com",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: MixpeekSDK) -> None:
        describe = client.describe.url(
            prompt="prompt",
            url="https://example.com",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: MixpeekSDK) -> None:
        response = client.describe.with_raw_response.url(
            prompt="prompt",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        describe = response.parse()
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: MixpeekSDK) -> None:
        with client.describe.with_streaming_response.url(
            prompt="prompt",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            describe = response.parse()
            assert_matches_type(object, describe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDescribe:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_upload(self, async_client: AsyncMixpeekSDK) -> None:
        describe = await async_client.describe.upload(
            file=b"raw file contents",
            prompt="prompt",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        describe = await async_client.describe.upload(
            file=b"raw file contents",
            prompt="prompt",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.describe.with_raw_response.upload(
            file=b"raw file contents",
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        describe = await response.parse()
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.describe.with_streaming_response.upload(
            file=b"raw file contents",
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            describe = await response.parse()
            assert_matches_type(object, describe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeekSDK) -> None:
        describe = await async_client.describe.url(
            prompt="prompt",
            url="https://example.com",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        describe = await async_client.describe.url(
            prompt="prompt",
            url="https://example.com",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.describe.with_raw_response.url(
            prompt="prompt",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        describe = await response.parse()
        assert_matches_type(object, describe, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.describe.with_streaming_response.url(
            prompt="prompt",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            describe = await response.parse()
            assert_matches_type(object, describe, path=["response"])

        assert cast(Any, response.is_closed) is True
