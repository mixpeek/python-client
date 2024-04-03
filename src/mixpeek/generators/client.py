# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error_response import ErrorResponse
from ..types.generation_response import GenerationResponse
from ..types.http_validation_error import HttpValidationError
from ..types.message import Message
from ..types.model import Model
from ..types.settings import Settings

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GeneratorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate(
        self,
        *,
        model: Model,
        response_format: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[str] = OMIT,
        messages: typing.Sequence[Message],
        settings: typing.Optional[Settings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationResponse:
        """
        Parameters:
            - model: Model.

            - response_format: typing.Optional[typing.Dict[str, typing.Any]].

            - context: typing.Optional[str].

            - messages: typing.Sequence[Message].

            - settings: typing.Optional[Settings].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import Message, Model
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        client.generators.generate(
            model=Model(
                provider="provider",
                model="gpt-3.5-turbo",
            ),
            messages=[
                Message(
                    role="role",
                    content="content",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "messages": messages}
        if response_format is not OMIT:
            _request["response_format"] = response_format
        if context is not OMIT:
            _request["context"] = context
        if settings is not OMIT:
            _request["settings"] = settings
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "generate"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GenerationResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGeneratorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate(
        self,
        *,
        model: Model,
        response_format: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[str] = OMIT,
        messages: typing.Sequence[Message],
        settings: typing.Optional[Settings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GenerationResponse:
        """
        Parameters:
            - model: Model.

            - response_format: typing.Optional[typing.Dict[str, typing.Any]].

            - context: typing.Optional[str].

            - messages: typing.Sequence[Message].

            - settings: typing.Optional[Settings].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import Message, Model
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        await client.generators.generate(
            model=Model(
                provider="provider",
                model="gpt-3.5-turbo",
            ),
            messages=[
                Message(
                    role="role",
                    content="content",
                )
            ],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"model": model, "messages": messages}
        if response_format is not OMIT:
            _request["response_format"] = response_format
        if context is not OMIT:
            _request["context"] = context
        if settings is not OMIT:
            _request["settings"] = settings
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "generate"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GenerationResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
