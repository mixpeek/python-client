# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .task import (
    TaskResource,
    AsyncTaskResource,
    TaskResourceWithRawResponse,
    AsyncTaskResourceWithRawResponse,
    TaskResourceWithStreamingResponse,
    AsyncTaskResourceWithStreamingResponse,
)
from ...types import agent_create_params
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
from ...types.agentresponse import Agentresponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def task(self) -> TaskResource:
        return TaskResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agentresponse:
        """
        Start Agent

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
            "/agent/",
            body=maybe_transform({"prompt": prompt}, agent_create_params.AgentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agentresponse,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def task(self) -> AsyncTaskResource:
        return AsyncTaskResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agentresponse:
        """
        Start Agent

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
            "/agent/",
            body=await async_maybe_transform({"prompt": prompt}, agent_create_params.AgentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agentresponse,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_raw_response_wrapper(
            agent.create,
        )

    @cached_property
    def task(self) -> TaskResourceWithRawResponse:
        return TaskResourceWithRawResponse(self._agent.task)


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_raw_response_wrapper(
            agent.create,
        )

    @cached_property
    def task(self) -> AsyncTaskResourceWithRawResponse:
        return AsyncTaskResourceWithRawResponse(self._agent.task)


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_streamed_response_wrapper(
            agent.create,
        )

    @cached_property
    def task(self) -> TaskResourceWithStreamingResponse:
        return TaskResourceWithStreamingResponse(self._agent.task)


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_streamed_response_wrapper(
            agent.create,
        )

    @cached_property
    def task(self) -> AsyncTaskResourceWithStreamingResponse:
        return AsyncTaskResourceWithStreamingResponse(self._agent.task)
