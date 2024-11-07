# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from ...types import index_text_params
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
from ...types.index_text_response import IndexTextResponse

__all__ = ["IndexResource", "AsyncIndexResource"]


class IndexResource(SyncAPIResource):
    @cached_property
    def videos(self) -> VideosResource:
        return VideosResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return IndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return IndexResourceWithStreamingResponse(self)

    def text(
        self,
        *,
        collection_id: str,
        text: str,
        asset_update: Optional[index_text_params.AssetUpdate] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        text_settings: Optional[index_text_params.TextSettings] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexTextResponse:
        """
        Index Text

        Args:
          collection_id: Unique identifier for the collection where the processed asset will be stored.

          text: The text to be processed.

          asset_update: Asset update information for existing assets

          metadata: Additional metadata associated with the file. Can include any key-value pairs
              relevant to the file.

          text_settings: Settings for text processing.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._post(
            "/index/text",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "text": text,
                    "asset_update": asset_update,
                    "metadata": metadata,
                    "text_settings": text_settings,
                },
                index_text_params.IndexTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexTextResponse,
        )


class AsyncIndexResource(AsyncAPIResource):
    @cached_property
    def videos(self) -> AsyncVideosResource:
        return AsyncVideosResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndexResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncIndexResourceWithStreamingResponse(self)

    async def text(
        self,
        *,
        collection_id: str,
        text: str,
        asset_update: Optional[index_text_params.AssetUpdate] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        text_settings: Optional[index_text_params.TextSettings] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexTextResponse:
        """
        Index Text

        Args:
          collection_id: Unique identifier for the collection where the processed asset will be stored.

          text: The text to be processed.

          asset_update: Asset update information for existing assets

          metadata: Additional metadata associated with the file. Can include any key-value pairs
              relevant to the file.

          text_settings: Settings for text processing.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._post(
            "/index/text",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "text": text,
                    "asset_update": asset_update,
                    "metadata": metadata,
                    "text_settings": text_settings,
                },
                index_text_params.IndexTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexTextResponse,
        )


class IndexResourceWithRawResponse:
    def __init__(self, index: IndexResource) -> None:
        self._index = index

        self.text = to_raw_response_wrapper(
            index.text,
        )

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._index.videos)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._index.images)


class AsyncIndexResourceWithRawResponse:
    def __init__(self, index: AsyncIndexResource) -> None:
        self._index = index

        self.text = async_to_raw_response_wrapper(
            index.text,
        )

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._index.videos)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._index.images)


class IndexResourceWithStreamingResponse:
    def __init__(self, index: IndexResource) -> None:
        self._index = index

        self.text = to_streamed_response_wrapper(
            index.text,
        )

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._index.videos)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._index.images)


class AsyncIndexResourceWithStreamingResponse:
    def __init__(self, index: AsyncIndexResource) -> None:
        self._index = index

        self.text = async_to_streamed_response_wrapper(
            index.text,
        )

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._index.videos)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._index.images)
