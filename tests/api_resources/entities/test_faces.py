# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type
from mixpeek.types.entities import (
    FaceResponse,
    FaceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixpeek) -> None:
        face = client.entities.faces.create(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixpeek) -> None:
        face = client.entities.faces.create(
            collection_id="collection_id",
            file=b"raw file contents",
            metadata="metadata",
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixpeek) -> None:
        response = client.entities.faces.with_raw_response.create(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixpeek) -> None:
        with client.entities.faces.with_streaming_response.create(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Mixpeek) -> None:
        face = client.entities.faces.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixpeek) -> None:
        face = client.entities.faces.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixpeek) -> None:
        response = client.entities.faces.with_raw_response.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixpeek) -> None:
        with client.entities.faces.with_streaming_response.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_face_id` but received ''"):
            client.entities.faces.with_raw_response.update(
                path_face_id="",
                collection_id="collection_id",
                body_face_id="",
                metadata={},
            )

    @parametrize
    def test_method_list(self, client: Mixpeek) -> None:
        face = client.entities.faces.list(
            collection_id="collection_id",
        )
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixpeek) -> None:
        face = client.entities.faces.list(
            collection_id="collection_id",
            page=0,
            page_size=0,
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixpeek) -> None:
        response = client.entities.faces.with_raw_response.list(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixpeek) -> None:
        with client.entities.faces.with_streaming_response.list(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(FaceListResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.entities.faces.with_raw_response.list(
                collection_id="",
            )

    @parametrize
    def test_method_delete(self, client: Mixpeek) -> None:
        face = client.entities.faces.delete(
            face_id="face_id",
        )
        assert_matches_type(object, face, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Mixpeek) -> None:
        face = client.entities.faces.delete(
            face_id="face_id",
            x_namespace="X-Namespace",
        )
        assert_matches_type(object, face, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixpeek) -> None:
        response = client.entities.faces.with_raw_response.delete(
            face_id="face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(object, face, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixpeek) -> None:
        with client.entities.faces.with_streaming_response.delete(
            face_id="face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(object, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            client.entities.faces.with_raw_response.delete(
                face_id="",
            )


class TestAsyncFaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.create(
            collection_id="collection_id",
            file=b"raw file contents",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.create(
            collection_id="collection_id",
            file=b"raw file contents",
            metadata="metadata",
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.faces.with_raw_response.create(
            collection_id="collection_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.faces.with_streaming_response.create(
            collection_id="collection_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.faces.with_raw_response.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.faces.with_streaming_response.update(
            path_face_id="face_id",
            collection_id="collection_id",
            body_face_id="face_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_face_id` but received ''"):
            await async_client.entities.faces.with_raw_response.update(
                path_face_id="",
                collection_id="collection_id",
                body_face_id="",
                metadata={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.list(
            collection_id="collection_id",
        )
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.list(
            collection_id="collection_id",
            page=0,
            page_size=0,
            x_namespace="X-Namespace",
        )
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.faces.with_raw_response.list(
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(FaceListResponse, face, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.faces.with_streaming_response.list(
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(FaceListResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.entities.faces.with_raw_response.list(
                collection_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.delete(
            face_id="face_id",
        )
        assert_matches_type(object, face, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMixpeek) -> None:
        face = await async_client.entities.faces.delete(
            face_id="face_id",
            x_namespace="X-Namespace",
        )
        assert_matches_type(object, face, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.entities.faces.with_raw_response.delete(
            face_id="face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(object, face, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixpeek) -> None:
        async with async_client.entities.faces.with_streaming_response.delete(
            face_id="face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(object, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixpeek) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            await async_client.entities.faces.with_raw_response.delete(
                face_id="",
            )
