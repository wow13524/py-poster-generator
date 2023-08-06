from inspect import Parameter
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast
from .api import Expression, Plugin

T = TypeVar("T")

name_str: Callable[[Parameter], str] = lambda param: param.name
uname_str: Callable[[Callable[..., Any]], str] = lambda callable: callable.__name__

class ActiveContext:
    def __init__(self, plugin_map: Dict[Type[Plugin[Any]], Plugin[Any]]) -> None:
        self._context = {
            plugin_class: plugin.new_context()
            for plugin_class, plugin in plugin_map.items()
        }
    
    def _evaluate_fields(self, obj: Expression[Any, Any], evaluated: Dict[str, Any], filter_params: Optional[set[Parameter]]=None) -> Dict[str, Any]:
        raw_fields: Dict[str, Any] = getattr(obj, "_fields")
        filter_param_names: set[str] = set(map(name_str, filter_params or obj.get_allowed_fields()))
        to_forward_fields: set[Callable[..., Any]] = obj.get_forward_fields()
        to_forward_field_names: set[str] = set(map(uname_str, to_forward_fields))
        evaluated_to_forward_fields: Dict[str, Any] = {
            field: value
            for field,value in evaluated.items()
            if field in to_forward_field_names
        }
        evaluated_fields: Dict[str, Any] = {}
        for field,value in raw_fields.items():
            if field in filter_param_names and field not in evaluated:
                if type(value) == list:
                    value = [
                        self.evaluate(v, evaluated) if isinstance(v, Expression) else v
                        for v in cast(List[Union[Any, Expression[Any, Any]]], value)
                    ]
                elif type(value) == dict:
                    value = {
                        k: self.evaluate(v, evaluated) if isinstance(v, Expression) else v
                        for k,v in cast(Dict[str, Union[Any, Expression[Any, Any]]], value).items()
                    }
                elif isinstance(value, Expression):
                    value = self.evaluate(cast(Expression[Any, Any], value), evaluated_to_forward_fields)
                evaluated_fields[field] = value
        return evaluated_fields

    def _filter_fields(self, fn: Callable[..., Any], fields: Dict[str, Any]) -> Dict[str, Any]:
        allowed_fields: set[Parameter] = Expression.get_allowed_fields(fn)
        allowed_fields_names: set[str] = set(map(name_str, allowed_fields))
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
        post_effects: set[Callable[..., None]] = obj.get_post_effects()
        evaluated_fields: Dict[str, Any] = forwarded_fields.copy() if forwarded_fields else {}
        compute_required_fields: Dict[str, Any] = {**evaluated_fields, **self._evaluate_fields(obj, evaluated_fields, obj.get_allowed_fields(compute_fields))}
        for compute_field in compute_fields:
            evaluated_fields[uname_str(compute_field)] = compute_field(obj, context=context, **self._filter_fields(compute_field, compute_required_fields))
        evaluated_fields.update(self._evaluate_fields(obj, evaluated_fields))
        evaluated: T = obj.evaluate(context=context, **self._filter_fields(obj.evaluate, evaluated_fields))
        [fn(obj, context=context, evaluated=evaluated, **self._filter_fields(fn, evaluated_fields)) for fn in post_effects]
        return evaluated

    def update(self, plugin_class: Type[Plugin[T]], context: T) -> None:
        if plugin_class not in self._context:
            raise Exception(f"Could not update {__class__.__name__}: {plugin_class.__name__} is not included in this context")
        self._context[plugin_class] = context