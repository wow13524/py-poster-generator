from typing import Any, Callable, Optional, Type, TypeVar
from .constants import DECORATOR_ATTR_COMPUTE_FIELD, DECORATOR_ATTR_FORWARD_FIELD, DECORATOR_ATTR_POST_EFFECT
from .models import Element, Expression, Plugin

T = TypeVar("T")

def expression(*expression_classes: Type[Expression[Any, T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    def decorator(plugin_class: Type[Plugin[T]]) -> Type[Plugin[T]]:
        for expression_class in expression_classes:
            setattr(expression_class, "_plugin", plugin_class)
        expressions: set[Type[Expression[Any, T]]] = getattr(plugin_class, "_expressions") or set()
        setattr(plugin_class, "_expressions", expressions.union(expression_classes))
        return plugin_class
    return decorator

def element(*element_classes: Type[Element[T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    return expression(*element_classes)

def compute_field(fn: Optional[Callable[..., Any]]=None, *, forward: bool=False) -> Callable[..., Any]:
    def inner(fn: Callable[..., T]) -> Callable[..., T]:
        setattr(fn, DECORATOR_ATTR_COMPUTE_FIELD, True)
        if forward:
            setattr(fn, DECORATOR_ATTR_FORWARD_FIELD, True)
        return fn
    return inner if fn is None else inner(fn)

def post_effect(fn: Callable[..., None]) -> Callable[..., None]:
    setattr(fn, DECORATOR_ATTR_POST_EFFECT, True)
    return fn