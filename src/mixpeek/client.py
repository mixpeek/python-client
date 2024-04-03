
import typing
import httpx
import os

from .base_client import BaseMixpeek, \
    AsyncBaseMixpeek
from .types.message import Message
from .types.model import Model
from .types.settings import Settings
from .types.generation_response import GenerationResponse
from .core.request_options import RequestOptions
from .parse_client import MixpeekParseClient, \
    AsyncMixpeekParseClient


# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class Mixpeek(BaseMixpeek): 

    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: str. The base url to use for requests from the client.

        - authorization: typing.Optional[str].

        - index_id: typing.Optional[str].

        - api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from mixpeek.client import Mixpeek

    client = Mixpeek(
        authorization="YOUR_AUTHORIZATION",
        index_id="YOUR_INDEX_ID",
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MIXPEEK_API_KEY"),
        timeout: typing.Optional[float] = None,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        super().__init__(
            base_url=base_url,
            authorization=authorization,
            index_id=index_id,
            api_key=api_key,
            timeout=timeout,
            httpx_client=httpx_client
        )
        self.parse = MixpeekParseClient(client_wrapper=self._client_wrapper)

    def generate(
        self,
        *,
        model: Model,
        # Pydantic model that represents the JSON schema of the response
        response_format: typing.Optional[typing.Any],
        context: typing.Optional[str] = OMIT,
        messages: typing.Sequence[Message],
        settings: typing.Optional[Settings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationResponse:
        if response_format is not None:
            response_format = response_format.model_json_schema()
        return self.generators.generate(
            model=model,
            response_format=response_format,
            context=context,
            messages=messages,
            settings=settings,
            request_options=request_options,
        )


class AsyncMixpeek(AsyncBaseMixpeek):

    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: str. The base url to use for requests from the client.

        - authorization: typing.Optional[str].

        - index_id: typing.Optional[str].

        - api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from mixpeek.client import AsyncMixpeek

    client = AsyncMixpeek(
        authorization="YOUR_AUTHORIZATION",
        index_id="YOUR_INDEX_ID",
        api_key="YOUR_API_KEY",
        base_url="https://yourhost.com/path/to/api",
    )
    """
    def __init__(
        self,
        *,
        base_url: str,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("MIXPEEK_API_KEY"),
        timeout: typing.Optional[float] = None,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        super().__init__(
            base_url=base_url,
            authorization=authorization,
            index_id=index_id,
            api_key=api_key,
            timeout=timeout,
            httpx_client=httpx_client
        )
        self.parse = AsyncMixpeekParseClient(
            client_wrapper=self._client_wrapper
        )

    async def generate(
        self,
        *,
        model: Model,
        # Pydantic model that represents the JSON schema of the response
        response_format: typing.Optional[typing.Any],
        context: typing.Optional[str] = OMIT,
        messages: typing.Sequence[Message],
        settings: typing.Optional[Settings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationResponse:
        if response_format is not None:
            response_format = response_format.model_json_schema()
        return await self.generators.generate(
            model=model,
            response_format=response_format,
            context=context,
            messages=messages,
            settings=settings,
            request_options=request_options,
        )