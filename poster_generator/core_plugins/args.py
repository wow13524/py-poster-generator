from poster_generator.api import expression, Expression, Plugin
from typing import Any, Dict

ArgsContext = Dict[str, Any]

class Get(Expression[Any, ArgsContext]):
    def evaluate(self, context: ArgsContext, key: str) -> Any:
        return context.get(key)

@expression(Get)
class Args(Plugin[ArgsContext]):
    def new_context(self) -> ArgsContext:
        return {}