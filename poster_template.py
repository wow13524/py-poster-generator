import argparse
import importlib
import type_utils
from plugin_api import Expression,ExpressionType,Plugin,PluginType,RawExpression,parse_expression
from typing import Any,Dict,List,Optional,Type,Union

CACHED_PLUGINS: Dict[PluginType,Plugin] = {}
DEFAULT_REQUIRED: List[str] = [
    "base"
]

class PosterTemplateMetaArg(type_utils.PropertyDict):
    name_or_flags: Union[str,List[str]]
    nargs: Optional[Union[int,str]]
    default: Optional[Any]
    type: Optional[str]
    required: Optional[bool]
    help: Optional[str]
    metavar: Optional[str]
    dest: Optional[str]

class PosterTemplateMeta(type_utils.PropertyDict):
    name: str
    args: List[PosterTemplateMetaArg]
    required: List[str]
    width: int
    height: int

class PosterTemplateModel(type_utils.PropertyDict):
    meta: PosterTemplateMeta
    logic: List[RawExpression]

def _get_plugin(plugin_name: str) -> Plugin:
    module: Any = importlib.import_module(plugin_name)
    plugin: PluginType = getattr(module,"export_plugin")
    assert issubclass(plugin,Plugin), f"{plugin_name} is not a subclass of Plugin"
    if plugin not in CACHED_PLUGINS:
        CACHED_PLUGINS[plugin] = plugin()
    return CACHED_PLUGINS[plugin]

def _get_required_expressions(required: List[str]) -> Dict[str,Type[Expression]]:
    expressions: Dict[str,Type[Expression]] = {}
    required = DEFAULT_REQUIRED + required
    for plugin_name in required:
        plugin: Plugin = _get_plugin(plugin_name)
        expressions = {**expressions, **{
            f"{plugin.__class__.__name__}.{expression.__qualname__}": expression for expression in plugin.expressions
        }}
    return expressions

def _parse_logic(plugins: List[Plugin],raw_expressions: List[RawExpression]) -> List[Expression]:
    expression_map: Dict[str,ExpressionType] = {}
    for plugin in plugins:
        expression_map.update({f"{plugin.__class__.__name__}.{expression.__qualname__}": expression for expression in plugin.expressions})
    return [parse_expression(expression_map,raw_expression) for raw_expression in raw_expressions]

class PosterTemplate:
    def __init__(self,model: PosterTemplateModel) -> None:
        expressions: Dict[str,Type[Expression]] = _get_required_expressions(model.meta.required)
        print(expressions)
        self._model = model
        self._plugins = [_get_plugin(plugin_name) for plugin_name in DEFAULT_REQUIRED+model.meta.required]
        self._logic = _parse_logic(self._plugins,model.logic)
        self._parser: argparse.ArgumentParser = argparse.ArgumentParser(self.name)

        for arg in model.meta.args:
            name_or_flags: List[str] = arg.name_or_flags if isinstance(arg.name_or_flags,List) else [arg.name_or_flags]
            kwargs: Dict[str,Any] = {k:v for k,v in dict(arg).items() if v is not None}
            del kwargs["name_or_flags"]
            if arg.type:
                kwargs["type"] = type_utils.parse_type(arg.type)
            self._parser.add_argument(
                *name_or_flags,
                **kwargs
            )
    
    @property
    def name(self) -> str:
        return self._model.meta.name
    
    @property
    def width(self) -> int:
        return self._model.meta.width
    
    @property
    def height(self) -> int:
        return self._model.meta.height