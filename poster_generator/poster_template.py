from .api.expression import Expression, RawExpression
from .context_provider import PluginContext
from .type_utils import PropertyDict, parse_type
from argparse import ArgumentParser
from typing import Any, Dict, List, Optional, Union

class PosterTemplateMetaArg(PropertyDict):
    name_or_flags: Union[str, List[str]]
    nargs: Optional[Union[int, str]]
    default: Optional[Any]
    type: Optional[str]
    required: Optional[bool]
    help: Optional[str]
    metavar: Optional[str]
    dest: Optional[str]

class PosterTemplateMeta(PropertyDict):
    name: str
    args: List[PosterTemplateMetaArg]
    required: List[str]
    width: int
    height: int

class PosterTemplateModel(PropertyDict):
    meta: PosterTemplateMeta
    logic: List[RawExpression]

class PosterTemplate:
    def __init__(self, model: PosterTemplateModel) -> None:
        self._model: PosterTemplateModel = model
        self._plugin_context: PluginContext = PluginContext(model.meta.required)
        self._logic: List[Expression] = [self._plugin_context.parse_expression(raw_expression) for raw_expression in model.logic]
        self._parser: ArgumentParser = ArgumentParser(self.name)

        for arg in model.meta.args:
            name_or_flags: List[str] = arg.name_or_flags if isinstance(arg.name_or_flags,List) else [arg.name_or_flags]
            kwargs: Dict[str,Any] = {k:v for k,v in dict(arg).items() if v is not None and k != "name_or_flags"}
            if arg.type:
                kwargs["type"] = parse_type(arg.type)
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
    def plugin_context(self) -> PluginContext:
        return self._plugin_context