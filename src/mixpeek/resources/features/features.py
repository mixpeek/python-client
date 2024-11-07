# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from ...types import feature_list_params, feature_update_params, feature_retrieve_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.feature import Feature
from ...types.feature_list_response import FeatureListResponse
from ...types.shared_params.sort_option import SortOption
from ...types.shared_params.logical_operator import LogicalOperator

__all__ = ["FeaturesResource", "AsyncFeaturesResource"]


class FeaturesResource(SyncAPIResource):
    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> FeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return FeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return FeaturesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        feature_id: str,
        *,
        include_vectors: Optional[bool] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Feature:
        """
        Get Feature

        Args:
          include_vectors: When true, includes the feature's vector embeddings in the response

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._get(
            f"/features/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_vectors": include_vectors}, feature_retrieve_params.FeatureRetrieveParams
                ),
            ),
            cast_to=Feature,
        )

    def update(
        self,
        feature_id: str,
        *,
        metadata: object,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Feature:
        """
        Full Feature Update

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._put(
            f"/features/{feature_id}",
            body=maybe_transform({"metadata": metadata}, feature_update_params.FeatureUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def list(
        self,
        *,
        collection_ids: List[str],
        offset_feature_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        select: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureListResponse:
        """
        Retrieves a list of features based on the provided filters and sorting criteria.
        If you provide a sort, then pagination isn't supported.

        Args:
          collection_ids: Collection IDs to filter features

          offset_feature_id: The offset id to start returning results from. Used for pagination

          filters: Complex nested query filters

          select: List of fields to return in results, supports dot notation.

          sort: List of fields to sort by, with direction (asc or desc).
                      NOTE: fields will require a specialty index to use this, consult with the team.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._post(
            "/features",
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "select": select,
                    "sort": sort,
                },
                feature_list_params.FeatureListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset_feature_id": offset_feature_id,
                        "page_size": page_size,
                    },
                    feature_list_params.FeatureListParams,
                ),
            ),
            cast_to=FeatureListResponse,
        )

    def delete(
        self,
        feature_id: str,
        *,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Feature

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._delete(
            f"/features/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFeaturesResource(AsyncAPIResource):
    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncFeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncFeaturesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        feature_id: str,
        *,
        include_vectors: Optional[bool] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Feature:
        """
        Get Feature

        Args:
          include_vectors: When true, includes the feature's vector embeddings in the response

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._get(
            f"/features/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_vectors": include_vectors}, feature_retrieve_params.FeatureRetrieveParams
                ),
            ),
            cast_to=Feature,
        )

    async def update(
        self,
        feature_id: str,
        *,
        metadata: object,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Feature:
        """
        Full Feature Update

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._put(
            f"/features/{feature_id}",
            body=await async_maybe_transform({"metadata": metadata}, feature_update_params.FeatureUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    async def list(
        self,
        *,
        collection_ids: List[str],
        offset_feature_id: Optional[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        select: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeatureListResponse:
        """
        Retrieves a list of features based on the provided filters and sorting criteria.
        If you provide a sort, then pagination isn't supported.

        Args:
          collection_ids: Collection IDs to filter features

          offset_feature_id: The offset id to start returning results from. Used for pagination

          filters: Complex nested query filters

          select: List of fields to return in results, supports dot notation.

          sort: List of fields to sort by, with direction (asc or desc).
                      NOTE: fields will require a specialty index to use this, consult with the team.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._post(
            "/features",
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "select": select,
                    "sort": sort,
                },
                feature_list_params.FeatureListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset_feature_id": offset_feature_id,
                        "page_size": page_size,
                    },
                    feature_list_params.FeatureListParams,
                ),
            ),
            cast_to=FeatureListResponse,
        )

    async def delete(
        self,
        feature_id: str,
        *,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Feature

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._delete(
            f"/features/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FeaturesResourceWithRawResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.retrieve = to_raw_response_wrapper(
            features.retrieve,
        )
        self.update = to_raw_response_wrapper(
            features.update,
        )
        self.list = to_raw_response_wrapper(
            features.list,
        )
        self.delete = to_raw_response_wrapper(
            features.delete,
        )

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._features.search)


class AsyncFeaturesResourceWithRawResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.retrieve = async_to_raw_response_wrapper(
            features.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            features.update,
        )
        self.list = async_to_raw_response_wrapper(
            features.list,
        )
        self.delete = async_to_raw_response_wrapper(
            features.delete,
        )

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._features.search)


class FeaturesResourceWithStreamingResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.retrieve = to_streamed_response_wrapper(
            features.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            features.update,
        )
        self.list = to_streamed_response_wrapper(
            features.list,
        )
        self.delete = to_streamed_response_wrapper(
            features.delete,
        )

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._features.search)


class AsyncFeaturesResourceWithStreamingResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.retrieve = async_to_streamed_response_wrapper(
            features.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            features.update,
        )
        self.list = async_to_streamed_response_wrapper(
            features.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            features.delete,
        )

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._features.search)
