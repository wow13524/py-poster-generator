from abc import ABC
from PIL.Image import Image
from typing import Any, Callable, Dict, Generic, ParamSpec, Type, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = ParamSpec("V")

class Expression(ABC, Generic[T, U]):
    _fields: Dict[str, Any]
    evaluate: Callable[..., T]

class Element(Expression[Image, T]):
    pass

class Plugin(ABC, Generic[T]):
    elements: set[Type[Element[T]]] = set()
    expressions: set[Type[Expression[Any, T]]] = set()
   
    def new_context(self) -> T:
        raise NotImplemented