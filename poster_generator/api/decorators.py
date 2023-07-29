from .models import Element, Expression, Plugin
from typing import Any, Callable, Type, TypeVar

T = TypeVar("T")

def element(*element_classes: Type[Element[T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    def decorator(plugin_class: Type[Plugin[T]]) -> Type[Plugin[T]]:
        if not plugin_class.elements:
            plugin_class.elements = set(element_classes)
        else:
            plugin_class.elements.union(element_classes)
        return plugin_class
    return decorator

def expression(*expression_classes: Type[Expression[Any, T]]) -> Callable[[Type[Plugin[T]]], Type[Plugin[T]]]:
    def decorator(plugin_class: Type[Plugin[T]]) -> Type[Plugin[T]]:
        if not plugin_class.expressions:
            plugin_class.expressions = set(expression_classes)
        else:
            plugin_class.expressions.union(expression_classes)
        return plugin_class
    return decorator