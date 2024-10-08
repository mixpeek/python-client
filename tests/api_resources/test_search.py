# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_text(self, client: MixpeekSDK) -> None:
        search = client.search.text(
            input="input",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: MixpeekSDK) -> None:
        search = client.search.text(
            input="input",
            filters={},
            group_by_file=True,
            input_type="input_type",
            modality="modality",
            model_id="model_id",
            pagination={
                "page": 1,
                "page_size": 1,
            },
            source="source",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: MixpeekSDK) -> None:
        response = client.search.with_raw_response.text(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: MixpeekSDK) -> None:
        with client.search.with_streaming_response.text(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: MixpeekSDK) -> None:
        search = client.search.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: MixpeekSDK) -> None:
        search = client.search.upload(
            file=b"raw file contents",
            filters="filters",
            page=0,
            page_size=0,
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: MixpeekSDK) -> None:
        response = client.search.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: MixpeekSDK) -> None:
        with client.search.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_url(self, client: MixpeekSDK) -> None:
        search = client.search.url(
            input="input",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: MixpeekSDK) -> None:
        search = client.search.url(
            input="input",
            filters={},
            group_by_file=True,
            input_type="input_type",
            modality="modality",
            model_id="model_id",
            pagination={
                "page": 1,
                "page_size": 1,
            },
            source="source",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: MixpeekSDK) -> None:
        response = client.search.with_raw_response.url(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: MixpeekSDK) -> None:
        with client.search.with_streaming_response.url(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_text(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.text(
            input="input",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.text(
            input="input",
            filters={},
            group_by_file=True,
            input_type="input_type",
            modality="modality",
            model_id="model_id",
            pagination={
                "page": 1,
                "page_size": 1,
            },
            source="source",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.search.with_raw_response.text(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.search.with_streaming_response.text(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.upload(
            file=b"raw file contents",
            filters="filters",
            page=0,
            page_size=0,
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.search.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.search.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.url(
            input="input",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        search = await async_client.search.url(
            input="input",
            filters={},
            group_by_file=True,
            input_type="input_type",
            modality="modality",
            model_id="model_id",
            pagination={
                "page": 1,
                "page_size": 1,
            },
            source="source",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.search.with_raw_response.url(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.search.with_streaming_response.url(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True
