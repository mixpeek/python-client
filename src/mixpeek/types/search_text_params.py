# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SearchTextParams",
    "Filters",
    "FiltersAnd",
    "FiltersAndLogicalOperator",
    "FiltersAndLogicalOperatorAnd",
    "FiltersAndLogicalOperatorAndFilterCondition",
    "FiltersAndLogicalOperatorNor",
    "FiltersAndLogicalOperatorNorLogicalOperator",
    "FiltersAndLogicalOperatorNorLogicalOperatorAnd",
    "FiltersAndLogicalOperatorNorLogicalOperatorAndFilterCondition",
    "FiltersAndLogicalOperatorNorLogicalOperatorNor",
    "FiltersAndLogicalOperatorNorLogicalOperatorNorFilterCondition",
    "FiltersAndLogicalOperatorNorLogicalOperatorOr",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperator",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAnd",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAndFilterCondition",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNor",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNorFilterCondition",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOr",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOrFilterCondition",
    "FiltersAndLogicalOperatorNorLogicalOperatorOrFilterCondition",
    "FiltersAndLogicalOperatorNorFilterCondition",
    "FiltersAndLogicalOperatorOr",
    "FiltersAndLogicalOperatorOrLogicalOperator",
    "FiltersAndLogicalOperatorOrLogicalOperatorAnd",
    "FiltersAndLogicalOperatorOrLogicalOperatorAndFilterCondition",
    "FiltersAndLogicalOperatorOrLogicalOperatorNor",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperator",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAnd",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAndFilterCondition",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNor",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNorFilterCondition",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOr",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOrFilterCondition",
    "FiltersAndLogicalOperatorOrLogicalOperatorNorFilterCondition",
    "FiltersAndLogicalOperatorOrLogicalOperatorOr",
    "FiltersAndLogicalOperatorOrLogicalOperatorOrFilterCondition",
    "FiltersAndLogicalOperatorOrFilterCondition",
    "FiltersAndFilterCondition",
    "FiltersNor",
    "FiltersNorLogicalOperator",
    "FiltersNorLogicalOperatorAnd",
    "FiltersNorLogicalOperatorAndLogicalOperator",
    "FiltersNorLogicalOperatorAndLogicalOperatorAnd",
    "FiltersNorLogicalOperatorAndLogicalOperatorAndFilterCondition",
    "FiltersNorLogicalOperatorAndLogicalOperatorNor",
    "FiltersNorLogicalOperatorAndLogicalOperatorNorFilterCondition",
    "FiltersNorLogicalOperatorAndLogicalOperatorOr",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperator",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAnd",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAndFilterCondition",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNor",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNorFilterCondition",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOr",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOrFilterCondition",
    "FiltersNorLogicalOperatorAndLogicalOperatorOrFilterCondition",
    "FiltersNorLogicalOperatorAndFilterCondition",
    "FiltersNorLogicalOperatorNor",
    "FiltersNorLogicalOperatorNorFilterCondition",
    "FiltersNorLogicalOperatorOr",
    "FiltersNorLogicalOperatorOrLogicalOperator",
    "FiltersNorLogicalOperatorOrLogicalOperatorAnd",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperator",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAnd",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAndFilterCondition",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNor",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNorFilterCondition",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOr",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOrFilterCondition",
    "FiltersNorLogicalOperatorOrLogicalOperatorAndFilterCondition",
    "FiltersNorLogicalOperatorOrLogicalOperatorNor",
    "FiltersNorLogicalOperatorOrLogicalOperatorNorFilterCondition",
    "FiltersNorLogicalOperatorOrLogicalOperatorOr",
    "FiltersNorLogicalOperatorOrLogicalOperatorOrFilterCondition",
    "FiltersNorLogicalOperatorOrFilterCondition",
    "FiltersNorFilterCondition",
    "FiltersOr",
    "FiltersOrLogicalOperator",
    "FiltersOrLogicalOperatorAnd",
    "FiltersOrLogicalOperatorAndLogicalOperator",
    "FiltersOrLogicalOperatorAndLogicalOperatorAnd",
    "FiltersOrLogicalOperatorAndLogicalOperatorAndFilterCondition",
    "FiltersOrLogicalOperatorAndLogicalOperatorNor",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperator",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAnd",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAndFilterCondition",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNor",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNorFilterCondition",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOr",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOrFilterCondition",
    "FiltersOrLogicalOperatorAndLogicalOperatorNorFilterCondition",
    "FiltersOrLogicalOperatorAndLogicalOperatorOr",
    "FiltersOrLogicalOperatorAndLogicalOperatorOrFilterCondition",
    "FiltersOrLogicalOperatorAndFilterCondition",
    "FiltersOrLogicalOperatorNor",
    "FiltersOrLogicalOperatorNorLogicalOperator",
    "FiltersOrLogicalOperatorNorLogicalOperatorAnd",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperator",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAnd",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAndFilterCondition",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNor",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNorFilterCondition",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOr",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOrFilterCondition",
    "FiltersOrLogicalOperatorNorLogicalOperatorAndFilterCondition",
    "FiltersOrLogicalOperatorNorLogicalOperatorNor",
    "FiltersOrLogicalOperatorNorLogicalOperatorNorFilterCondition",
    "FiltersOrLogicalOperatorNorLogicalOperatorOr",
    "FiltersOrLogicalOperatorNorLogicalOperatorOrFilterCondition",
    "FiltersOrLogicalOperatorNorFilterCondition",
    "FiltersOrLogicalOperatorOr",
    "FiltersOrLogicalOperatorOrFilterCondition",
    "FiltersOrFilterCondition",
    "GroupBy",
]


class SearchTextParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    query: Required[str]

    filters: Optional[Filters]
    """Complex nested query filters"""

    group_by: Optional[GroupBy]
    """Grouping options for search results"""

    model_id: Optional[Literal["vuse-generic-v1", "multimodal-v1", "image-embed-v1"]]
    """Embedding model to use"""

    sort: Optional[Iterable[Dict[str, str]]]
    """List of fields to sort by, with direction (asc or desc)"""

    authorization: Annotated[str, PropertyInfo(alias="Authorization")]

    index_id: Annotated[str, PropertyInfo(alias="index-id")]
    """filter by organization"""


class FiltersAndLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorAnd: TypeAlias = Union[FiltersAndLogicalOperatorAndFilterCondition, object]


class FiltersAndLogicalOperatorNorLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorAnd: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorAndFilterCondition, object
]


class FiltersAndLogicalOperatorNorLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorNor: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorNorFilterCondition, object
]


class FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAnd: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAndFilterCondition, object
]


class FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNor: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNorFilterCondition, object
]


class FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOr: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOrFilterCondition, object
]


class FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersAndLogicalOperatorNorLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNorLogicalOperatorOr: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperatorOrLogicalOperator,
    FiltersAndLogicalOperatorNorLogicalOperatorOrFilterCondition,
]


class FiltersAndLogicalOperatorNorLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorNorLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersAndLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorNor: TypeAlias = Union[
    FiltersAndLogicalOperatorNorLogicalOperator, FiltersAndLogicalOperatorNorFilterCondition
]


class FiltersAndLogicalOperatorOrLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorAnd: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorAndFilterCondition, object
]


class FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAnd: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAndFilterCondition, object
]


class FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNor: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNorFilterCondition, object
]


class FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOr: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOrFilterCondition, object
]


class FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersAndLogicalOperatorOrLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorNor: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorNorLogicalOperator,
    FiltersAndLogicalOperatorOrLogicalOperatorNorFilterCondition,
]


class FiltersAndLogicalOperatorOrLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOrLogicalOperatorOr: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperatorOrFilterCondition, object
]


class FiltersAndLogicalOperatorOrLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorOrLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersAndLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAndLogicalOperatorOr: TypeAlias = Union[
    FiltersAndLogicalOperatorOrLogicalOperator, FiltersAndLogicalOperatorOrFilterCondition
]


class FiltersAndLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersAndLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersAnd: TypeAlias = Union[FiltersAndLogicalOperator, FiltersAndFilterCondition]


class FiltersNorLogicalOperatorAndLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorAndFilterCondition, object
]


class FiltersNorLogicalOperatorAndLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorNor: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorNorFilterCondition, object
]


class FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAndFilterCondition, object
]


class FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNor: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNorFilterCondition, object
]


class FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOr: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOrFilterCondition, object
]


class FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersNorLogicalOperatorAndLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAndLogicalOperatorOr: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperatorOrLogicalOperator,
    FiltersNorLogicalOperatorAndLogicalOperatorOrFilterCondition,
]


class FiltersNorLogicalOperatorAndLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorAndLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersNorLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorAndLogicalOperator, FiltersNorLogicalOperatorAndFilterCondition
]


class FiltersNorLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorNor: TypeAlias = Union[FiltersNorLogicalOperatorNorFilterCondition, object]


class FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAndFilterCondition, object
]


class FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNor: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNorFilterCondition, object
]


class FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOr: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOrFilterCondition, object
]


class FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersNorLogicalOperatorOrLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorAndLogicalOperator,
    FiltersNorLogicalOperatorOrLogicalOperatorAndFilterCondition,
]


class FiltersNorLogicalOperatorOrLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorNor: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorNorFilterCondition, object
]


class FiltersNorLogicalOperatorOrLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOrLogicalOperatorOr: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperatorOrFilterCondition, object
]


class FiltersNorLogicalOperatorOrLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorOrLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersNorLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNorLogicalOperatorOr: TypeAlias = Union[
    FiltersNorLogicalOperatorOrLogicalOperator, FiltersNorLogicalOperatorOrFilterCondition
]


class FiltersNorLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNorLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersNor: TypeAlias = Union[FiltersNorLogicalOperator, FiltersNorFilterCondition]


class FiltersOrLogicalOperatorAndLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorAndFilterCondition, object
]


class FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAndFilterCondition, object
]


class FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNor: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNorFilterCondition, object
]


class FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOr: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOrFilterCondition, object
]


class FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersOrLogicalOperatorAndLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorNor: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorNorLogicalOperator,
    FiltersOrLogicalOperatorAndLogicalOperatorNorFilterCondition,
]


class FiltersOrLogicalOperatorAndLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAndLogicalOperatorOr: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperatorOrFilterCondition, object
]


class FiltersOrLogicalOperatorAndLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorAndLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersOrLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorAndLogicalOperator, FiltersOrLogicalOperatorAndFilterCondition
]


class FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAndFilterCondition, object
]


class FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNor: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNorFilterCondition, object
]


class FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOr: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOrFilterCondition, object
]


class FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperator(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperatorOr]], PropertyInfo(alias="OR")
    ]


class FiltersOrLogicalOperatorNorLogicalOperatorAndFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorAndLogicalOperator,
    FiltersOrLogicalOperatorNorLogicalOperatorAndFilterCondition,
]


class FiltersOrLogicalOperatorNorLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorNor: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorNorFilterCondition, object
]


class FiltersOrLogicalOperatorNorLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNorLogicalOperatorOr: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperatorOrFilterCondition, object
]


class FiltersOrLogicalOperatorNorLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorNorLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersOrLogicalOperatorNorFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorNor: TypeAlias = Union[
    FiltersOrLogicalOperatorNorLogicalOperator, FiltersOrLogicalOperatorNorFilterCondition
]


class FiltersOrLogicalOperatorOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOrLogicalOperatorOr: TypeAlias = Union[FiltersOrLogicalOperatorOrFilterCondition, object]


class FiltersOrLogicalOperator(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersOrLogicalOperatorNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorOr]], PropertyInfo(alias="OR")]


class FiltersOrFilterCondition(TypedDict, total=False):
    key: Required[str]
    """Field name to filter on"""

    value: Required[object]
    """Value to compare against"""

    operator: str
    """Comparison operator"""


FiltersOr: TypeAlias = Union[FiltersOrLogicalOperator, FiltersOrFilterCondition]


class Filters(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOr]], PropertyInfo(alias="OR")]


class GroupBy(TypedDict, total=False):
    field: Optional[str]
    """Field to group by"""

    max_features: Optional[int]
    """Maximum number of features to group"""
