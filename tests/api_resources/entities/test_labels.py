# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types.entities import LabelResponse, LabelListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Mixpeek) -> None:
        label = client.entities.labels.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        )
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixpeek) -> None:
        label = client.entities.labels.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
            index_id="index-id",
        )
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixpeek) -> None:
        response = client.entities.labels.with_raw_response.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixpeek) -> None:
        with client.entities.labels.with_streaming_response.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_label_id` but received ''"):
            client.entities.labels.with_raw_response.update(
                path_label_id="",
                body_label_id="",
                metadata={},
            )

    @parametrize
    def test_method_list(self, client: Mixpeek) -> None:
        label = client.entities.labels.list()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixpeek) -> None:
        label = client.entities.labels.list(
            page=0,
            page_size=0,
            index_id="index-id",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixpeek) -> None:
        response = client.entities.labels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixpeek) -> None:
        with client.entities.labels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mixpeek) -> None:
        label = client.entities.labels.delete(
            label_id="label_id",
        )
        assert_matches_type(object, label, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Mixpeek) -> None:
        label = client.entities.labels.delete(
            label_id="label_id",
            index_id="index-id",
        )
        assert_matches_type(object, label, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixpeek) -> None:
        response = client.entities.labels.with_raw_response.delete(
            label_id="label_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(object, label, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixpeek) -> None:
        with client.entities.labels.with_streaming_response.delete(
            label_id="label_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(object, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            client.entities.labels.with_raw_response.delete(
                label_id="",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        )
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
            index_id="index-id",
        )
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.labels.with_raw_response.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.labels.with_streaming_response.update(
            path_label_id="label_id",
            body_label_id="label_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_label_id` but received ''"):
            await async_client.entities.labels.with_raw_response.update(
                path_label_id="",
                body_label_id="",
                metadata={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.list()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.list(
            page=0,
            page_size=0,
            index_id="index-id",
        )
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.labels.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(LabelListResponse, label, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.labels.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(LabelListResponse, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.delete(
            label_id="label_id",
        )
        assert_matches_type(object, label, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeek) -> None:
        label = await async_client.entities.labels.delete(
            label_id="label_id",
            index_id="index-id",
        )
        assert_matches_type(object, label, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.labels.with_raw_response.delete(
            label_id="label_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(object, label, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.labels.with_streaming_response.delete(
            label_id="label_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(object, label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `label_id` but received ''"):
            await async_client.entities.labels.with_raw_response.delete(
                label_id="",
            )
