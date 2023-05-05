from poster_generator.api import Expression, Plugin, expression
from typing import Any, Dict

ArgsContext = Dict[str, Any]

class Get(Expression):
    name: str

    def evaluate(self, context: ArgsContext) -> Any:
        return context[self.name]

@expression(Get)
class Args(Plugin):
    def context(self) -> ArgsContext:
        return {}