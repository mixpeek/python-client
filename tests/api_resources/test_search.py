# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixpeek import Mixpeek, AsyncMixpeek
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_text(self, client: Mixpeek) -> None:
        search = client.search.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: Mixpeek) -> None:
        search = client.search.text(
            collection_ids=["collection1", "collection2"],
            query="query",
            filters={
                "and": [
                    {
                        "OR": [
                            {
                                "key": "personal.age",
                                "operator": "gte",
                                "value": 30,
                            },
                            {
                                "key": "work.experience",
                                "operator": "gt",
                                "value": 5,
                            },
                        ]
                    },
                    {
                        "key": "skills.programming",
                        "operator": "in",
                        "value": ["python", "mongodb"],
                    },
                    {
                        "NOR": [
                            {
                                "key": "status",
                                "value": "inactive",
                            },
                            {
                                "key": "department",
                                "value": "HR",
                            },
                        ]
                    },
                    {
                        "key": "salary",
                        "operator": "lte",
                        "value": 100000,
                    },
                    {
                        "key": "certifications",
                        "operator": "exists",
                        "value": True,
                    },
                ],
                "nor": [{}, {}, {}],
                "or": [{}, {}, {}],
            },
            group_by_file=True,
            input_type="text",
            model_id="vuse-generic-v1",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: Mixpeek) -> None:
        response = client.search.with_raw_response.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: Mixpeek) -> None:
        with client.search.with_streaming_response.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload(self, client: Mixpeek) -> None:
        search = client.search.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Mixpeek) -> None:
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
    def test_raw_response_upload(self, client: Mixpeek) -> None:
        response = client.search.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Mixpeek) -> None:
        with client.search.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_url(self, client: Mixpeek) -> None:
        search = client.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_method_url_with_all_params(self, client: Mixpeek) -> None:
        search = client.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
            filters={
                "and": [
                    {
                        "OR": [
                            {
                                "key": "personal.age",
                                "operator": "gte",
                                "value": 30,
                            },
                            {
                                "key": "work.experience",
                                "operator": "gt",
                                "value": 5,
                            },
                        ]
                    },
                    {
                        "key": "skills.programming",
                        "operator": "in",
                        "value": ["python", "mongodb"],
                    },
                    {
                        "NOR": [
                            {
                                "key": "status",
                                "value": "inactive",
                            },
                            {
                                "key": "department",
                                "value": "HR",
                            },
                        ]
                    },
                    {
                        "key": "salary",
                        "operator": "lte",
                        "value": 100000,
                    },
                    {
                        "key": "certifications",
                        "operator": "exists",
                        "value": True,
                    },
                ],
                "nor": [{}, {}, {}],
                "or": [{}, {}, {}],
            },
            group_by_file=True,
            input_type="text",
            model_id="vuse-generic-v1",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_raw_response_url(self, client: Mixpeek) -> None:
        response = client.search.with_raw_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    def test_streaming_response_url(self, client: Mixpeek) -> None:
        with client.search.with_streaming_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_text(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.search.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.search.text(
            collection_ids=["collection1", "collection2"],
            query="query",
            filters={
                "and": [
                    {
                        "OR": [
                            {
                                "key": "personal.age",
                                "operator": "gte",
                                "value": 30,
                            },
                            {
                                "key": "work.experience",
                                "operator": "gt",
                                "value": 5,
                            },
                        ]
                    },
                    {
                        "key": "skills.programming",
                        "operator": "in",
                        "value": ["python", "mongodb"],
                    },
                    {
                        "NOR": [
                            {
                                "key": "status",
                                "value": "inactive",
                            },
                            {
                                "key": "department",
                                "value": "HR",
                            },
                        ]
                    },
                    {
                        "key": "salary",
                        "operator": "lte",
                        "value": 100000,
                    },
                    {
                        "key": "certifications",
                        "operator": "exists",
                        "value": True,
                    },
                ],
                "nor": [{}, {}, {}],
                "or": [{}, {}, {}],
            },
            group_by_file=True,
            input_type="text",
            model_id="vuse-generic-v1",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.search.with_raw_response.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncMixpeek) -> None:
        async with async_client.search.with_streaming_response.text(
            collection_ids=["collection1", "collection2"],
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.search.upload(
            file=b"raw file contents",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncMixpeek) -> None:
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
    async def test_raw_response_upload(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.search.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncMixpeek) -> None:
        async with async_client.search.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_url(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_method_url_with_all_params(self, async_client: AsyncMixpeek) -> None:
        search = await async_client.search.url(
            collection_ids=["collection1", "collection2"],
            url="url",
            filters={
                "and": [
                    {
                        "OR": [
                            {
                                "key": "personal.age",
                                "operator": "gte",
                                "value": 30,
                            },
                            {
                                "key": "work.experience",
                                "operator": "gt",
                                "value": 5,
                            },
                        ]
                    },
                    {
                        "key": "skills.programming",
                        "operator": "in",
                        "value": ["python", "mongodb"],
                    },
                    {
                        "NOR": [
                            {
                                "key": "status",
                                "value": "inactive",
                            },
                            {
                                "key": "department",
                                "value": "HR",
                            },
                        ]
                    },
                    {
                        "key": "salary",
                        "operator": "lte",
                        "value": 100000,
                    },
                    {
                        "key": "certifications",
                        "operator": "exists",
                        "value": True,
                    },
                ],
                "nor": [{}, {}, {}],
                "or": [{}, {}, {}],
            },
            group_by_file=True,
            input_type="text",
            model_id="vuse-generic-v1",
            authorization="Authorization",
            index_id="index-id",
        )
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_raw_response_url(self, async_client: AsyncMixpeek) -> None:
        response = await async_client.search.with_raw_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(object, search, path=["response"])

    @parametrize
    async def test_streaming_response_url(self, async_client: AsyncMixpeek) -> None:
        async with async_client.search.with_streaming_response.url(
            collection_ids=["collection1", "collection2"],
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(object, search, path=["response"])

        assert cast(Any, response.is_closed) is True
