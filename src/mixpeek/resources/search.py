# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from ..types import search_url_params, search_text_params, search_upload_params
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

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def text(
        self,
        *,
        input: str,
        filters: object | NotGiven = NOT_GIVEN,
        group_by_file: bool | NotGiven = NOT_GIVEN,
        input_type: Optional[str] | NotGiven = NOT_GIVEN,
        modality: Optional[str] | NotGiven = NOT_GIVEN,
        model_id: Optional[str] | NotGiven = NOT_GIVEN,
        pagination: search_text_params.Pagination | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
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
        Search

        Args:
          input: url, text, or base64 input

          filters: Additional filters for the search

          group_by_file: Whether to group search results by file

          pagination: Pagination parameters

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
            "/search/text",
            body=maybe_transform(
                {
                    "input": input,
                    "filters": filters,
                    "group_by_file": group_by_file,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                    "pagination": pagination,
                    "source": source,
                },
                search_text_params.SearchTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        filters: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
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
        Search Video

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
                "filters": filters,
                "page": page,
                "page_size": page_size,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/search/upload",
            body=maybe_transform(body, search_upload_params.SearchUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def url(
        self,
        *,
        input: str,
        filters: object | NotGiven = NOT_GIVEN,
        group_by_file: bool | NotGiven = NOT_GIVEN,
        input_type: Optional[str] | NotGiven = NOT_GIVEN,
        modality: Optional[str] | NotGiven = NOT_GIVEN,
        model_id: Optional[str] | NotGiven = NOT_GIVEN,
        pagination: search_url_params.Pagination | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
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
        Search Url

        Args:
          input: url, text, or base64 input

          filters: Additional filters for the search

          group_by_file: Whether to group search results by file

          pagination: Pagination parameters

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
            "/search/url",
            body=maybe_transform(
                {
                    "input": input,
                    "filters": filters,
                    "group_by_file": group_by_file,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                    "pagination": pagination,
                    "source": source,
                },
                search_url_params.SearchURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def text(
        self,
        *,
        input: str,
        filters: object | NotGiven = NOT_GIVEN,
        group_by_file: bool | NotGiven = NOT_GIVEN,
        input_type: Optional[str] | NotGiven = NOT_GIVEN,
        modality: Optional[str] | NotGiven = NOT_GIVEN,
        model_id: Optional[str] | NotGiven = NOT_GIVEN,
        pagination: search_text_params.Pagination | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
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
        Search

        Args:
          input: url, text, or base64 input

          filters: Additional filters for the search

          group_by_file: Whether to group search results by file

          pagination: Pagination parameters

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
            "/search/text",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "filters": filters,
                    "group_by_file": group_by_file,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                    "pagination": pagination,
                    "source": source,
                },
                search_text_params.SearchTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        filters: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
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
        Search Video

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
                "filters": filters,
                "page": page,
                "page_size": page_size,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/search/upload",
            body=await async_maybe_transform(body, search_upload_params.SearchUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def url(
        self,
        *,
        input: str,
        filters: object | NotGiven = NOT_GIVEN,
        group_by_file: bool | NotGiven = NOT_GIVEN,
        input_type: Optional[str] | NotGiven = NOT_GIVEN,
        modality: Optional[str] | NotGiven = NOT_GIVEN,
        model_id: Optional[str] | NotGiven = NOT_GIVEN,
        pagination: search_url_params.Pagination | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
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
        Search Url

        Args:
          input: url, text, or base64 input

          filters: Additional filters for the search

          group_by_file: Whether to group search results by file

          pagination: Pagination parameters

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
            "/search/url",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "filters": filters,
                    "group_by_file": group_by_file,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                    "pagination": pagination,
                    "source": source,
                },
                search_url_params.SearchURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.text = to_raw_response_wrapper(
            search.text,
        )
        self.upload = to_raw_response_wrapper(
            search.upload,
        )
        self.url = to_raw_response_wrapper(
            search.url,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.text = async_to_raw_response_wrapper(
            search.text,
        )
        self.upload = async_to_raw_response_wrapper(
            search.upload,
        )
        self.url = async_to_raw_response_wrapper(
            search.url,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.text = to_streamed_response_wrapper(
            search.text,
        )
        self.upload = to_streamed_response_wrapper(
            search.upload,
        )
        self.url = to_streamed_response_wrapper(
            search.url,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.text = async_to_streamed_response_wrapper(
            search.text,
        )
        self.upload = async_to_streamed_response_wrapper(
            search.upload,
        )
        self.url = async_to_streamed_response_wrapper(
            search.url,
        )
