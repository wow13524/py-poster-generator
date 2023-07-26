from poster_generator.api import expression, Expression, Plugin
from typing import Any, Dict

VarsContext = Dict[str, Any]

class Get(Expression):
    def evaluate(self, context: VarsContext, name: str) -> Any:
        return context.get(name)

class Set(Expression):
    def evaluate(self, context: VarsContext, name: str, value: Any) -> None:
        context[name] = value

@expression(Get, Set)
class Vars(Plugin):
    def new_context(self) -> Any:
        return {}