from models import *
from typing import Callable, Type

def element(*element_classes: Type[Element]) -> Callable[[Type[Plugin]], Type[Plugin]]:
    def decorator(plugin_class: Type[Plugin]) -> Type[Plugin]:
        if not plugin_class.elements:
            plugin_class.elements = set(element_classes)
        else:
            plugin_class.elements.union(element_classes)
        return plugin_class
    return decorator

def expression(*expression_classes: Type[Expression]) -> Callable[[Type[Plugin]], Type[Plugin]]:
    def decorator(plugin_class: Type[Plugin]) -> Type[Plugin]:
        if not plugin_class.expressions:
            plugin_class.expressions = set(expression_classes)
        else:
            plugin_class.expressions.union(expression_classes)
        return plugin_class
    return decorator