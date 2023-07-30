from poster_generator.api import expression, Expression, Plugin
from typing import Dict

VarsContext = Dict[str, object]

class Get(Expression[object, VarsContext]):
    def evaluate(self, context: VarsContext, name: str) -> object:
        return context.get(name)

class Set(Expression[None, VarsContext]):
    def evaluate(self, context: VarsContext, name: str, value: object) -> None:
        context[name] = value

@expression(Get, Set)
class Vars(Plugin[VarsContext]):
    def new_context(self) -> VarsContext:
        return {}