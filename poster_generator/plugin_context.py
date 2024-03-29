from importlib import import_module
from inspect import Parameter, getmembers, isclass
from typeguard import CollectionCheckStrategy, check_type
from typing import Any, Dict, List, Optional, Tuple, Type, Union, cast, get_args, get_origin
from .active_context import ActiveContext
from .api import Element, Expression, Plugin, EXPRESSION_SPECIAL_TYPE

DEFAULT_PLUGINS = ["poster_generator.core_plugins"]

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
    
    #Optional[Union[str, List[str]]]
    
    @staticmethod
    def _make_type_expression_safe(typ: type) -> type:
        if (origin := get_origin(typ)):
            args = [PluginContext._make_type_expression_safe(arg) for arg in get_args(typ)]
            return Union[typ, origin[*args], Expression[typ, Any]]
        return Union[typ, Expression[typ, Any]]

    def _parse_raw_object(self, raw_obj: Any, obj_type: type) -> Any:
        to_check_type: type = self._make_type_expression_safe(obj_type)
        type_origin: Optional[type] = get_origin(obj_type)
        type_args: Tuple[type, ...] = get_args(obj_type)
        if type(raw_obj) == list:
            raw_list: List[Any] = raw_obj
            obj = [self._parse_raw_object(v, type_args[0] if type_origin is list else Any) for v in raw_list]
        elif type(raw_obj) == dict:
            raw_dict: Dict[str, Any] = raw_obj
            if EXPRESSION_SPECIAL_TYPE in raw_dict:
                raw_type: str = raw_dict[EXPRESSION_SPECIAL_TYPE]
                obj_class: Optional[Type[Expression[Any, Any]]] = self._expression_name_map.get(raw_type)
                assert obj_class is not None, f"Plugin containing {EXPRESSION_SPECIAL_TYPE}='{raw_type}' not imported"
                required_fields: set[Parameter] = obj_class.get_required_fields()
                parsed_fields: Dict[str, Any] = {}
                for param in obj_class.get_allowed_fields():
                    try:
                        parsed_fields[param.name] = self._parse_raw_object(raw_dict.get(param.name, param.default), param.annotation)
                    except Exception as e:
                        raise Exception(f"Failed to parse field '{param.name}': {e}")
                missing_fields: List[str] = [param.name for param in required_fields if param.name not in parsed_fields]
                assert not any(missing_fields), f"Missing required fields {missing_fields}"
                obj = obj_class()
                setattr(obj, "_fields", parsed_fields)
            else:
                obj = {
                    key: self._parse_raw_object(value, type_args[1] if type_origin is dict else Any)
                    for key,value in raw_dict.items()
                }
        else:
            obj = raw_obj
        try:
            return check_type(obj, to_check_type, collection_check_strategy=CollectionCheckStrategy.ALL_ITEMS)
        except Exception as e:
            raise Exception(f"Expected type {obj_type}, got {type(cast(Any, raw_obj))}, due to Typeguard Exception:\n"+str(e))
    
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