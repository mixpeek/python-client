
import typing
import httpx

from .base_client import BaseMixpeek, \
    AsyncBaseMixpeek
from .types.message import Message
from .types.model import Model
from .types.settings import Settings
from .types.generation_response import GenerationResponse
from .core.request_options import RequestOptions


# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class Mixpeek(BaseMixpeek): 

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