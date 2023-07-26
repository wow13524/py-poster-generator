from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import Any, Callable, ClassVar, Dict, Generic, Type, TypeVar

T = TypeVar("T")

@dataclass(frozen=True,kw_only=True,slots=True)
class Element(DataClassJsonMixin):
    type: str
    args: Dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True,kw_only=True,slots=True)
class Expression(DataClassJsonMixin, Generic[T]):
    type: str
    args: Dict[str, Any] = field(default_factory=dict)
    evaluate: Callable[..., T]

@dataclass(frozen=True,kw_only=True,slots=True)
class Plugin:
    elements: ClassVar[set[Type[Element]]] = set()
    expressions: ClassVar[set[Type[Expression[Any]]]] = set()

    @classmethod
    def new_context(cls) -> Any:
        return None