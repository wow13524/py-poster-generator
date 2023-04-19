import importlib
import type_utils
from argparse import ArgumentParser
from plugin_api import Expression,ExpressionType,Plugin,PluginType,RawExpression,parse_expression
from typing import Any,Dict,List,Optional,Union

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

def _get_plugin(plugin_name: str) -> List[Plugin]:
    module: Any = importlib.import_module(plugin_name)
    plugins: List[PluginType] = getattr(module,"export_plugins")
    assert type(plugins) == list, f"{plugin_name} missing list 'export_plugins'"
    for plugin in plugins:
        assert issubclass(plugin,Plugin), f"{plugin_name} is not a subclass of Plugin"
        if plugin not in CACHED_PLUGINS:
            CACHED_PLUGINS[plugin] = plugin()
    return [CACHED_PLUGINS[plugin] for plugin in plugins]

def _parse_logic(plugins: List[Plugin],raw_expressions: List[RawExpression]) -> List[Expression]:
    expression_map: Dict[str,ExpressionType] = {}
    for plugin in plugins:
        expression_map.update({f"{plugin.__class__.__name__}.{expression.__qualname__}": expression for expression in plugin.expressions})
    return [parse_expression(expression_map,raw_expression) for raw_expression in raw_expressions]

class PosterTemplate:
    def __init__(self,model: PosterTemplateModel) -> None:
        self._model = model
        self._plugins = [plugin for plugin_name in DEFAULT_REQUIRED+model.meta.required  for plugin in _get_plugin(plugin_name)]
        self._logic = _parse_logic(self._plugins,model.logic)
        self._parser: ArgumentParser = ArgumentParser(self.name)

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
    
    @property
    def logic(self) -> List[Expression]:
        return self._logic

    @property
    def parser(self) -> ArgumentParser:
        return self._parser
    
    @property
    def plugins(self) -> List[Plugin]:
        return self._plugins