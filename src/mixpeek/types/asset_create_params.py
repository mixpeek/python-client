# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.filter_condition import FilterCondition

__all__ = [
    "AssetCreateParams",
    "Filters",
    "FiltersAnd",
    "FiltersAndLogicalOperatorInput",
    "FiltersAndLogicalOperatorInputAnd",
    "FiltersAndLogicalOperatorInputNor",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInput",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputAnd",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputNor",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputOr",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInput",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputAnd",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputNor",
    "FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputOr",
    "FiltersAndLogicalOperatorInputOr",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInput",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputAnd",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputNor",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInput",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputAnd",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputNor",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputOr",
    "FiltersAndLogicalOperatorInputOrLogicalOperatorInputOr",
    "FiltersNor",
    "FiltersNorLogicalOperatorInput",
    "FiltersNorLogicalOperatorInputAnd",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInput",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputAnd",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputNor",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputOr",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInput",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputAnd",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputNor",
    "FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputOr",
    "FiltersNorLogicalOperatorInputNor",
    "FiltersNorLogicalOperatorInputOr",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInput",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputAnd",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInput",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputAnd",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputNor",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputOr",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputNor",
    "FiltersNorLogicalOperatorInputOrLogicalOperatorInputOr",
    "FiltersOr",
    "FiltersOrLogicalOperatorInput",
    "FiltersOrLogicalOperatorInputAnd",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInput",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputAnd",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputNor",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInput",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputAnd",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputNor",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputOr",
    "FiltersOrLogicalOperatorInputAndLogicalOperatorInputOr",
    "FiltersOrLogicalOperatorInputNor",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInput",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputAnd",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInput",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputAnd",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputNor",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputOr",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputNor",
    "FiltersOrLogicalOperatorInputNorLogicalOperatorInputOr",
    "FiltersOrLogicalOperatorInputOr",
    "GroupBy",
]


class AssetCreateParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """List of Collection IDs to search within, required"""

    page: Optional[int]

    page_size: int

    filters: Optional[Filters]
    """Used for filtering across all indexes"""

    group_by: Optional[GroupBy]
    """Grouping options for search results"""

    return_url: Optional[bool]
    """
    Return the presigned URL for the asset and preview asset, this will introduce
    additional latency
    """

    select: Optional[List[str]]
    """List of fields to return in results, supports dot notation.

    If None, all fields are returned.
    """

    sort: Optional[SortOption]
    """List of fields to sort by, with direction (asc or desc).

    Supports dot notation for nested fields.
    """

    x_namespace: Annotated[str, PropertyInfo(alias="X-Namespace")]
    """Optional namespace for data isolation.

    Example: 'netflix_prod' or 'spotify_recs_dev'. To create a namespace, use the
    /namespaces endpoint.
    """


FiltersAndLogicalOperatorInputAnd: TypeAlias = Union[FilterCondition, object]

FiltersAndLogicalOperatorInputNorLogicalOperatorInputAnd: TypeAlias = Union[FilterCondition, object]

FiltersAndLogicalOperatorInputNorLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersAndLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[
    FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersAndLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")
    ]
    """Logical OR operation"""


FiltersAndLogicalOperatorInputNor: TypeAlias = Union[
    FiltersAndLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputAnd: TypeAlias = Union[FilterCondition, object]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersAndLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[
    FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersAndLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersAndLogicalOperatorInputOr: TypeAlias = Union[
    FiltersAndLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersAnd: TypeAlias = Union[FiltersAndLogicalOperatorInput, FilterCondition]

FiltersNorLogicalOperatorInputAndLogicalOperatorInputAnd: TypeAlias = Union[FilterCondition, object]

FiltersNorLogicalOperatorInputAndLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersNorLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[
    FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersNorLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")
    ]
    """Logical OR operation"""


FiltersNorLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersNorLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersNorLogicalOperatorInputOrLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersNorLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersNorLogicalOperatorInputOr: TypeAlias = Union[
    FiltersNorLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersNor: TypeAlias = Union[FiltersNorLogicalOperatorInput, FilterCondition]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputAnd: TypeAlias = Union[FilterCondition, object]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersOrLogicalOperatorInputAndLogicalOperatorInputNor: TypeAlias = Union[
    FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersOrLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputAnd: TypeAlias = Union[
    FilterCondition, object
]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputNor: TypeAlias = Union[
    FilterCondition, object
]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[
    FilterCondition, object
]


class FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputAnd]],
        PropertyInfo(alias="AND"),
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]
    """Logical NOR operation"""

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]
    """Logical OR operation"""


FiltersOrLogicalOperatorInputNorLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersOrLogicalOperatorInputNor: TypeAlias = Union[
    FiltersOrLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


FiltersOr: TypeAlias = Union[FiltersOrLogicalOperatorInput, FilterCondition]


class Filters(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAnd]], PropertyInfo(alias="AND")]
    """Logical AND operation"""

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNor]], PropertyInfo(alias="NOR")]
    """Logical NOR operation"""

    or_: Annotated[Optional[Iterable[FiltersOr]], PropertyInfo(alias="OR")]
    """Logical OR operation"""


class GroupBy(TypedDict, total=False):
    field: Optional[str]
    """Field to group by

            Note: We currently do not support ad-hoc grouping.
            This means the field must be indexed separately.
            Please contact us to add additional fields for grouping.
    """

    max_assets: Optional[int]
    """Maximum number of assets to group"""

    sort: Optional[SortOption]
    """Sort options for ordering the inside of the groups"""
