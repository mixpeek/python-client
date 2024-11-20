# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

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
from ...types.entities import face_list_params, face_create_params, face_update_params
from ...types.entities.face_response import FaceResponse
from ...types.entities.face_list_response import FaceListResponse

__all__ = ["FacesResource", "AsyncFacesResource"]


class FacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return FacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return FacesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_id: str,
        file: FileTypes,
        metadata: str | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceResponse:
        """Register Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "collection_id": collection_id,
                "file": file,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/entities/faces",
            body=maybe_transform(body, face_create_params.FaceCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaceResponse,
        )

    def update(
        self,
        *,
        path_face_id: str,
        collection_id: str,
        body_face_id: str,
        metadata: object,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceResponse:
        """Update Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_face_id:
            raise ValueError(f"Expected a non-empty value for `path_face_id` but received {path_face_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._patch(
            f"/entities/faces/{path_face_id}",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "face_id": body_face_id,
                    "metadata": metadata,
                },
                face_update_params.FaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaceResponse,
        )

    def list(
        self,
        collection_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceListResponse:
        """
        List registered faces for a specific collection.

        Args:
          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._get(
            f"/entities/faces/{collection_id}",
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
                    face_list_params.FaceListParams,
                ),
            ),
            cast_to=FaceListResponse,
        )

    def delete(
        self,
        face_id: str,
        *,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return self._delete(
            f"/entities/faces/{face_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncFacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncFacesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_id: str,
        file: FileTypes,
        metadata: str | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceResponse:
        """Register Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "collection_id": collection_id,
                "file": file,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/entities/faces",
            body=await async_maybe_transform(body, face_create_params.FaceCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaceResponse,
        )

    async def update(
        self,
        *,
        path_face_id: str,
        collection_id: str,
        body_face_id: str,
        metadata: object,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceResponse:
        """Update Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_face_id:
            raise ValueError(f"Expected a non-empty value for `path_face_id` but received {path_face_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._patch(
            f"/entities/faces/{path_face_id}",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "face_id": body_face_id,
                    "metadata": metadata,
                },
                face_update_params.FaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaceResponse,
        )

    async def list(
        self,
        collection_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FaceListResponse:
        """
        List registered faces for a specific collection.

        Args:
          x_namespace: Optional namespace for data isolation. Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._get(
            f"/entities/faces/{collection_id}",
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
                    face_list_params.FaceListParams,
                ),
            ),
            cast_to=FaceListResponse,
        )

    async def delete(
        self,
        face_id: str,
        *,
        x_namespace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Face

        Args:
          x_namespace: Optional namespace for data isolation.

        Example: 'netflix_prod' or
              'spotify_recs_dev'. To create a namespace, use the /namespaces endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        extra_headers = {**strip_not_given({"X-Namespace": x_namespace}), **(extra_headers or {})}
        return await self._delete(
            f"/entities/faces/{face_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FacesResourceWithRawResponse:
    def __init__(self, faces: FacesResource) -> None:
        self._faces = faces

        self.create = to_raw_response_wrapper(
            faces.create,
        )
        self.update = to_raw_response_wrapper(
            faces.update,
        )
        self.list = to_raw_response_wrapper(
            faces.list,
        )
        self.delete = to_raw_response_wrapper(
            faces.delete,
        )


class AsyncFacesResourceWithRawResponse:
    def __init__(self, faces: AsyncFacesResource) -> None:
        self._faces = faces

        self.create = async_to_raw_response_wrapper(
            faces.create,
        )
        self.update = async_to_raw_response_wrapper(
            faces.update,
        )
        self.list = async_to_raw_response_wrapper(
            faces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            faces.delete,
        )


class FacesResourceWithStreamingResponse:
    def __init__(self, faces: FacesResource) -> None:
        self._faces = faces

        self.create = to_streamed_response_wrapper(
            faces.create,
        )
        self.update = to_streamed_response_wrapper(
            faces.update,
        )
        self.list = to_streamed_response_wrapper(
            faces.list,
        )
        self.delete = to_streamed_response_wrapper(
            faces.delete,
        )


class AsyncFacesResourceWithStreamingResponse:
    def __init__(self, faces: AsyncFacesResource) -> None:
        self._faces = faces

        self.create = async_to_streamed_response_wrapper(
            faces.create,
        )
        self.update = async_to_streamed_response_wrapper(
            faces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            faces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            faces.delete,
        )
