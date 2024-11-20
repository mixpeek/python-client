# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "User",
    "APIKey",
    "Namespace",
    "NamespacePayloadIndexes",
    "NamespacePayloadIndexesFieldSchema",
    "NamespacePayloadIndexesFieldSchemaTextIndexParams",
    "NamespacePayloadIndexesFieldSchemaIntegerIndexParams",
    "NamespacePayloadIndexesFieldSchemaKeywordIndexParams",
    "NamespacePayloadIndexesFieldSchemaFloatIndexParams",
    "NamespacePayloadIndexesFieldSchemaGeoIndexParams",
    "NamespacePayloadIndexesFieldSchemaDatetimeIndexParams",
    "NamespacePayloadIndexesFieldSchemaUuidIndexParams",
    "NamespacePayloadIndexesFieldSchemaBoolIndexParams",
]


class APIKey(BaseModel):
    created_at: Optional[datetime] = None

    key: Optional[str] = None

    name: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaTextIndexParams(BaseModel):
    lowercase: Optional[bool] = None

    max_token_len: Optional[int] = None

    min_token_len: Optional[int] = None

    tokenizer: Optional[Literal["word", "whitespace", "prefix", "multilingual"]] = None

    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaIntegerIndexParams(BaseModel):
    lookup: Optional[bool] = None

    range: Optional[bool] = None

    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaKeywordIndexParams(BaseModel):
    is_tenant: Optional[bool] = None

    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaFloatIndexParams(BaseModel):
    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaGeoIndexParams(BaseModel):
    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaDatetimeIndexParams(BaseModel):
    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaUuidIndexParams(BaseModel):
    is_tenant: Optional[bool] = None

    type: Optional[str] = None


class NamespacePayloadIndexesFieldSchemaBoolIndexParams(BaseModel):
    type: Optional[str] = None


NamespacePayloadIndexesFieldSchema: TypeAlias = Union[
    NamespacePayloadIndexesFieldSchemaTextIndexParams,
    NamespacePayloadIndexesFieldSchemaIntegerIndexParams,
    NamespacePayloadIndexesFieldSchemaKeywordIndexParams,
    NamespacePayloadIndexesFieldSchemaFloatIndexParams,
    NamespacePayloadIndexesFieldSchemaGeoIndexParams,
    NamespacePayloadIndexesFieldSchemaDatetimeIndexParams,
    NamespacePayloadIndexesFieldSchemaUuidIndexParams,
    NamespacePayloadIndexesFieldSchemaBoolIndexParams,
    None,
]


class NamespacePayloadIndexes(BaseModel):
    field_name: str

    type: Literal["keyword", "integer", "float", "bool", "geo", "datetime", "text", "uuid"]

    field_schema: Optional[NamespacePayloadIndexesFieldSchema] = None
    """Configuration for text index"""


class Namespace(BaseModel):
    namespace_id: str

    payload_indexes: Optional[Dict[str, NamespacePayloadIndexes]] = None

    vectors_indexes: List[str]


class User(BaseModel):
    email: str

    account_type: Optional[str] = None

    api_keys: Optional[List[APIKey]] = None

    credit_count: Optional[int] = None

    index_ids: Optional[List[str]] = None

    metadata: Optional[object] = None

    namespaces: Optional[List[Namespace]] = None

    user_id: Optional[str] = None
