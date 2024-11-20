# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.assets import feature_list_params
from ...types.grouped_asset_data import GroupedAssetData

__all__ = ["FeaturesResource", "AsyncFeaturesResource"]


class FeaturesResource(SyncAPIResource):
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

    def list(
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
    ) -> GroupedAssetData:
        """
        Get asset details including all related features

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
            f"/assets/{asset_id}/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"return_url": return_url}, feature_list_params.FeatureListParams),
            ),
            cast_to=GroupedAssetData,
        )


class AsyncFeaturesResource(AsyncAPIResource):
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

    async def list(
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
    ) -> GroupedAssetData:
        """
        Get asset details including all related features

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
            f"/assets/{asset_id}/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"return_url": return_url}, feature_list_params.FeatureListParams),
            ),
            cast_to=GroupedAssetData,
        )


class FeaturesResourceWithRawResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.list = to_raw_response_wrapper(
            features.list,
        )


class AsyncFeaturesResourceWithRawResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.list = async_to_raw_response_wrapper(
            features.list,
        )


class FeaturesResourceWithStreamingResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.list = to_streamed_response_wrapper(
            features.list,
        )


class AsyncFeaturesResourceWithStreamingResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.list = async_to_streamed_response_wrapper(
            features.list,
        )
