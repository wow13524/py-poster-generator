from abc import ABC
from PIL.Image import Image
from typing import Any, Callable, ClassVar, Dict, Generic, Type, TypeVar, TypeVarTuple

T = TypeVar("T")
U = TypeVar("U")
V = TypeVarTuple("V")

class Expression(ABC, Generic[T, U]):
    _plugin: ClassVar['Plugin[Any]']
    _fields: Dict[str, Any]
    evaluate: Callable[..., T]

class Element(Expression[Image, T]):
    pass

class Plugin(ABC, Generic[T]):
    _elements: ClassVar[set[Type[Element[Any]]]] = set()
    _expressions: ClassVar[set[Type[Expression[Any, Any]]]] = set()
   
    def new_context(self) -> T:
        raise NotImplemented