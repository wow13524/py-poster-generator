from plugin_api import Expression,LogicContent,Plugin
from typing import Any,Dict,Type

class Args(Plugin):
    pass

@Args.expression
class Get(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self,context: LogicContent) -> Any:
        return context[self._name]