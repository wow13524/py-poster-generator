from abc import ABC
from PIL.Image import Image
from inspect import Parameter, getmembers, isfunction, signature
from typing import Any, Callable, ClassVar, Dict, Generic, List, Tuple, Type, TypeVar
from .constants import REQUIRED

T = TypeVar("T")
U = TypeVar("U")

def is_compute_field(obj: Any) -> bool:
    return isfunction(obj) and hasattr(obj, "_compute_field")

class Expression(ABC, Generic[T, U]):
    _plugin: ClassVar['Plugin[Any]']
    _fields: Dict[str, Any]
    
    @classmethod
    def get_allowed_fields(cls, fn: Callable[..., Any]) -> set[Parameter]:
        return set(signature(fn).parameters.values())

    @classmethod
    def get_compute_fields(cls) -> set[Callable[..., Any]]:
        compute_fields: List[Tuple[str, Callable[..., Any]]] = getmembers(cls, is_compute_field)
        return {param for _,param in compute_fields}

    @classmethod
    def get_required_fields(cls) -> set[Parameter]:
        compute_fields: set[Callable[..., Any]] = cls.get_compute_fields().union({cls.evaluate})
        compute_fields_names: set[str] = {fn.__name__ for fn in compute_fields}.union({"self", "context"})
        required_fields: set[Parameter] = set()
        for fn in compute_fields:
            required_fields = required_fields.union(set(filter(
                lambda x: x.name not in compute_fields_names and x.default == REQUIRED,
                cls.get_allowed_fields(fn)
            )))
        return required_fields
        
    def evaluate(self, *, context: U) -> T:
        raise NotImplemented

class Element(Expression[Tuple[Image, Tuple[int, int]], T]):
    pass

class Plugin(ABC, Generic[T]):
    _expressions: ClassVar[set[Type[Expression[Any, Any]]]] = set()
   
    def new_context(self) -> T:
        raise NotImplemented