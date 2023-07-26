from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Type, TypeVar

T = TypeVar("T")

@dataclass(frozen=True,kw_only=True,slots=True)
class Element:
    pass

@dataclass(frozen=True,kw_only=True,slots=True)
class Expression:
    evaluate: Callable[..., Any]

@dataclass(frozen=True,kw_only=True,slots=True)
class Plugin:
    elements: ClassVar[set[Type[Element]]] = set()
    expressions: ClassVar[set[Type[Expression]]] = set()

    def new_context(self) -> Any:
        return None