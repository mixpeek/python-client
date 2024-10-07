# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import embed_create_params
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
from ..types.embeddingresponse import Embeddingresponse

__all__ = ["EmbedResource", "AsyncEmbedResource"]


class EmbedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return EmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return EmbedResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: str,
        input_type: Optional[Literal["text", "base64", "url"]] | NotGiven = NOT_GIVEN,
        modality: Optional[Literal["video", "image"]] | NotGiven = NOT_GIVEN,
        model_id: Optional[object] | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Embeddingresponse:
        """
        Embed

        Args:
          input: The input data to be processed.

          input_type: The type of input data. Can be text, base64, or url.

          modality: The modality of the input data.

          model_id: The model to be used for processing.

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
            "/embed/",
            body=maybe_transform(
                {
                    "input": input,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Embeddingresponse,
        )


class AsyncEmbedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncEmbedResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: str,
        input_type: Optional[Literal["text", "base64", "url"]] | NotGiven = NOT_GIVEN,
        modality: Optional[Literal["video", "image"]] | NotGiven = NOT_GIVEN,
        model_id: Optional[object] | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Embeddingresponse:
        """
        Embed

        Args:
          input: The input data to be processed.

          input_type: The type of input data. Can be text, base64, or url.

          modality: The modality of the input data.

          model_id: The model to be used for processing.

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
            "/embed/",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "input_type": input_type,
                    "modality": modality,
                    "model_id": model_id,
                },
                embed_create_params.EmbedCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Embeddingresponse,
        )


class EmbedResourceWithRawResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_raw_response_wrapper(
            embed.create,
        )


class AsyncEmbedResourceWithRawResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_raw_response_wrapper(
            embed.create,
        )


class EmbedResourceWithStreamingResponse:
    def __init__(self, embed: EmbedResource) -> None:
        self._embed = embed

        self.create = to_streamed_response_wrapper(
            embed.create,
        )


class AsyncEmbedResourceWithStreamingResponse:
    def __init__(self, embed: AsyncEmbedResource) -> None:
        self._embed = embed

        self.create = async_to_streamed_response_wrapper(
            embed.create,
        )
