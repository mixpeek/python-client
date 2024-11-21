# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast

import httpx

from ...types import (
    asset_create_params,
    asset_search_params,
    asset_update_params,
    asset_retrieve_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .features import (
    FeaturesResource,
    AsyncFeaturesResource,
    FeaturesResourceWithRawResponse,
    AsyncFeaturesResourceWithRawResponse,
    FeaturesResourceWithStreamingResponse,
    AsyncFeaturesResourceWithStreamingResponse,
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
from ...types.asset_response import AssetResponse
from ...types.asset_search_response import AssetSearchResponse
from ...types.asset_update_response import AssetUpdateResponse
from ...types.shared_params.sort_option import SortOption

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def features(self) -> FeaturesResource:
        return FeaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_ids: List[str],
        page: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[asset_create_params.Filters] | NotGiven = NOT_GIVEN,
        group_by: Optional[asset_create_params.GroupBy] | NotGiven = NOT_GIVEN,
        return_url: Optional[bool] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List Assets

        Args:
          collection_ids: List of Collection IDs to search within, required

          filters: Used for filtering across all indexes

          group_by: Grouping options for search results

          return_url: Return the presigned URL for the asset and preview asset, this will introduce
              additional latency

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._post(
            "/assets",
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "group_by": group_by,
                    "return_url": return_url,
                    "select": select,
                    "sort": sort,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    asset_create_params.AssetCreateParams,
                ),
            ),
            cast_to=object,
        )

    def retrieve(
        self,
        asset_id: str,
        *,
        return_url: bool | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetResponse:
        """
        Get basic asset details

        Args:
          asset_id: Unique identifier of the asset

          return_url: Whether to generate and return presigned S3 URLs for the asset and preview. Set
              to false to improve performance when URLs aren't needed

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._get(
            f"/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"return_url": return_url}, asset_retrieve_params.AssetRetrieveParams),
            ),
            cast_to=AssetResponse,
        )

    def update(
        self,
        asset_id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        propagate_features: Optional[bool] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetUpdateResponse:
        """Partial Asset Update

        Args:
          metadata: Updated metadata for the asset.

        This can include any key-value pairs that should
              be updated or added to the asset's metadata.

          propagate_features: If True, the features will be propagated to all assets with the same asset_id

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return cast(
            AssetUpdateResponse,
            self._patch(
                f"/assets/{asset_id}",
                body=maybe_transform(
                    {
                        "metadata": metadata,
                        "propagate_features": propagate_features,
                    },
                    asset_update_params.AssetUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AssetUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        asset_id: str,
        *,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Asset

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._delete(
            f"/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def search(
        self,
        *,
        collection_ids: List[str],
        filters: Optional[asset_search_params.Filters] | NotGiven = NOT_GIVEN,
        query: Optional[asset_search_params.Query] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetSearchResponse:
        """
        Search Assets

        Args:
          collection_ids: List of Collection IDs to search within, required

          filters: Complex nested query filters

          query: Structured query object specifying which fields to search in and what to search
              for

          select: List of fields to return in results

          sort: List of fields to sort by

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._post(
            "/assets/search",
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "query": query,
                    "select": select,
                    "sort": sort,
                },
                asset_search_params.AssetSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetSearchResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def features(self) -> AsyncFeaturesResource:
        return AsyncFeaturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_ids: List[str],
        page: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[asset_create_params.Filters] | NotGiven = NOT_GIVEN,
        group_by: Optional[asset_create_params.GroupBy] | NotGiven = NOT_GIVEN,
        return_url: Optional[bool] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        List Assets

        Args:
          collection_ids: List of Collection IDs to search within, required

          filters: Used for filtering across all indexes

          group_by: Grouping options for search results

          return_url: Return the presigned URL for the asset and preview asset, this will introduce
              additional latency

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._post(
            "/assets",
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "group_by": group_by,
                    "return_url": return_url,
                    "select": select,
                    "sort": sort,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    asset_create_params.AssetCreateParams,
                ),
            ),
            cast_to=object,
        )

    async def retrieve(
        self,
        asset_id: str,
        *,
        return_url: bool | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetResponse:
        """
        Get basic asset details

        Args:
          asset_id: Unique identifier of the asset

          return_url: Whether to generate and return presigned S3 URLs for the asset and preview. Set
              to false to improve performance when URLs aren't needed

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._get(
            f"/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_url": return_url}, asset_retrieve_params.AssetRetrieveParams
                ),
            ),
            cast_to=AssetResponse,
        )

    async def update(
        self,
        asset_id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        propagate_features: Optional[bool] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetUpdateResponse:
        """Partial Asset Update

        Args:
          metadata: Updated metadata for the asset.

        This can include any key-value pairs that should
              be updated or added to the asset's metadata.

          propagate_features: If True, the features will be propagated to all assets with the same asset_id

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return cast(
            AssetUpdateResponse,
            await self._patch(
                f"/assets/{asset_id}",
                body=await async_maybe_transform(
                    {
                        "metadata": metadata,
                        "propagate_features": propagate_features,
                    },
                    asset_update_params.AssetUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AssetUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        asset_id: str,
        *,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Asset

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._delete(
            f"/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def search(
        self,
        *,
        collection_ids: List[str],
        filters: Optional[asset_search_params.Filters] | NotGiven = NOT_GIVEN,
        query: Optional[asset_search_params.Query] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetSearchResponse:
        """
        Search Assets

        Args:
          collection_ids: List of Collection IDs to search within, required

          filters: Complex nested query filters

          query: Structured query object specifying which fields to search in and what to search
              for

          select: List of fields to return in results

          sort: List of fields to sort by

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._post(
            "/assets/search",
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "query": query,
                    "select": select,
                    "sort": sort,
                },
                asset_search_params.AssetSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetSearchResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )
        self.search = to_raw_response_wrapper(
            assets.search,
        )

    @cached_property
    def features(self) -> FeaturesResourceWithRawResponse:
        return FeaturesResourceWithRawResponse(self._assets.features)


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )
        self.search = async_to_raw_response_wrapper(
            assets.search,
        )

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithRawResponse:
        return AsyncFeaturesResourceWithRawResponse(self._assets.features)


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )
        self.search = to_streamed_response_wrapper(
            assets.search,
        )

    @cached_property
    def features(self) -> FeaturesResourceWithStreamingResponse:
        return FeaturesResourceWithStreamingResponse(self._assets.features)


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            assets.search,
        )

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithStreamingResponse:
        return AsyncFeaturesResourceWithStreamingResponse(self._assets.features)
