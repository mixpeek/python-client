# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type
from mixpeek.types import Embeddingresponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MixpeekSDK) -> None:
        embed = client.embed.create(
            input="input",
        )
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MixpeekSDK) -> None:
        embed = client.embed.create(
            input="input",
            input_type="text",
            modality="video",
            model_id={},
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MixpeekSDK) -> None:
        response = client.embed.with_raw_response.create(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = response.parse()
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MixpeekSDK) -> None:
        with client.embed.with_streaming_response.create(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = response.parse()
            assert_matches_type(Embeddingresponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeekSDK) -> None:
        embed = await async_client.embed.create(
            input="input",
        )
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        embed = await async_client.embed.create(
            input="input",
            input_type="text",
            modality="video",
            model_id={},
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.embed.with_raw_response.create(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embed = await response.parse()
        assert_matches_type(Embeddingresponse, embed, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.embed.with_streaming_response.create(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embed = await response.parse()
            assert_matches_type(Embeddingresponse, embed, path=["response"])

        assert cast(Any, response.is_closed) is True
