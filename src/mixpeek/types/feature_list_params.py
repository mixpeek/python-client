# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sort_option import SortOption
from .shared_params.filter_condition import FilterCondition

__all__ = [
    "FeatureListParams",
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
]


class FeatureListParams(TypedDict, total=False):
    collection_ids: Required[List[str]]
    """Collection IDs to filter features"""

    offset_feature_id: Optional[str]
    """The offset id to start returning results from. Used for pagination"""

    page_size: int

    filters: Optional[Filters]
    """Complex nested query filters"""

    select: Optional[Iterable[object]]
    """List of fields to return in results, supports dot notation."""

    sort: Optional[SortOption]
    """
    List of fields to sort by, with direction (asc or desc). NOTE: fields will
    require a specialty index to use this, consult with the team.
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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersAndLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[
    FiltersAndLogicalOperatorInputNorLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersAndLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")
    ]


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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersAndLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[
    FiltersAndLogicalOperatorInputOrLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersAndLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersAndLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


FiltersAndLogicalOperatorInputOr: TypeAlias = Union[
    FiltersAndLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersNorLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[
    FiltersNorLogicalOperatorInputAndLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersNorLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")
    ]


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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersNorLogicalOperatorInputOrLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersNorLogicalOperatorInputOrLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersNorLogicalOperatorInputOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersNorLogicalOperatorInputOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


FiltersNorLogicalOperatorInputOr: TypeAlias = Union[
    FiltersNorLogicalOperatorInputOrLogicalOperatorInput, FilterCondition
]


class FiltersNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersOrLogicalOperatorInputAndLogicalOperatorInputNor: TypeAlias = Union[
    FiltersOrLogicalOperatorInputAndLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputAndLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInputAndLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputAndLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


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

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputNor]],
        PropertyInfo(alias="NOR"),
    ]

    or_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInputOr]],
        PropertyInfo(alias="OR"),
    ]


FiltersOrLogicalOperatorInputNorLogicalOperatorInputAnd: TypeAlias = Union[
    FiltersOrLogicalOperatorInputNorLogicalOperatorInputAndLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputNor: TypeAlias = Union[FilterCondition, object]

FiltersOrLogicalOperatorInputNorLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInputNorLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputAnd]], PropertyInfo(alias="AND")
    ]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[
        Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputNor]], PropertyInfo(alias="NOR")
    ]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputNorLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


FiltersOrLogicalOperatorInputNor: TypeAlias = Union[
    FiltersOrLogicalOperatorInputNorLogicalOperatorInput, FilterCondition
]

FiltersOrLogicalOperatorInputOr: TypeAlias = Union[FilterCondition, object]


class FiltersOrLogicalOperatorInput(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOrLogicalOperatorInputOr]], PropertyInfo(alias="OR")]


FiltersOr: TypeAlias = Union[FiltersOrLogicalOperatorInput, FilterCondition]


class Filters(TypedDict, total=False):
    and_: Annotated[Optional[Iterable[FiltersAnd]], PropertyInfo(alias="AND")]

    case_sensitive: Optional[bool]
    """Whether to perform case-sensitive matching"""

    nor: Annotated[Optional[Iterable[FiltersNor]], PropertyInfo(alias="NOR")]

    or_: Annotated[Optional[Iterable[FiltersOr]], PropertyInfo(alias="OR")]
