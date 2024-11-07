# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types import HealthCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealthcheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mixpeek) -> None:
        healthcheck = client.healthcheck.retrieve()
        assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixpeek) -> None:
        response = client.healthcheck.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = response.parse()
        assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixpeek) -> None:
        with client.healthcheck.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = response.parse()
            assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealthcheck:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeek) -> None:
        healthcheck = await async_client.healthcheck.retrieve()
        assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.healthcheck.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthcheck = await response.parse()
        assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        async with async_client.healthcheck.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthcheck = await response.parse()
            assert_matches_type(HealthCheckResponse, healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True
