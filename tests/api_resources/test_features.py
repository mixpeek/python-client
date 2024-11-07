# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types import (
    Feature,
    FeatureListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mixpeek) -> None:
        feature = client.features.retrieve(
            feature_id="feature_id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mixpeek) -> None:
        feature = client.features.retrieve(
            feature_id="feature_id",
            include_vectors=True,
            index_id="index-id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixpeek) -> None:
        response = client.features.with_raw_response.retrieve(
            feature_id="feature_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixpeek) -> None:
        with client.features.with_streaming_response.retrieve(
            feature_id="feature_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.features.with_raw_response.retrieve(
                feature_id="",
            )

    @parametrize
    def test_method_update(self, client: Mixpeek) -> None:
        feature = client.features.update(
            feature_id="feature_id",
            metadata={},
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixpeek) -> None:
        feature = client.features.update(
            feature_id="feature_id",
            metadata={},
            index_id="index-id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixpeek) -> None:
        response = client.features.with_raw_response.update(
            feature_id="feature_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixpeek) -> None:
        with client.features.with_streaming_response.update(
            feature_id="feature_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.features.with_raw_response.update(
                feature_id="",
                metadata={},
            )

    @parametrize
    def test_method_list(self, client: Mixpeek) -> None:
        feature = client.features.list(
            collection_ids=["string", "string", "string"],
        )
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixpeek) -> None:
        feature = client.features.list(
            collection_ids=["string", "string", "string"],
            offset_feature_id="offset_feature_id",
            page_size=0,
            filters={"case_sensitive": True},
            select=[{}, {}, {}],
            sort={
                "direction": "asc",
                "field": "score",
            },
            index_id="index-id",
        )
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixpeek) -> None:
        response = client.features.with_raw_response.list(
            collection_ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixpeek) -> None:
        with client.features.with_streaming_response.list(
            collection_ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(FeatureListResponse, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mixpeek) -> None:
        feature = client.features.delete(
            feature_id="feature_id",
        )
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Mixpeek) -> None:
        feature = client.features.delete(
            feature_id="feature_id",
            index_id="index-id",
        )
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixpeek) -> None:
        response = client.features.with_raw_response.delete(
            feature_id="feature_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixpeek) -> None:
        with client.features.with_streaming_response.delete(
            feature_id="feature_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(object, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            client.features.with_raw_response.delete(
                feature_id="",
            )


class TestAsyncFeatures:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.retrieve(
            feature_id="feature_id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.retrieve(
            feature_id="feature_id",
            include_vectors=True,
            index_id="index-id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.with_raw_response.retrieve(
            feature_id="feature_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.with_streaming_response.retrieve(
            feature_id="feature_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.features.with_raw_response.retrieve(
                feature_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.update(
            feature_id="feature_id",
            metadata={},
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.update(
            feature_id="feature_id",
            metadata={},
            index_id="index-id",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.with_raw_response.update(
            feature_id="feature_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.with_streaming_response.update(
            feature_id="feature_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.features.with_raw_response.update(
                feature_id="",
                metadata={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.list(
            collection_ids=["string", "string", "string"],
        )
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.list(
            collection_ids=["string", "string", "string"],
            offset_feature_id="offset_feature_id",
            page_size=0,
            filters={"case_sensitive": True},
            select=[{}, {}, {}],
            sort={
                "direction": "asc",
                "field": "score",
            },
            index_id="index-id",
        )
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.with_raw_response.list(
            collection_ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(FeatureListResponse, feature, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.with_streaming_response.list(
            collection_ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(FeatureListResponse, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.delete(
            feature_id="feature_id",
        )
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeek) -> None:
        feature = await async_client.features.delete(
            feature_id="feature_id",
            index_id="index-id",
        )
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.features.with_raw_response.delete(
            feature_id="feature_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(object, feature, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeek) -> None:
        async with async_client.features.with_streaming_response.delete(
            feature_id="feature_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(object, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feature_id` but received ''"):
            await async_client.features.with_raw_response.delete(
                feature_id="",
            )
