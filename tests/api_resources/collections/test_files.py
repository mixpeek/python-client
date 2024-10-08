# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import MixpeekSDK, AsyncMixpeekSDK
from tests.utils import assert_matches_type
from mixpeek.types.collections import (
    Fileresponse,
    Groupedfiledata,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MixpeekSDK) -> None:
        file = client.collections.files.create(
            collection_id="collection_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MixpeekSDK) -> None:
        file = client.collections.files.create(
            collection_id="collection_id",
            filters={},
            page=1,
            page_size=1,
            randomize=True,
            sort_by="sort_by",
            sort_order="asc",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MixpeekSDK) -> None:
        response = client.collections.files.with_raw_response.create(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MixpeekSDK) -> None:
        with client.collections.files.with_streaming_response.create(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: MixpeekSDK) -> None:
        file = client.collections.files.retrieve(
            file_id="file_id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: MixpeekSDK) -> None:
        file = client.collections.files.retrieve(
            file_id="file_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: MixpeekSDK) -> None:
        response = client.collections.files.with_raw_response.retrieve(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: MixpeekSDK) -> None:
        with client.collections.files.with_streaming_response.retrieve(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Fileresponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.collections.files.with_raw_response.retrieve(
                file_id="",
            )

    @parametrize
    def test_method_update(self, client: MixpeekSDK) -> None:
        file = client.collections.files.update(
            file_id="file_id",
            body={},
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: MixpeekSDK) -> None:
        file = client.collections.files.update(
            file_id="file_id",
            body={},
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: MixpeekSDK) -> None:
        response = client.collections.files.with_raw_response.update(
            file_id="file_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: MixpeekSDK) -> None:
        with client.collections.files.with_streaming_response.update(
            file_id="file_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Fileresponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.collections.files.with_raw_response.update(
                file_id="",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: MixpeekSDK) -> None:
        file = client.collections.files.delete(
            file_id="file_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: MixpeekSDK) -> None:
        file = client.collections.files.delete(
            file_id="file_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: MixpeekSDK) -> None:
        response = client.collections.files.with_raw_response.delete(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: MixpeekSDK) -> None:
        with client.collections.files.with_streaming_response.delete(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.collections.files.with_raw_response.delete(
                file_id="",
            )

    @parametrize
    def test_method_full(self, client: MixpeekSDK) -> None:
        file = client.collections.files.full(
            file_id="file_id",
        )
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    def test_method_full_with_all_params(self, client: MixpeekSDK) -> None:
        file = client.collections.files.full(
            file_id="file_id",
            modality="modality",
            page=1,
            page_size=1,
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    def test_raw_response_full(self, client: MixpeekSDK) -> None:
        response = client.collections.files.with_raw_response.full(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    def test_streaming_response_full(self, client: MixpeekSDK) -> None:
        with client.collections.files.with_streaming_response.full(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(Groupedfiledata, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_full(self, client: MixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.collections.files.with_raw_response.full(
                file_id="",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.create(
            collection_id="collection_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.create(
            collection_id="collection_id",
            filters={},
            page=1,
            page_size=1,
            randomize=True,
            sort_by="sort_by",
            sort_order="asc",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.files.with_raw_response.create(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.files.with_streaming_response.create(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.retrieve(
            file_id="file_id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.retrieve(
            file_id="file_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.files.with_raw_response.retrieve(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.files.with_streaming_response.retrieve(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Fileresponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.collections.files.with_raw_response.retrieve(
                file_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.update(
            file_id="file_id",
            body={},
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.update(
            file_id="file_id",
            body={},
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.files.with_raw_response.update(
            file_id="file_id",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Fileresponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.files.with_streaming_response.update(
            file_id="file_id",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Fileresponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.collections.files.with_raw_response.update(
                file_id="",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.delete(
            file_id="file_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.delete(
            file_id="file_id",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.files.with_raw_response.delete(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.files.with_streaming_response.delete(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.collections.files.with_raw_response.delete(
                file_id="",
            )

    @parametrize
    async def test_method_full(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.full(
            file_id="file_id",
        )
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    async def test_method_full_with_all_params(self, async_client: AsyncMixpeekSDK) -> None:
        file = await async_client.collections.files.full(
            file_id="file_id",
            modality="modality",
            page=1,
            page_size=1,
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    async def test_raw_response_full(self, async_client: AsyncMixpeekSDK) -> None:
        response = await async_client.collections.files.with_raw_response.full(
            file_id="file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(Groupedfiledata, file, path=["response"])

    @parametrize
    async def test_streaming_response_full(self, async_client: AsyncMixpeekSDK) -> None:
        async with async_client.collections.files.with_streaming_response.full(
            file_id="file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(Groupedfiledata, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_full(self, async_client: AsyncMixpeekSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.collections.files.with_raw_response.full(
                file_id="",
            )
