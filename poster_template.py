import type_utils
from typing import Any,List,Optional,Union

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
    def __init__(self) -> None:
        pass