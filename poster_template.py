import argparse
import importlib
import type_utils
from plugin_api import RawExpression,Expression,parse_expression
from typing import Any,Dict,List,Optional,Type,Union

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

def _get_required_expressions(required: List[str]) -> Dict[str,Type[Expression]]:
    expressions: Dict[str,Type[Expression]] = {}
    required = DEFAULT_REQUIRED + required
    for plugin_name in required:
        module: Any = importlib.import_module(plugin_name)
        if hasattr(module,"plugin_expressions"):
            expressions = {**expressions, **{
                f"{module.__name__}.{expression.__qualname__}": expression for expression in module.plugin_expressions
            }}
    return expressions

class PosterTemplate:
    def __init__(self,model: PosterTemplateModel) -> None:
        expressions: Dict[str,Type[Expression]] = _get_required_expressions(model.meta.required)
        print(expressions)
        self._model = model
        self._logic = [parse_expression(expressions,raw_expression) for raw_expression in model.logic]
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