# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .faces import (
    FacesResource,
    AsyncFacesResource,
    FacesResourceWithRawResponse,
    AsyncFacesResourceWithRawResponse,
    FacesResourceWithStreamingResponse,
    AsyncFacesResourceWithStreamingResponse,
)
from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def faces(self) -> FacesResource:
        return FacesResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def faces(self) -> AsyncFacesResource:
        return AsyncFacesResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixpeek/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixpeek/python-client#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def faces(self) -> FacesResourceWithRawResponse:
        return FacesResourceWithRawResponse(self._entities.faces)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._entities.labels)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def faces(self) -> AsyncFacesResourceWithRawResponse:
        return AsyncFacesResourceWithRawResponse(self._entities.faces)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._entities.labels)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def faces(self) -> FacesResourceWithStreamingResponse:
        return FacesResourceWithStreamingResponse(self._entities.faces)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._entities.labels)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

    @cached_property
    def faces(self) -> AsyncFacesResourceWithStreamingResponse:
        return AsyncFacesResourceWithStreamingResponse(self._entities.faces)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._entities.labels)
