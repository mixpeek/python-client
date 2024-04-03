# This file was auto-generated by Fern from our API Definition.

import datetime as dt
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
from ..types.http_validation_error import HttpValidationError
from ..types.workflow_response import WorkflowResponse
from ..types.workflow_settings import WorkflowSettings

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        code_as_string: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings: WorkflowSettings,
        workflow_name: typing.Optional[str] = OMIT,
        last_run: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowResponse:
        """
        Parameters:
            - workflow_id: typing.Optional[str].

            - code_as_string: str.

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - settings: WorkflowSettings.

            - workflow_name: typing.Optional[str].

            - last_run: typing.Optional[dt.datetime].

            - created_at: typing.Optional[dt.datetime].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import WorkflowSettings
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        client.workflows.create(
            code_as_string="code_as_string",
            settings=WorkflowSettings(),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"code_as_string": code_as_string, "settings": settings}
        if workflow_id is not OMIT:
            _request["workflow_id"] = workflow_id
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if workflow_name is not OMIT:
            _request["workflow_name"] = workflow_name
        if last_run is not OMIT:
            _request["last_run"] = last_run
        if created_at is not OMIT:
            _request["created_at"] = created_at
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workflows"),
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
            return pydantic.parse_obj_as(WorkflowResponse, _response.json())  # type: ignore
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

    def invoke(
        self,
        workflow_id: str,
        *,
        websocket_id: typing.Optional[str] = None,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - workflow_id: str.

            - websocket_id: typing.Optional[str].

            - request: typing.Dict[str, typing.Any].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        client.workflows.invoke(
            workflow_id="workflow_id",
            request={},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"workflows/{jsonable_encoder(workflow_id)}/invoke"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "websocket_id": websocket_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
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

    def convert_code_to_string(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowResponse:
        """
        Parameters:
            - request: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        client.workflows.convert_code_to_string(
            request="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workflows/code"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request),
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
            return pydantic.parse_obj_as(WorkflowResponse, _response.json())  # type: ignore
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


class AsyncWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        workflow_id: typing.Optional[str] = OMIT,
        code_as_string: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        settings: WorkflowSettings,
        workflow_name: typing.Optional[str] = OMIT,
        last_run: typing.Optional[dt.datetime] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WorkflowResponse:
        """
        Parameters:
            - workflow_id: typing.Optional[str].

            - code_as_string: str.

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - settings: WorkflowSettings.

            - workflow_name: typing.Optional[str].

            - last_run: typing.Optional[dt.datetime].

            - created_at: typing.Optional[dt.datetime].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import WorkflowSettings
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        await client.workflows.create(
            code_as_string="code_as_string",
            settings=WorkflowSettings(),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"code_as_string": code_as_string, "settings": settings}
        if workflow_id is not OMIT:
            _request["workflow_id"] = workflow_id
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if workflow_name is not OMIT:
            _request["workflow_name"] = workflow_name
        if last_run is not OMIT:
            _request["last_run"] = last_run
        if created_at is not OMIT:
            _request["created_at"] = created_at
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workflows"),
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
            return pydantic.parse_obj_as(WorkflowResponse, _response.json())  # type: ignore
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

    async def invoke(
        self,
        workflow_id: str,
        *,
        websocket_id: typing.Optional[str] = None,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - workflow_id: str.

            - websocket_id: typing.Optional[str].

            - request: typing.Dict[str, typing.Any].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        await client.workflows.invoke(
            workflow_id="workflow_id",
            request={},
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"workflows/{jsonable_encoder(workflow_id)}/invoke"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "websocket_id": websocket_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
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

    async def convert_code_to_string(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkflowResponse:
        """
        Parameters:
            - request: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        await client.workflows.convert_code_to_string(
            request="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "workflows/code"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request),
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
            return pydantic.parse_obj_as(WorkflowResponse, _response.json())  # type: ignore
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
