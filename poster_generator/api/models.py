from abc import ABC
from PIL.Image import Image
from inspect import Parameter, getmembers, isfunction, signature
from typing import Any, Callable, ClassVar, Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union, cast
from .constants import DECORATOR_ATTR_COMPUTE_FIELD, DECORATOR_ATTR_FORWARD_FIELD, DECORATOR_ATTR_POST_EFFECT, REQUIRED

T = TypeVar("T")
U = TypeVar("U")

"""
Expression is an ABC which can be subclassed to represent a type of arbitrary
expression which can then be evaluated under a given context to yield a value.
Every Expression belongs to a Plugin which is responsible for creating contexts
that can be used when evaluating expressions.  An Expression is defined by the
following:
- Any instance methods decorated as a compute_field
- Its evaluate() method
- Any instance methods decorated as a post_effect
Each of these methods also define required and optional fields in their method
signatures, and these are compiled to determine all of the fields required in
order to evaluate an Expression.
When evaluating an Expression, all of the methods are executed in the following
order:
- Any instance methods decorated as a compute_field
    - These methods are evaluated first and their returned values are then made
      available for use after all compute_fields are evaluated.
    - The evaluated compute_fields can also optionally have their values
      forwarded to all child Expression evaluations.
- Its evaluate() method
    - The evaluate() method is evaluated with all of its requested fields as
      well as any compute_fields.
    - The resulting value is what the Expression is considered to evaluate to.
- Any instance methods decorated as a post_effect
    - These methods are evaluated last and are not expected to return anything.
    - These methods accept an additional 'evaluated' field which holds the
      result of evaluate().
    - These methods are especially useful for subclassable components which can
      require fields and perform actions without any additional support from
      subclasses.
While an Expression can define required and optional fields which are then
passed in by the user, these fields are not limited to explicit value types.
An Expression can also accept additional Expression objects in place of
explicit values when satisfying field requirements.
In this way, with the ability for developers to define their own Expression
classes, end users will have the ability to define and execute complex
routines under conditions imposed by the Expression classes made available.
"""
class Expression(ABC, Generic[T, U]):
    _plugin: ClassVar['Plugin[Any]']
    _fields: Dict[str, Any]
    
    @classmethod
    def _get_default_fns(cls) -> set[Callable[..., Any]]:
        fns: set[Callable[..., Any]] = set()
        fns.update(cls.get_compute_fields())
        fns.update(cls.get_post_fields())
        fns.add(cls.evaluate)
        return fns

    @classmethod
    def _get_fields_with_attr(cls, attr: str) -> set[Callable[..., Any]]:
        fields: List[Tuple[str, Callable[..., Any]]] = getmembers(
            cls,
            lambda obj: isfunction(obj) and hasattr(obj, attr)
        )
        return {param for _,param in fields}

    @classmethod
    def get_allowed_fields(cls, fns: Optional[Union[Callable[..., Any], set[Callable[..., Any]]]]=None) -> set[Parameter]:
        fns = fns or cls._get_default_fns()
        fields: set[Parameter] = set()
        if type(fns) == set:
            for fn in cast(set[Callable[..., Any]], fns):
                fields.update(signature(fn).parameters.values())
        else:
            fields = set(signature(cast(Callable[..., Any], fns)).parameters.values())
        fields = {field for field in fields if field.name not in ("self", "context", "evaluated")}
        return fields
        

    @classmethod
    def get_compute_fields(cls) -> set[Callable[..., Any]]:
        return cls._get_fields_with_attr(DECORATOR_ATTR_COMPUTE_FIELD)
    
    @classmethod
    def get_forward_fields(cls) -> set[Callable[..., Any]]:
        return cls._get_fields_with_attr(DECORATOR_ATTR_FORWARD_FIELD)
    
    @classmethod
    def get_post_fields(cls) -> set[Callable[..., Any]]:
        return cls._get_fields_with_attr(DECORATOR_ATTR_POST_EFFECT)

    @classmethod
    def get_required_fields(cls, fns: Optional[set[Callable[..., Any]]]=None) -> set[Parameter]:
        fns = fns or cls._get_default_fns()
        field_names: set[str] = {fn.__name__ for fn in fns}
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