# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRead:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MixpeekSDK) -> None:
        read = client.read.create()
        assert_matches_type(object, read, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MixpeekSDK) -> None:
        read = client.read.create(
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, read, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MixpeekSDK) -> None:
        response = client.read.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = response.parse()
        assert_matches_type(object, read, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MixpeekSDK) -> None:
        with client.read.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = response.parse()
            assert_matches_type(object, read, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRead:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeekSDK) -> None:
        read = await async_client.read.create()
        assert_matches_type(object, read, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        read = await async_client.read.create(
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, read, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.read.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        read = await response.parse()
        assert_matches_type(object, read, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.read.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            read = await response.parse()
            assert_matches_type(object, read, path=["response"])

        assert cast(Any, response.is_closed) is True
