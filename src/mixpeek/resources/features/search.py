# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    strip_not_given,
    deepcopy_minimal,
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
from ...types.features import search_url_params, search_file_params, search_text_params, search_feedback_params
from ...types.shared_params.sort_option import SortOption
from ...types.shared_params.logical_operator import LogicalOperator

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

    def feedback(
        self,
        *,
        feature_id: str,
        is_relevant: bool,
        search_id: str,
        feedback_text: Optional[str] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Submit feedback for search results to improve future searches

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._post(
            "/features/search/feedback",
            body=maybe_transform(
                {
                    "feature_id": feature_id,
                    "is_relevant": is_relevant,
                    "search_id": search_id,
                    "feedback_text": feedback_text,
                },
                search_feedback_params.SearchFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def file(
        self,
        *,
        file: FileTypes,
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By File

        Args:
          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "file": file,
                "filters": filters,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/features/search/file",
            body=maybe_transform(body, search_file_params.SearchFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_file_params.SearchFileParams,
                ),
            ),
            cast_to=object,
        )

    def text(
        self,
        *,
        collection_ids: List[str],
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        group_by: Optional[search_text_params.GroupBy] | NotGiven = NOT_GIVEN,
        model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]] | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        search_type: Literal["semantic", "fulltext"] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By Text

        Args:
          collection_ids: List of Collection IDs to search within, required

          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          filters: Complex nested query filters

          group_by: Grouping options for search results

          model_id: Embedding model to use

          query: Text query for the search

          search_type: Type of search to perform

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._post(
            "/features/search/text",
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "group_by": group_by,
                    "model_id": model_id,
                    "query": query,
                    "search_type": search_type,
                    "select": select,
                    "sort": sort,
                },
                search_text_params.SearchTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_text_params.SearchTextParams,
                ),
            ),
            cast_to=object,
        )

    def url(
        self,
        *,
        collection_ids: List[str],
        url: str,
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        group_by: Optional[search_url_params.GroupBy] | NotGiven = NOT_GIVEN,
        model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]] | NotGiven = NOT_GIVEN,
        search_type: Literal["semantic", "fulltext"] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By Url

        Args:
          collection_ids: List of Collection IDs to search within, required

          url: Url to fetch and search

          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          filters: Complex nested query filters

          group_by: Grouping options for search results

          model_id: Embedding model to use

          search_type: Type of search to perform

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._post(
            "/features/search/url",
            body=maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "url": url,
                    "filters": filters,
                    "group_by": group_by,
                    "model_id": model_id,
                    "search_type": search_type,
                    "select": select,
                    "sort": sort,
                },
                search_url_params.SearchURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_url_params.SearchURLParams,
                ),
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

    async def feedback(
        self,
        *,
        feature_id: str,
        is_relevant: bool,
        search_id: str,
        feedback_text: Optional[str] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Submit feedback for search results to improve future searches

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._post(
            "/features/search/feedback",
            body=await async_maybe_transform(
                {
                    "feature_id": feature_id,
                    "is_relevant": is_relevant,
                    "search_id": search_id,
                    "feedback_text": feedback_text,
                },
                search_feedback_params.SearchFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def file(
        self,
        *,
        file: FileTypes,
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By File

        Args:
          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "file": file,
                "filters": filters,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/features/search/file",
            body=await async_maybe_transform(body, search_file_params.SearchFileParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_file_params.SearchFileParams,
                ),
            ),
            cast_to=object,
        )

    async def text(
        self,
        *,
        collection_ids: List[str],
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        group_by: Optional[search_text_params.GroupBy] | NotGiven = NOT_GIVEN,
        model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]] | NotGiven = NOT_GIVEN,
        query: Optional[str] | NotGiven = NOT_GIVEN,
        search_type: Literal["semantic", "fulltext"] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By Text

        Args:
          collection_ids: List of Collection IDs to search within, required

          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          filters: Complex nested query filters

          group_by: Grouping options for search results

          model_id: Embedding model to use

          query: Text query for the search

          search_type: Type of search to perform

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._post(
            "/features/search/text",
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "filters": filters,
                    "group_by": group_by,
                    "model_id": model_id,
                    "query": query,
                    "search_type": search_type,
                    "select": select,
                    "sort": sort,
                },
                search_text_params.SearchTextParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_text_params.SearchTextParams,
                ),
            ),
            cast_to=object,
        )

    async def url(
        self,
        *,
        collection_ids: List[str],
        url: str,
        offset_position: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filters: Optional[LogicalOperator] | NotGiven = NOT_GIVEN,
        group_by: Optional[search_url_params.GroupBy] | NotGiven = NOT_GIVEN,
        model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]] | NotGiven = NOT_GIVEN,
        search_type: Literal["semantic", "fulltext"] | NotGiven = NOT_GIVEN,
        select: Optional[List[str]] | NotGiven = NOT_GIVEN,
        sort: Optional[SortOption] | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Search Features By Url

        Args:
          collection_ids: List of Collection IDs to search within, required

          url: Url to fetch and search

          offset_position: The position to start returning results from. Used for pagination. Does not work
              with group_by

          page_size: Number of results to return per page.

          filters: Complex nested query filters

          group_by: Grouping options for search results

          model_id: Embedding model to use

          search_type: Type of search to perform

          select: List of fields to return in results, supports dot notation. If None, all fields
              are returned.

          sort: List of fields to sort by, with direction (asc or desc). Supports dot notation
              for nested fields.

          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._post(
            "/features/search/url",
            body=await async_maybe_transform(
                {
                    "collection_ids": collection_ids,
                    "url": url,
                    "filters": filters,
                    "group_by": group_by,
                    "model_id": model_id,
                    "search_type": search_type,
                    "select": select,
                    "sort": sort,
                },
                search_url_params.SearchURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "offset_position": offset_position,
                        "page_size": page_size,
                    },
                    search_url_params.SearchURLParams,
                ),
            ),
            cast_to=object,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.feedback = to_raw_response_wrapper(
            search.feedback,
        )
        self.file = to_raw_response_wrapper(
            search.file,
        )
        self.text = to_raw_response_wrapper(
            search.text,
        )
        self.url = to_raw_response_wrapper(
            search.url,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.feedback = async_to_raw_response_wrapper(
            search.feedback,
        )
        self.file = async_to_raw_response_wrapper(
            search.file,
        )
        self.text = async_to_raw_response_wrapper(
            search.text,
        )
        self.url = async_to_raw_response_wrapper(
            search.url,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.feedback = to_streamed_response_wrapper(
            search.feedback,
        )
        self.file = to_streamed_response_wrapper(
            search.file,
        )
        self.text = to_streamed_response_wrapper(
            search.text,
        )
        self.url = to_streamed_response_wrapper(
            search.url,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.feedback = async_to_streamed_response_wrapper(
            search.feedback,
        )
        self.file = async_to_streamed_response_wrapper(
            search.file,
        )
        self.text = async_to_streamed_response_wrapper(
            search.text,
        )
        self.url = async_to_streamed_response_wrapper(
            search.url,
        )
