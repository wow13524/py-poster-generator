from importlib import import_module
from inspect import getmembers, isclass
from typing import Any, Dict, List, Type
from .api.models import Element, Expression, Plugin

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]

class ActiveContext:
    def __init__(
        self,
        element_plugin_map: Dict[Type[Element], Type[Plugin]],
        expression_plugin_map: Dict[Type[Expression], Type[Plugin]],
        plugin_map: Dict[Type[Plugin], Plugin]
    ) -> None:
        self._element_plugin_map = element_plugin_map
        self._expression_plugin_map = expression_plugin_map
        self._context = {
            plugin_class: plugin.new_context()
            for plugin_class, plugin in plugin_map.items()
        }
    
    def update(self, plugin_class: Type[Plugin], context: Any) -> None:
        if plugin_class not in self._context:
            raise Exception(f"Could not update {__class__.__name__}: {plugin_class.__name__} is not included in this context")
        self._context[plugin_class] = context

class PluginContext:
    def __init__(self, required_plugins: List[str]) -> None:
        self._element_name_map: Dict[str, Type[Element]] = {}
        self._element_plugin_map: Dict[Type[Element], Type[Plugin]] = {}
        self._expression_name_map: Dict[str, Type[Expression]] = {}
        self._expression_plugin_map: Dict[Type[Expression], Type[Plugin]] = {}
        self._plugin_map: Dict[Type[Plugin], Plugin] = {}

        for module_name in required_plugins + DEFAULT_PLUGINS:
            try:
                module = import_module(module_name)
            except Exception as e:
                raise Exception(f"Failed to load plugin(s) from '{module_name}': {e}")
            
            for plugin_name, plugin_class in getmembers(module, isclass):
                if issubclass(plugin_class, Plugin):
                    try:
                        self._plugin_map[plugin_class] = plugin_class()
                    except Exception as e:
                        raise Exception(f"Failed to load plugin {plugin_name}.{plugin_name}: {e}")
                    
                    for element_class in plugin_class.elements:
                        self._element_name_map[element_class.__name__] = element_class
                        self._element_plugin_map[element_class] = plugin_class
                    
                    for expression_class in plugin_class.expressions:
                        self._expression_name_map[expression_class.__name__] = expression_class
                        self._expression_plugin_map[expression_class] = plugin_class
    
    def new_active_context(self) -> ActiveContext:
        return ActiveContext(self._element_plugin_map, self._expression_plugin_map, self._plugin_map)