from abc import ABC
from PIL.Image import Image
from inspect import Parameter, getmembers, isfunction, signature
from typing import Any, Callable, ClassVar, Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union, cast
from .constants import REQUIRED

T = TypeVar("T")
U = TypeVar("U")

class Expression(ABC, Generic[T, U]):
    _plugin: ClassVar['Plugin[Any]']
    _fields: Dict[str, Any]
    
    @classmethod
    def _get_fields_with_attr(cls, attr: str) -> set[Callable[..., Any]]:
        fields: List[Tuple[str, Callable[..., Any]]] = getmembers(
            cls,
            lambda obj: isfunction(obj) and hasattr(obj, attr)
        )
        return {param for _,param in fields}

    @classmethod
    def get_allowed_fields(cls, fns: Union[Callable[..., Any], set[Callable[..., Any]]]) -> set[Parameter]:
        if type(fns) == set:
            fields: set[Parameter] = set()
            for fn in cast(set[Callable[..., Any]], fns):
                fields.update(signature(fn).parameters.values())
            return fields
        else:
            return set(signature(cast(Callable[..., Any], fns)).parameters.values())

    @classmethod
    def get_compute_fields(cls) -> set[Callable[..., Any]]:
        return cls._get_fields_with_attr("_compute_field")
    
    @classmethod
    def get_forward_fields(cls) -> set[Callable[..., Any]]:
        return cls._get_fields_with_attr("_forward")

    @classmethod
    def get_required_fields(cls, fns: Optional[set[Callable[..., Any]]]=None) -> set[Parameter]:
        if fns is None:
            fns = set()
            fns.update(cls.get_compute_fields())
            fns.add(cls.evaluate)
        field_names: set[str] = {fn.__name__ for fn in fns}.union({"self", "context"})
        required_fields: set[Parameter] = set()
        for fn in fns:
            required_fields.update(set(filter(
                lambda x: x.name not in field_names and x.default == REQUIRED,
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