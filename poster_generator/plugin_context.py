from importlib import import_module
from inspect import getmembers, isclass, Parameter
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast
from .api import Element, Expression, Plugin

T = TypeVar("T")
U = TypeVar("U", bound=Union[Element[Any], Expression[Any, Any]])

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]

param_str: Callable[[Parameter], str] = lambda param: param.name
callable_str: Callable[[Callable[..., Any]], str] = lambda callable: callable.__name__

class ActiveContext:
    def __init__(self, plugin_map: Dict[Type[Plugin[Any]], Plugin[Any]]) -> None:
        self._context = {
            plugin_class: plugin.new_context()
            for plugin_class, plugin in plugin_map.items()
        }
    
    def _evaluate_fields(self, obj: Expression[Any, Any], evaluated: Dict[str, Any], filter_params: Optional[set[Parameter]]=None) -> None:
        raw_fields: Dict[str, Any] = getattr(obj, "_fields")
        filter_param_names: set[str] = set(map(param_str, filter_params or {}))
        forward_fields: set[Callable[..., Any]] = obj.get_forward_fields()
        forward_field_names: set[str] = set(map(callable_str, forward_fields))
        evaluated_forward_fields: Dict[str, Any] = {
            field: value
            for field,value in evaluated.items()
            if field in forward_field_names
        }
        evaluated.update({
            field: self.evaluate(cast(Expression[Any, Any], value), evaluated_forward_fields) if isinstance(value, Expression) else value
            for field,value in raw_fields.items() 
            if (filter_params is None or field in filter_param_names) and field not in evaluated
        })

    def _filter_fields(self, fn: Callable[..., Any], fields: Dict[str, Any]) -> Dict[str, Any]:
        allowed_fields: set[Parameter] = Expression.get_allowed_fields(fn)
        allowed_fields_names: set[str] = set(map(param_str, allowed_fields))
        return {
            field: value
            for field,value in fields.items()
            if field in allowed_fields_names
        }

    def _get_context(self, expression_class: Type[Expression[Any, T]]) -> T:
        plugin_class: Type[Plugin[Any]] = getattr(expression_class, "_plugin")
        if plugin_class not in self._context:
            raise Exception(f"Could not get context for {expression_class.__name__}: parent plugin '{plugin_class.__name__}' is not part of this context")
        return self._context[plugin_class]

    def evaluate(self, obj: Expression[T, Any], forwarded_fields: Optional[Dict[str, Any]]=None) -> T:
        context: Any = self._get_context(obj.__class__)
        compute_fields: set[Callable[..., Any]] = obj.get_compute_fields()
        evaluated_fields: Dict[str, Any] = forwarded_fields.copy() if forwarded_fields else {}

        self._evaluate_fields(obj, evaluated_fields, obj.get_allowed_fields(compute_fields))
        evaluated_fields.update({
            fn.__name__: fn(obj, context=context, **self._filter_fields(fn, evaluated_fields))
            for fn in compute_fields
        })

        self._evaluate_fields(obj, evaluated_fields)
        return obj.evaluate(context=context, **self._filter_fields(obj.evaluate, evaluated_fields))

    def update(self, plugin_class: Type[Plugin[T]], context: T) -> None:
        if plugin_class not in self._context:
            raise Exception(f"Could not update {__class__.__name__}: {plugin_class.__name__} is not included in this context")
        self._context[plugin_class] = context

class PluginContext:
    def __init__(self, required_plugins: List[str]) -> None:
        self._expression_name_map: Dict[str, Type[Expression[Any, Any]]] = {}
        self._plugin_map: Dict[Type[Plugin[Any]], Plugin[Any]] = {}

        for module_name in set(required_plugins + DEFAULT_PLUGINS):
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
    
    def _parse_raw_object(self, raw_obj: Dict[str, Any], obj_type: Type[U]) -> U:
        raw_type: Optional[str] = raw_obj.get("type")
        if raw_type is None:
            raise Exception(f"Raw {obj_type.__name__} is missing 'type' identifier")
        
        obj_class: Optional[Type[U]] = cast(Optional[Type[U]], self._expression_name_map.get(raw_type))
        if obj_class is None:
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_type}': plugin not imported")
        elif not issubclass(obj_class, obj_type):
            raise Exception(f"Failed to parse {obj_type.__name__} '{raw_type}': not an {obj_type.__name__}")
        
        required_fields: set[Parameter] = obj_class.get_required_fields()
        parsed_required_fields = {
            field: self._parse_raw_object(cast(Dict[str, Any], value), obj_type) if type(value) == dict else value
            for field,value in raw_obj.items()
        }
        missing_keys = [param.name for param in required_fields if param.name not in parsed_required_fields]
        if any(missing_keys):
            raise Exception(f"Cannot parse {obj_class.__name__} with missing keys {missing_keys}")

        obj = obj_class()
        setattr(obj, "_fields", parsed_required_fields)
        return obj
    
    def new_active_context(self) -> ActiveContext:
        return ActiveContext(self._plugin_map)
    
    def parse_element(self, raw_obj: Dict[str, Any]) -> Element[Any]:
        return cast(Element[Any], self._parse_raw_object(raw_obj, Element))
    
    def parse_expression(self, raw_obj: Dict[str, Any]) -> Expression[Any, Any]:
        return cast(Expression[Any, Any], self._parse_raw_object(raw_obj, Expression))