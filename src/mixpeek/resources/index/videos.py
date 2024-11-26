# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.index import video_url_params
from ..._base_client import make_request_options
from ...types.index.video_url_response import VideoURLResponse

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)

    def url(
        self,
        *,
        collection_id: str,
        url: str,
        asset_update: Optional[video_url_params.AssetUpdate] | NotGiven = NOT_GIVEN,
        feature_extractors: Optional[Iterable[video_url_params.FeatureExtractor]] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoURLResponse:
        """
        Index Video Url

        Args:
          collection_id: Unique identifier for the collection where the processed asset will be stored.

          url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.

          asset_update: Asset update information for existing assets

          feature_extractors: Settings for video processing. Only applicable if the URL points to a video
              file.

          metadata: Additional metadata associated with the asset. Can include any key-value pairs
              relevant to the asset.

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._post(
            "/index/videos/url",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "url": url,
                    "asset_update": asset_update,
                    "feature_extractors": feature_extractors,
                    "metadata": metadata,
                },
                video_url_params.VideoURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoURLResponse,
        )


class AsyncVideosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)

    async def url(
        self,
        *,
        collection_id: str,
        url: str,
        asset_update: Optional[video_url_params.AssetUpdate] | NotGiven = NOT_GIVEN,
        feature_extractors: Optional[Iterable[video_url_params.FeatureExtractor]] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VideoURLResponse:
        """
        Index Video Url

        Args:
          collection_id: Unique identifier for the collection where the processed asset will be stored.

          url: The URL of the asset to be processed. Must be a valid HTTP or HTTPS URL.

          asset_update: Asset update information for existing assets

          feature_extractors: Settings for video processing. Only applicable if the URL points to a video
              file.

          metadata: Additional metadata associated with the asset. Can include any key-value pairs
              relevant to the asset.

          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._post(
            "/index/videos/url",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "url": url,
                    "asset_update": asset_update,
                    "feature_extractors": feature_extractors,
                    "metadata": metadata,
                },
                video_url_params.VideoURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VideoURLResponse,
        )


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.url = to_raw_response_wrapper(
            videos.url,
        )


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.url = async_to_raw_response_wrapper(
            videos.url,
        )


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

        self.url = to_streamed_response_wrapper(
            videos.url,
        )


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

        self.url = async_to_streamed_response_wrapper(
            videos.url,
        )