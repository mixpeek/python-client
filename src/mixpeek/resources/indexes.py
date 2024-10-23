# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Mapping, Iterable, Optional, cast

import httpx

from ..types import index_url_params, index_upload_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    strip_not_given,
    deepcopy_minimal,
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
from ..types.index_url_response import IndexURLResponse
from ..types.index_upload_response import IndexUploadResponse

__all__ = ["IndexesResource", "AsyncIndexesResource"]


class IndexesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return IndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return IndexesResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        collection_id: str,
        file: FileTypes,
        image_settings: str | NotGiven = NOT_GIVEN,
        metadata: str | NotGiven = NOT_GIVEN,
        video_settings: str | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexUploadResponse:
        """
        Index Upload

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
        body = deepcopy_minimal(
            {
                "collection_id": collection_id,
                "file": file,
                "image_settings": image_settings,
                "metadata": metadata,
                "video_settings": video_settings,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/index/upload",
            body=maybe_transform(body, index_upload_params.IndexUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexUploadResponse,
        )

    def url(
        self,
        *,
        collection_id: str,
        url: str,
        file_update: Optional[index_url_params.FileUpdate] | NotGiven = NOT_GIVEN,
        image_settings: Optional[index_url_params.ImageSettings] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        prevent_duplicate: Optional[bool] | NotGiven = NOT_GIVEN,
        should_save: Optional[bool] | NotGiven = NOT_GIVEN,
        video_settings: Optional[Iterable[index_url_params.VideoSetting]] | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexURLResponse:
        """
        Index Url

        Args:
          collection_id: Unique identifier for the collection where the processed file will be stored.

          url: The URL of the file to be processed. Must be a valid HTTP or HTTPS URL.

          file_update: File update information for existing files

          image_settings: Settings for image processing. Only applicable if the URL points to an image
              file.

          metadata: Additional metadata associated with the file. Can include any key-value pairs
              relevant to the file.

          prevent_duplicate: Indicates whether to prevent duplicate processing of the same URL.

          should_save: Indicates whether the processed file should be uploaded to S3 storage.

          video_settings: Settings for video processing. Only applicable if the URL points to a video
              file.

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
        return cast(
            IndexURLResponse,
            self._post(
                "/index/url",
                body=maybe_transform(
                    {
                        "collection_id": collection_id,
                        "url": url,
                        "file_update": file_update,
                        "image_settings": image_settings,
                        "metadata": metadata,
                        "prevent_duplicate": prevent_duplicate,
                        "should_save": should_save,
                        "video_settings": video_settings,
                    },
                    index_url_params.IndexURLParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IndexURLResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncIndexesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncIndexesResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        collection_id: str,
        file: FileTypes,
        image_settings: str | NotGiven = NOT_GIVEN,
        metadata: str | NotGiven = NOT_GIVEN,
        video_settings: str | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexUploadResponse:
        """
        Index Upload

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
        body = deepcopy_minimal(
            {
                "collection_id": collection_id,
                "file": file,
                "image_settings": image_settings,
                "metadata": metadata,
                "video_settings": video_settings,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/index/upload",
            body=await async_maybe_transform(body, index_upload_params.IndexUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexUploadResponse,
        )

    async def url(
        self,
        *,
        collection_id: str,
        url: str,
        file_update: Optional[index_url_params.FileUpdate] | NotGiven = NOT_GIVEN,
        image_settings: Optional[index_url_params.ImageSettings] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        prevent_duplicate: Optional[bool] | NotGiven = NOT_GIVEN,
        should_save: Optional[bool] | NotGiven = NOT_GIVEN,
        video_settings: Optional[Iterable[index_url_params.VideoSetting]] | NotGiven = NOT_GIVEN,
        authorization: str | NotGiven = NOT_GIVEN,
        index_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexURLResponse:
        """
        Index Url

        Args:
          collection_id: Unique identifier for the collection where the processed file will be stored.

          url: The URL of the file to be processed. Must be a valid HTTP or HTTPS URL.

          file_update: File update information for existing files

          image_settings: Settings for image processing. Only applicable if the URL points to an image
              file.

          metadata: Additional metadata associated with the file. Can include any key-value pairs
              relevant to the file.

          prevent_duplicate: Indicates whether to prevent duplicate processing of the same URL.

          should_save: Indicates whether the processed file should be uploaded to S3 storage.

          video_settings: Settings for video processing. Only applicable if the URL points to a video
              file.

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
        return cast(
            IndexURLResponse,
            await self._post(
                "/index/url",
                body=await async_maybe_transform(
                    {
                        "collection_id": collection_id,
                        "url": url,
                        "file_update": file_update,
                        "image_settings": image_settings,
                        "metadata": metadata,
                        "prevent_duplicate": prevent_duplicate,
                        "should_save": should_save,
                        "video_settings": video_settings,
                    },
                    index_url_params.IndexURLParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, IndexURLResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class IndexesResourceWithRawResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.upload = to_raw_response_wrapper(
            indexes.upload,
        )
        self.url = to_raw_response_wrapper(
            indexes.url,
        )


class AsyncIndexesResourceWithRawResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.upload = async_to_raw_response_wrapper(
            indexes.upload,
        )
        self.url = async_to_raw_response_wrapper(
            indexes.url,
        )


class IndexesResourceWithStreamingResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.upload = to_streamed_response_wrapper(
            indexes.upload,
        )
        self.url = to_streamed_response_wrapper(
            indexes.url,
        )


class AsyncIndexesResourceWithStreamingResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.upload = async_to_streamed_response_wrapper(
            indexes.upload,
        )
        self.url = async_to_streamed_response_wrapper(
            indexes.url,
        )
