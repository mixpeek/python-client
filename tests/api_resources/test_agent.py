# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type
from mixpeek.types import Agentresponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MixpeekSDK) -> None:
        agent = client.agent.create(
            prompt="prompt",
        )
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MixpeekSDK) -> None:
        agent = client.agent.create(
            prompt="prompt",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MixpeekSDK) -> None:
        response = client.agent.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MixpeekSDK) -> None:
        with client.agent.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agentresponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeekSDK) -> None:
        agent = await async_client.agent.create(
            prompt="prompt",
        )
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        agent = await async_client.agent.create(
            prompt="prompt",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.agent.with_raw_response.create(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agentresponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.agent.with_streaming_response.create(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agentresponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
