from poster_generator.api import Expression, Plugin, expression
from typing import List

class Join(Expression):
    def evaluate(self,separator: str, value: List[str]) -> str:
        return separator.join(value)

@expression(Join)
class Str(Plugin):
    pass