from importlib import import_module
from inspect import get_annotations, getmembers, isclass, Parameter, signature
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast
from .api.models import Element, Expression, Plugin
from .models import RawObject

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]
IGNORE_ANNOTATIONS = [
    "self",
    "context",
    "return"
]

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

    def evaluate(self, obj: Expression[T, Any]) -> T:
        raw_fields = cast(Dict[str, Any], getattr(obj, "_fields"))
        evaluated_fields = {
            field: self.evaluate(cast(Expression[Any, Any], value)) if isinstance(value, Expression) else value
            for field,value in raw_fields.items()
        }
        return obj.evaluate(context=self._get_context(obj.__class__), **evaluated_fields)

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
                    
                    elements: set[Type[Element[Any]]] = getattr(plugin_class, "_elements")
                    expressions: set[Type[Expression[Any, Any]]] = getattr(plugin_class, "_expressions")
                    for expression_class in elements.union(expressions):
                        expression_name = f"{plugin_class.__name__}.{expression_class.__name__}"
                        if expression_name in self._expression_name_map:
                            raise Exception(f"Duplicate '{expression_name}' found")
                        self._expression_name_map[expression_name] = expression_class
    
    def new_active_context(self) -> ActiveContext:
        return ActiveContext(self._plugin_map)
    
    def _is_raw_object(self, raw_value: Any) -> bool:
        if type(raw_value) != dict:
            return False
        value = cast(Dict[str, Any], raw_value)
        if type(value.get("type")) != str:
            return False
        if type(value.get("args")) != dict:
            return False
        if not any(type(k) == str for k in cast(Dict[Any, Any], value["args"])):
            return False
        return True

    def _parse_raw_object(self, raw_obj: RawObject, obj_type: Type[V]) -> V:
        obj_class: Optional[Type[V]] = cast(Optional[Type[V]], self._expression_name_map.get(raw_obj.type))
        if obj_class is None:
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_obj.type}': does not exist")
        elif not issubclass(obj_class, obj_type):
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_obj.type}': is not an {obj_type.__name__}")
        annotations = get_annotations(obj_class.evaluate)
        for field in IGNORE_ANNOTATIONS:
            if field in annotations:
                del annotations[field]
        args_fields = {
            field: self._parse_raw_object(RawObject(**value), obj_type) if self._is_raw_object(value) else value
            for field,value in raw_obj.args.items()
        }
        fields = {
            **{
                field: value.default for field,value in signature(obj_class.evaluate).parameters.items()
                if value.default is not Parameter.empty
            },
            **args_fields
        }
        missing_keys = [key for key in annotations.keys() if key not in fields]
        if any(missing_keys):
            raise Exception(f"Cannot parse {obj_class.__name__} with missing keys {missing_keys}")

        obj = obj_class()
        setattr(obj, "_fields", fields)
        return obj
    
    def parse_element(self, raw_obj: RawObject) -> Element[Any]:
        return self._parse_raw_object(raw_obj, Element)
    
    def parse_expression(self, raw_obj: RawObject) -> Expression[Any, Any]:
        return self._parse_raw_object(raw_obj, Expression)