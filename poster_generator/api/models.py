from typing import Any, Callable, ClassVar, Dict, Type, TypeVar

T = TypeVar("T")

class Evaluatable:
    _fields: Dict[str, Any]
    evaluate: Callable[..., Any]

class Element(Evaluatable):
    pass

class Expression(Evaluatable):
    pass

class Plugin:
    elements: ClassVar[set[Type[Element]]] = set()
    expressions: ClassVar[set[Type[Expression]]] = set()

    def new_context(self) -> Any:
        return None