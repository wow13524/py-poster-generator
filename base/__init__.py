from .expressions import GetArg,SetVar
from plugin_api import Expression
from typing import List,Type

plugin_expressions: List[Type[Expression]] = [
    GetArg,
    SetVar
]