from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplateMetaArg:
    name_or_flags: Union[str, List[str]]
    nargs: Optional[Union[int, str]] = None
    default: Optional[Any] = None
    type: Optional[str] = None
    required: Optional[bool] = None
    help: Optional[str] = None
    metavar: Optional[str] = None
    dest: Optional[str] = None

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplateMeta:
    name: str
    cli_args: List[PosterTemplateMetaArg] = field(default_factory=list)
    required_plugins: List[str] = field(default_factory=list)
    width: int
    height: int

@dataclass(frozen=True,kw_only=True,slots=True)
class PosterTemplate:
    meta: PosterTemplateMeta
    logic: List[Dict[str, Any]] = field(default_factory=list)
    content: List[Dict[str, Any]] = field(default_factory=list)