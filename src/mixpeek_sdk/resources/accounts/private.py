# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...types.accounts import private_update_params
from ...types.accounts.user import User

__all__ = ["PrivateResource", "AsyncPrivateResource"]


class PrivateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrivateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return PrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return PrivateResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        api_keys: Optional[Iterable[private_update_params.APIKey]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/accounts/private/",
            body=maybe_transform(
                {
                    "api_keys": api_keys,
                    "metadata": metadata,
                },
                private_update_params.PrivateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Get User"""
        return self._get(
            "/accounts/private/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class AsyncPrivateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrivateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncPrivateResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        api_keys: Optional[Iterable[private_update_params.APIKey]] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """
        Update User

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/accounts/private/",
            body=await async_maybe_transform(
                {
                    "api_keys": api_keys,
                    "metadata": metadata,
                },
                private_update_params.PrivateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> User:
        """Get User"""
        return await self._get(
            "/accounts/private/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=User,
        )


class PrivateResourceWithRawResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.update = to_raw_response_wrapper(
            private.update,
        )
        self.list = to_raw_response_wrapper(
            private.list,
        )


class AsyncPrivateResourceWithRawResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.update = async_to_raw_response_wrapper(
            private.update,
        )
        self.list = async_to_raw_response_wrapper(
            private.list,
        )


class PrivateResourceWithStreamingResponse:
    def __init__(self, private: PrivateResource) -> None:
        self._private = private

        self.update = to_streamed_response_wrapper(
            private.update,
        )
        self.list = to_streamed_response_wrapper(
            private.list,
        )


class AsyncPrivateResourceWithStreamingResponse:
    def __init__(self, private: AsyncPrivateResource) -> None:
        self._private = private

        self.update = async_to_streamed_response_wrapper(
            private.update,
        )
        self.list = async_to_streamed_response_wrapper(
            private.list,
        )
