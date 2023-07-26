from poster_generator.api import expression, Expression, Plugin
from typing import Any, Dict

ArgsContext = Dict[str, Any]

class Get(Expression):
    def evaluate(self, context: ArgsContext, key: str) -> Any:
        return context.get(key)

@expression(Get)
class Args(Plugin):
    def new_context(self) -> Any:
        return {}