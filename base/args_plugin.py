from plugin_api import ContextProvider,Expression,Plugin
from typing import Any,Dict,Type

class Args(Plugin):
    pass

@Args.expression
class Get(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self,context_provider: ContextProvider) -> Any:
        return context_provider.get(self)[self._name]