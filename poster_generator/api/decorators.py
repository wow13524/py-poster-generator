from .models import Element, Expression, Plugin
from typing import Any, Callable, Type, TypeVar

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

def field(*, forward: bool=False) -> Callable[..., Any]:
    def inner(fn: Callable[..., T]) -> Callable[..., T]:
        setattr(fn, "_compute_field", True)
        if forward:
            setattr(fn, "_forward", True)
        return fn
    return inner