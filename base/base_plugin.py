from plugin_api import Expression,LogicContent,Plugin
from typing import Any

class Base(Plugin):
    pass

@Base.expression
class Literal(Expression):
    value: Any
    
    def evaluate(self,context: LogicContent) -> Any:
        return self.value