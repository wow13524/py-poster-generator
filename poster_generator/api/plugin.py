from .element import ElementType
from .expression import ExpressionType
from typing import Any, Callable, List, Type

PluginType = Type['Plugin']
PluginTypeList = List[PluginType]

def element(element_class: ElementType) -> Callable[[PluginType], PluginType]:
    def decorator(plugin_class: PluginType) -> PluginType:
        if not hasattr(plugin_class, "elements"):
            plugin_class.elements = []
        plugin_class.elements.append(element_class)
        return plugin_class
    return decorator

def expression(expression_class: ExpressionType) -> Callable[[PluginType], PluginType]:
    def decorator(plugin_class: PluginType) -> PluginType:
        if not hasattr(plugin_class, "expressions"):
            plugin_class.expressions = []
        plugin_class.expressions.append(expression_class)
        return plugin_class
    return decorator

class Plugin:
    elements: List[ElementType]
    expressions: List[ExpressionType]

    def context(self) -> Any:
        pass