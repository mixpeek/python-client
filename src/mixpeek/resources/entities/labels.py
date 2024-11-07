# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.entities import label_list_params, label_update_params
from ...types.entities.label_response import LabelResponse
from ...types.entities.label_list_response import LabelListResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        path_label_id: str,
        body_label_id: str,
        metadata: Optional[object],
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelResponse:
        """
        Update an existing label's metadata

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_label_id:
            raise ValueError(f"Expected a non-empty value for `path_label_id` but received {path_label_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._patch(
            f"/entities/labels/{path_label_id}",
            body=maybe_transform(
                {
                    "label_id": body_label_id,
                    "metadata": metadata,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelListResponse:
        """
        List all registered labels

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._get(
            "/entities/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    def delete(
        self,
        label_id: str,
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
        Delete a specific label

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return self._delete(
            f"/entities/labels/{label_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        path_label_id: str,
        body_label_id: str,
        metadata: Optional[object],
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelResponse:
        """
        Update an existing label's metadata

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_label_id:
            raise ValueError(f"Expected a non-empty value for `path_label_id` but received {path_label_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._patch(
            f"/entities/labels/{path_label_id}",
            body=await async_maybe_transform(
                {
                    "label_id": body_label_id,
                    "metadata": metadata,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelResponse,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelListResponse:
        """
        List all registered labels

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._get(
            "/entities/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    async def delete(
        self,
        label_id: str,
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
        Delete a specific label

        Args:
          index_id: filter by organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not label_id:
            raise ValueError(f"Expected a non-empty value for `label_id` but received {label_id!r}")
        extra_headers = {**strip_not_given({"index-id": index_id}), **(extra_headers or {})}
        return await self._delete(
            f"/entities/labels/{label_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.update = to_raw_response_wrapper(
            labels.update,
        )
        self.list = to_raw_response_wrapper(
            labels.list,
        )
        self.delete = to_raw_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.update = async_to_raw_response_wrapper(
            labels.update,
        )
        self.list = async_to_raw_response_wrapper(
            labels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            labels.delete,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.update = to_streamed_response_wrapper(
            labels.update,
        )
        self.list = to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = to_streamed_response_wrapper(
            labels.delete,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.update = async_to_streamed_response_wrapper(
            labels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            labels.delete,
        )
