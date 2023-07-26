from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from typing import Any, Dict, List, Optional, Union

@dataclass(frozen=True,kw_only=True,slots=True)
class RawObject(DataClassJsonMixin):
    type: str
    args: Dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplateMetaArg(DataClassJsonMixin):
    name_or_flags: Union[str, List[str]]
    nargs: Optional[Union[int, str]] = None
    default: Optional[Any] = None
    type: Optional[str] = None
    required: Optional[bool] = None
    help: Optional[str] = None
    metavar: Optional[str] = None
    dest: Optional[str] = None

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplateMeta(DataClassJsonMixin):
    name: str
    cli_args: List[PosterTemplateMetaArg] = field(default_factory=list)
    required_plugins: List[str] = field(default_factory=list)
    width: int
    height: int

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplate(DataClassJsonMixin):
    meta: PosterTemplateMeta
    logic: List[RawObject] = field(default_factory=list)
    content: List[RawObject] = field(default_factory=list)