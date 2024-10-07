# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek_sdk import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTask:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: MixpeekSDK) -> None:
        task = client.agent.task.retrieve(
            task_id="task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: MixpeekSDK) -> None:
        task = client.agent.task.retrieve(
            task_id="task_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MixpeekSDK) -> None:
        response = client.agent.task.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MixpeekSDK) -> None:
        with client.agent.task.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.agent.task.with_raw_response.retrieve(
                task_id="",
            )


class TestAsyncTask:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        task = await async_client.agent.task.retrieve(
            task_id="task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        task = await async_client.agent.task.retrieve(
            task_id="task_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.agent.task.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.agent.task.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.agent.task.with_raw_response.retrieve(
                task_id="",
            )
