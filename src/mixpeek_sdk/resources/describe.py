# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import describe_url_params, describe_upload_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    strip_not_given,
    deepcopy_minimal,
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

__all__ = ["DescribeResource", "AsyncDescribeResource"]


class DescribeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DescribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return DescribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DescribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return DescribeResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        file: FileTypes,
        prompt: str,
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
        Endpoint to describe an uploaded video based on a given description.

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
        body = deepcopy_minimal(
            {
                "file": file,
                "prompt": prompt,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/describe/upload",
            body=maybe_transform(body, describe_upload_params.DescribeUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def url(
        self,
        *,
        prompt: str,
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
        Endpoint to describe a video from a URL based on a given description.

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
            "/describe/url",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                },
                describe_url_params.DescribeURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDescribeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDescribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncDescribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDescribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncDescribeResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        file: FileTypes,
        prompt: str,
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
        Endpoint to describe an uploaded video based on a given description.

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
        body = deepcopy_minimal(
            {
                "file": file,
                "prompt": prompt,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/describe/upload",
            body=await async_maybe_transform(body, describe_upload_params.DescribeUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def url(
        self,
        *,
        prompt: str,
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
        Endpoint to describe a video from a URL based on a given description.

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
            "/describe/url",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "url": url,
                },
                describe_url_params.DescribeURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DescribeResourceWithRawResponse:
    def __init__(self, describe: DescribeResource) -> None:
        self._describe = describe

        self.upload = to_raw_response_wrapper(
            describe.upload,
        )
        self.url = to_raw_response_wrapper(
            describe.url,
        )


class AsyncDescribeResourceWithRawResponse:
    def __init__(self, describe: AsyncDescribeResource) -> None:
        self._describe = describe

        self.upload = async_to_raw_response_wrapper(
            describe.upload,
        )
        self.url = async_to_raw_response_wrapper(
            describe.url,
        )


class DescribeResourceWithStreamingResponse:
    def __init__(self, describe: DescribeResource) -> None:
        self._describe = describe

        self.upload = to_streamed_response_wrapper(
            describe.upload,
        )
        self.url = to_streamed_response_wrapper(
            describe.url,
        )


class AsyncDescribeResourceWithStreamingResponse:
    def __init__(self, describe: AsyncDescribeResource) -> None:
        self._describe = describe

        self.upload = async_to_streamed_response_wrapper(
            describe.upload,
        )
        self.url = async_to_streamed_response_wrapper(
            describe.url,
        )
