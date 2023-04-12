import argparse
import type_utils
from typing import Any,Dict,List,Optional,Union,cast

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
    width: int
    height: int

class PosterTemplateModel(type_utils.PropertyDict):
    meta: PosterTemplateMeta

class PosterTemplate:
    def __init__(self,model: PosterTemplateModel) -> None:
        self._model = model
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
    
    