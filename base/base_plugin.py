from poster_generator.api import Element, Expression, Plugin, element, expression
from typing import Any

class Canvas(Element):
    pass

class Literal(Expression):
    value: Any

    def evaluate(self) -> Any:
        return self.value

@element(Canvas)
@expression(Literal)
class Base(Plugin):
    pass