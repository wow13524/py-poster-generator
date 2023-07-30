from .models import Element, Expression, Plugin
from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")

def element(*element_classes: Type[Element[T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    def decorator(plugin_class: Type[Plugin[T]]) -> Type[Plugin[T]]:
        for element_class in element_classes:
            setattr(element_class, "_plugin", plugin_class)
        elements: set[Type[Element[T]]] = getattr(plugin_class, "_elements")
        setattr(plugin_class, "_elements", elements.union(element_classes))
        return plugin_class
    return decorator

def expression(*expression_classes: Type[Expression[Any, T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    def decorator(plugin_class: Type[Plugin[T]]) -> Type[Plugin[T]]:
        for expression_class in expression_classes:
            setattr(expression_class, "_plugin", plugin_class)
        expressions: set[Type[Expression[Any, T]]] = getattr(plugin_class, "_elements")
        setattr(plugin_class, "_elements", expressions.union(expression_classes))
        return plugin_class
    return decorator