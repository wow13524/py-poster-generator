from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Dict

ArgsContext = Dict[str, object]

class Get(Expression[object, ArgsContext]):
    def evaluate(self, *, context: ArgsContext, key: str=REQUIRED) -> object:
        return context.get(key)

@expression(Get)
class Args(Plugin[ArgsContext]):
    def new_context(self) -> ArgsContext:
        return {}