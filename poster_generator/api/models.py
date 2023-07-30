from abc import ABC
from PIL.Image import Image
from typing import Any, ClassVar, Dict, Generic, Tuple, Type, TypeVar

T = TypeVar("T")
U = TypeVar("U")

class Expression(ABC, Generic[T, U]):
    _plugin: ClassVar['Plugin[Any]']
    _fields: Dict[str, Any]
    
    def evaluate(self, *, context: U) -> T:
        raise NotImplemented

class Element(Expression[Tuple[Image, int, int], T]):
    pass

class Plugin(ABC, Generic[T]):
    _elements: ClassVar[set[Type[Element[Any]]]] = set()
    _expressions: ClassVar[set[Type[Expression[Any, Any]]]] = set()
   
    def new_context(self) -> T:
        raise NotImplemented