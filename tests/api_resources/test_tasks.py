# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types.shared import TaskResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mixpeek) -> None:
        task = client.tasks.retrieve(
            task_id="task_id",
        )
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mixpeek) -> None:
        task = client.tasks.retrieve(
            task_id="task_id",
            index_id="index-id",
        )
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixpeek) -> None:
        response = client.tasks.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixpeek) -> None:
        with client.tasks.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                task_id="",
            )

    @parametrize
    def test_method_delete(self, client: Mixpeek) -> None:
        task = client.tasks.delete(
            task_id="task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Mixpeek) -> None:
        task = client.tasks.delete(
            task_id="task_id",
            index_id="index-id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixpeek) -> None:
        response = client.tasks.with_raw_response.delete(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixpeek) -> None:
        with client.tasks.with_streaming_response.delete(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.delete(
                task_id="",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeek) -> None:
        task = await async_client.tasks.retrieve(
            task_id="task_id",
        )
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixpeek) -> None:
        task = await async_client.tasks.retrieve(
            task_id="task_id",
            index_id="index-id",
        )
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                task_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeek) -> None:
        task = await async_client.tasks.delete(
            task_id="task_id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeek) -> None:
        task = await async_client.tasks.delete(
            task_id="task_id",
            index_id="index-id",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.tasks.with_raw_response.delete(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeek) -> None:
        async with async_client.tasks.with_streaming_response.delete(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.delete(
                task_id="",
            )
