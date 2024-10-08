# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "MixpeekSDK",
    "AsyncMixpeekSDK",
    "Client",
    "AsyncClient",
]


class MixpeekSDK(SyncAPIClient):
    accounts: resources.AccountsResource
    describe: resources.DescribeResource
    embed: resources.EmbedResource
    transcribe: resources.TranscribeResource
    read: resources.ReadResource
    recognize: resources.RecognizeResource
    agent: resources.AgentResource
    indexes: resources.IndexesResource
    search: resources.SearchResource
    collections: resources.CollectionsResource
    tasks: resources.TasksResource
    with_raw_response: MixpeekSDKWithRawResponse
    with_streaming_response: MixpeekSDKWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous mixpeek-sdk client instance."""
        if base_url is None:
            base_url = os.environ.get("MIXPEEK_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.mixpeek.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AccountsResource(self)
        self.describe = resources.DescribeResource(self)
        self.embed = resources.EmbedResource(self)
        self.transcribe = resources.TranscribeResource(self)
        self.read = resources.ReadResource(self)
        self.recognize = resources.RecognizeResource(self)
        self.agent = resources.AgentResource(self)
        self.indexes = resources.IndexesResource(self)
        self.search = resources.SearchResource(self)
        self.collections = resources.CollectionsResource(self)
        self.tasks = resources.TasksResource(self)
        self.with_raw_response = MixpeekSDKWithRawResponse(self)
        self.with_streaming_response = MixpeekSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMixpeekSDK(AsyncAPIClient):
    accounts: resources.AsyncAccountsResource
    describe: resources.AsyncDescribeResource
    embed: resources.AsyncEmbedResource
    transcribe: resources.AsyncTranscribeResource
    read: resources.AsyncReadResource
    recognize: resources.AsyncRecognizeResource
    agent: resources.AsyncAgentResource
    indexes: resources.AsyncIndexesResource
    search: resources.AsyncSearchResource
    collections: resources.AsyncCollectionsResource
    tasks: resources.AsyncTasksResource
    with_raw_response: AsyncMixpeekSDKWithRawResponse
    with_streaming_response: AsyncMixpeekSDKWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async mixpeek-sdk client instance."""
        if base_url is None:
            base_url = os.environ.get("MIXPEEK_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.mixpeek.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = resources.AsyncAccountsResource(self)
        self.describe = resources.AsyncDescribeResource(self)
        self.embed = resources.AsyncEmbedResource(self)
        self.transcribe = resources.AsyncTranscribeResource(self)
        self.read = resources.AsyncReadResource(self)
        self.recognize = resources.AsyncRecognizeResource(self)
        self.agent = resources.AsyncAgentResource(self)
        self.indexes = resources.AsyncIndexesResource(self)
        self.search = resources.AsyncSearchResource(self)
        self.collections = resources.AsyncCollectionsResource(self)
        self.tasks = resources.AsyncTasksResource(self)
        self.with_raw_response = AsyncMixpeekSDKWithRawResponse(self)
        self.with_streaming_response = AsyncMixpeekSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MixpeekSDKWithRawResponse:
    def __init__(self, client: MixpeekSDK) -> None:
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.describe = resources.DescribeResourceWithRawResponse(client.describe)
        self.embed = resources.EmbedResourceWithRawResponse(client.embed)
        self.transcribe = resources.TranscribeResourceWithRawResponse(client.transcribe)
        self.read = resources.ReadResourceWithRawResponse(client.read)
        self.recognize = resources.RecognizeResourceWithRawResponse(client.recognize)
        self.agent = resources.AgentResourceWithRawResponse(client.agent)
        self.indexes = resources.IndexesResourceWithRawResponse(client.indexes)
        self.search = resources.SearchResourceWithRawResponse(client.search)
        self.collections = resources.CollectionsResourceWithRawResponse(client.collections)
        self.tasks = resources.TasksResourceWithRawResponse(client.tasks)


class AsyncMixpeekSDKWithRawResponse:
    def __init__(self, client: AsyncMixpeekSDK) -> None:
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.describe = resources.AsyncDescribeResourceWithRawResponse(client.describe)
        self.embed = resources.AsyncEmbedResourceWithRawResponse(client.embed)
        self.transcribe = resources.AsyncTranscribeResourceWithRawResponse(client.transcribe)
        self.read = resources.AsyncReadResourceWithRawResponse(client.read)
        self.recognize = resources.AsyncRecognizeResourceWithRawResponse(client.recognize)
        self.agent = resources.AsyncAgentResourceWithRawResponse(client.agent)
        self.indexes = resources.AsyncIndexesResourceWithRawResponse(client.indexes)
        self.search = resources.AsyncSearchResourceWithRawResponse(client.search)
        self.collections = resources.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.tasks = resources.AsyncTasksResourceWithRawResponse(client.tasks)


class MixpeekSDKWithStreamedResponse:
    def __init__(self, client: MixpeekSDK) -> None:
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.describe = resources.DescribeResourceWithStreamingResponse(client.describe)
        self.embed = resources.EmbedResourceWithStreamingResponse(client.embed)
        self.transcribe = resources.TranscribeResourceWithStreamingResponse(client.transcribe)
        self.read = resources.ReadResourceWithStreamingResponse(client.read)
        self.recognize = resources.RecognizeResourceWithStreamingResponse(client.recognize)
        self.agent = resources.AgentResourceWithStreamingResponse(client.agent)
        self.indexes = resources.IndexesResourceWithStreamingResponse(client.indexes)
        self.search = resources.SearchResourceWithStreamingResponse(client.search)
        self.collections = resources.CollectionsResourceWithStreamingResponse(client.collections)
        self.tasks = resources.TasksResourceWithStreamingResponse(client.tasks)


class AsyncMixpeekSDKWithStreamedResponse:
    def __init__(self, client: AsyncMixpeekSDK) -> None:
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.describe = resources.AsyncDescribeResourceWithStreamingResponse(client.describe)
        self.embed = resources.AsyncEmbedResourceWithStreamingResponse(client.embed)
        self.transcribe = resources.AsyncTranscribeResourceWithStreamingResponse(client.transcribe)
        self.read = resources.AsyncReadResourceWithStreamingResponse(client.read)
        self.recognize = resources.AsyncRecognizeResourceWithStreamingResponse(client.recognize)
        self.agent = resources.AsyncAgentResourceWithStreamingResponse(client.agent)
        self.indexes = resources.AsyncIndexesResourceWithStreamingResponse(client.indexes)
        self.search = resources.AsyncSearchResourceWithStreamingResponse(client.search)
        self.collections = resources.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.tasks = resources.AsyncTasksResourceWithStreamingResponse(client.tasks)


Client = MixpeekSDK

AsyncClient = AsyncMixpeekSDK
