from importlib import import_module
from inspect import Parameter, getmembers, isclass
from typeguard import check_type
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast, get_args, get_origin
from .active_context import ActiveContext
from .api import Element, Expression, Plugin

T = TypeVar("T")

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]

uname_str: Callable[[type], str] = lambda callable: callable.__name__

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
    
    def _parse_raw_object(self, raw_obj: Any, obj_type: Type[T]) -> T:
        obj: Any
        type_origin: Optional[type] = get_origin(obj_type)
        type_args: Tuple[type, ...] = get_args(obj_type)
        type_error: str = f"""Expected type {uname_str(obj_type)}{f"[{', '.join(map(uname_str, type_args))}]" if type_args else ""}, got {uname_str(type(raw_obj))}"""
        if type(raw_obj) == list:
            assert check_type(cast(Any, raw_obj), list, typecheck_fail_callback=None), type_error
            obj = [self._parse_raw_object(v, Union[cast(Any, type_args)[0], Expression[Any, Any]]) for v in cast(List[Any], raw_obj)]
        elif type(raw_obj) == dict:
            raw_dict = cast(Dict[str, Any], raw_obj)
            if "@type" in raw_dict:
                raw_type: str = raw_dict["@type"]
                obj_class: Optional[Type[Expression[Any, Any]]] = self._expression_name_map.get(raw_type)
                assert obj_class is not None, f"Plugin containing '{obj_class}' not imported"
                required_fields: set[Parameter] = obj_class.get_required_fields()
                parsed_required_fields: Dict[str, Any] = {}
                for param in obj_class.get_allowed_fields():
                    try:
                        parsed_required_fields[param.name] = self._parse_raw_object(raw_dict.get(param.name), Union[param.annotation, Expression[Any, Any]])
                    except Exception as e:
                        raise Exception(f"Failed to parse field '{param.name}': {e}")
                missing_keys: List[str] = [param.name for param in required_fields if param.name not in parsed_required_fields]
                assert not any(missing_keys), f"Missing keys {missing_keys}"
                obj = obj_class()
                setattr(obj, "_fields", parsed_required_fields)
            else:
                assert type_origin == dict, type_error
                obj = {
                    key: self._parse_raw_object(value, Union[cast(Any, type_args)[1], Expression[Any, Any]])
                    for key,value in raw_dict.items()
                }
        else:
            obj = raw_obj
        try:
            return check_type(obj, obj_type)
        except Exception as e:
            raise Exception(type_error+"\n"+str(e))
    
    def new_active_context(self) -> ActiveContext:
        return ActiveContext(self._plugin_map)
    
    def parse_content(self, content: List[Dict[str, Any]]) -> List[Element[Any]]:
        parsed: List[Element[Any]] = []
        for i, raw_obj in enumerate(content):
            try:
                parsed.append(self._parse_raw_object(raw_obj, Element[Any]))
            except Exception as e:
                raise Exception(f"Failed to parse content[{i}]: {e}")
        return parsed
    
    def parse_logic(self, logic: List[Dict[str, Any]]) -> List[Expression[Any, Any]]:
        parsed: List[Expression[Any, Any]] = []
        for i, raw_obj in enumerate(logic):
            try:
                parsed.append(self._parse_raw_object(raw_obj, Expression[Any, Any]))
            except Exception as e:
                raise Exception(f"Failed to parse logic[{i}]: {e}")
        return parsed