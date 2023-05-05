from poster_generator.api import Expression, Plugin, expression
from typing import Any, Dict

VarsContext = Dict[str, Any]

class Get(Expression):
    name: str

    def evaluate(self, context: VarsContext) -> Any:
        return context[self.name]

class Set(Expression):
    name: str
    
    def evaluate(self, context: VarsContext, value: Any) -> None:
        context[self.name] = value

@expression(Get)
@expression(Set)
class Vars(Plugin):
    def context(self) -> Any:
        return {}