from poster_generator.api import Expression, Plugin, expression
from typing import Any

class Literal(Expression):
    value: Any

    def evaluate(self) -> Any:
        return self.value

@expression(Literal)
class Base(Plugin):
    pass