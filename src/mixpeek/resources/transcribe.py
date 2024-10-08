# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import transcribe_url_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["TranscribeResource", "AsyncTranscribeResource"]


class TranscribeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return TranscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return TranscribeResourceWithStreamingResponse(self)

    def url(
        self,
        *,
        url: str,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Transcribe By Url

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Authorization": authorization,
                    "index-id": index_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/transcribe/url",
            body=maybe_transform({"url": url}, transcribe_url_params.TranscribeURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTranscribeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncTranscribeResourceWithStreamingResponse(self)

    async def url(
        self,
        *,
        url: str,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Transcribe By Url

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Authorization": authorization,
                    "index-id": index_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/transcribe/url",
            body=await async_maybe_transform({"url": url}, transcribe_url_params.TranscribeURLParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TranscribeResourceWithRawResponse:
    def __init__(self, transcribe: TranscribeResource) -> None:
        self._transcribe = transcribe

        self.url = to_raw_response_wrapper(
            transcribe.url,
        )


class AsyncTranscribeResourceWithRawResponse:
    def __init__(self, transcribe: AsyncTranscribeResource) -> None:
        self._transcribe = transcribe

        self.url = async_to_raw_response_wrapper(
            transcribe.url,
        )


class TranscribeResourceWithStreamingResponse:
    def __init__(self, transcribe: TranscribeResource) -> None:
        self._transcribe = transcribe

        self.url = to_streamed_response_wrapper(
            transcribe.url,
        )


class AsyncTranscribeResourceWithStreamingResponse:
    def __init__(self, transcribe: AsyncTranscribeResource) -> None:
        self._transcribe = transcribe

        self.url = async_to_streamed_response_wrapper(
            transcribe.url,
        )
