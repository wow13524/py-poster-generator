from dataclasses import dataclass
from typing import Any, ClassVar, Type

@dataclass(frozen=True,kw_only=True,slots=True)
class Element:
    pass

@dataclass(frozen=True,kw_only=True,slots=True)
class Expression:
    pass

@dataclass(frozen=True,kw_only=True,slots=True)
class Plugin:
    elements: ClassVar[set[Type[Element]]] = set()
    expressions: ClassVar[set[Type[Expression]]] = set()

    @classmethod
    def new_context(cls) -> Any:
        return None