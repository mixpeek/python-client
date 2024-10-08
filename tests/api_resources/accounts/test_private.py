# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type
from mixpeek._utils import parse_datetime
from mixpeek.types.accounts import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrivate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: MixpeekSDK) -> None:
        private = client.accounts.private.update()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MixpeekSDK) -> None:
        private = client.accounts.private.update(
            api_keys=[
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
            ],
            metadata={},
        )
        assert_matches_type(User, private, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MixpeekSDK) -> None:
        response = client.accounts.private.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = response.parse()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MixpeekSDK) -> None:
        with client.accounts.private.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = response.parse()
            assert_matches_type(User, private, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: MixpeekSDK) -> None:
        private = client.accounts.private.list()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MixpeekSDK) -> None:
        response = client.accounts.private.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = response.parse()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MixpeekSDK) -> None:
        with client.accounts.private.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = response.parse()
            assert_matches_type(User, private, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrivate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeekSDK) -> None:
        private = await async_client.accounts.private.update()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        private = await async_client.accounts.private.update(
            api_keys=[
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
                {
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "key": "key",
                    "name": "name",
                },
            ],
            metadata={},
        )
        assert_matches_type(User, private, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.accounts.private.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = await response.parse()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.accounts.private.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = await response.parse()
            assert_matches_type(User, private, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeekSDK) -> None:
        private = await async_client.accounts.private.list()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.accounts.private.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        private = await response.parse()
        assert_matches_type(User, private, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.accounts.private.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            private = await response.parse()
            assert_matches_type(User, private, path=["response"])

        assert cast(Any, response.is_closed) is True
