from importlib import import_module
from inspect import getmembers, isclass, Parameter
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast
from .api import Element, Expression, Plugin

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]

T = TypeVar("T")
V = TypeVar("V", bound=Union[Element[Any], Expression[Any, Any]])

class ActiveContext:
    def __init__(self, plugin_map: Dict[Type[Plugin[Any]], Plugin[Any]]) -> None:
        self._context = {
            plugin_class: plugin.new_context()
            for plugin_class, plugin in plugin_map.items()
        }
    
    def update(self, plugin_class: Type[Plugin[T]], context: T) -> None:
        if plugin_class not in self._context:
            raise Exception(f"Could not update {__class__.__name__}: {plugin_class.__name__} is not included in this context")
        self._context[plugin_class] = context
    
    def _get_context(self, expression_class: Type[Expression[Any, T]]) -> T:
        plugin_class: Type[Plugin[Any]] = getattr(expression_class, "_plugin")
        if plugin_class not in self._context:
            raise Exception(f"Could not get context for {expression_class.__name__}: parent plugin '{plugin_class.__name__}' is not part of this context")
        return self._context[plugin_class]

    def _evaluate_fields(self, obj: Expression[Any, Any]) -> Dict[str, Any]:
        raw_fields = cast(Dict[str, Any], getattr(obj, "_fields"))
        return {
            field: self.evaluate(cast(Expression[Any, Any], value)) if isinstance(value, Expression) else value
            for field,value in raw_fields.items()
        }

    def evaluate(self, obj: Expression[T, Any]) -> T:
        context: Any = self._get_context(obj.__class__)
        fields: Dict[str, Any] = self._evaluate_fields(obj)
        computed_fields: Dict[str, Any] = {
            fn.__name__: fn(obj, context=context, **fields)
            for fn in obj.get_compute_fields()
        }
        return obj.evaluate(context=context, **fields, **computed_fields)

class PluginContext:
    def __init__(self, required_plugins: List[str]) -> None:
        self._expression_name_map: Dict[str, Type[Expression[Any, Any]]] = {}
        self._plugin_map: Dict[Type[Plugin[Any]], Plugin[Any]] = {}

        for module_name in required_plugins + DEFAULT_PLUGINS:
            try:
                module = import_module(module_name)
            except Exception as e:
                raise Exception(f"Failed to load plugin(s) from '{module_name}': {e}")
            
            for plugin_name, plugin_class in getmembers(module, isclass):
                if issubclass(plugin_class, Plugin):
                    plugin_class = cast(Type[Plugin[Any]], plugin_class)
                    try:
                        self._plugin_map[plugin_class] = plugin_class()
                    except Exception as e:
                        raise Exception(f"Failed to load plugin {module_name}.{plugin_name}: {e}")
                    
                    expressions: set[Type[Expression[Any, Any]]] = getattr(plugin_class, "_expressions")
                    for expression_class in expressions:
                        expression_name = f"{plugin_class.__name__}.{expression_class.__name__}"
                        if expression_name in self._expression_name_map:
                            raise Exception(f"Duplicate '{expression_name}' found")
                        
                        self._expression_name_map[expression_name] = expression_class
    
    def new_active_context(self) -> ActiveContext:
        return ActiveContext(self._plugin_map)

    def _parse_raw_object(self, raw_obj: Dict[str, Any], obj_type: Type[V]) -> V:
        raw_type: Optional[str] = raw_obj.get("type")
        if raw_type is None:
            raise Exception(f"Raw {obj_type.__name__} is missing 'type' identifier")
        
        obj_class: Optional[Type[V]] = cast(Optional[Type[V]], self._expression_name_map.get(raw_type))
        if obj_class is None:
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_type}': plugin not imported")
        elif not issubclass(obj_class, obj_type):
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_type}': not an {obj_type.__name__}")
        
        required_fields: set[Parameter] = obj_class.get_required_fields()
        parsed_required_fields = {
            field.name: self._parse_raw_object(cast(Dict[str, Any], value), obj_type) if type(value := raw_obj.get(field.name)) == dict else value
            for field in required_fields
        }
        missing_keys = [key for key in required_fields if key not in required_fields]
        if any(missing_keys):
            raise Exception(f"Cannot parse {obj_class.__name__} with missing keys {missing_keys}")

        obj = obj_class()
        setattr(obj, "_fields", parsed_required_fields)
        return obj
    
    def parse_element(self, raw_obj: Dict[str, Any]) -> Element[Any]:
        return cast(Element[Any], self._parse_raw_object(raw_obj, Element))
    
    def parse_expression(self, raw_obj: Dict[str, Any]) -> Expression[Any, Any]:
        return cast(Expression[Any, Any], self._parse_raw_object(raw_obj, Expression))