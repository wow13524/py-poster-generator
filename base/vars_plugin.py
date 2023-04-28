from plugin_api import ContextProvider,Expression,Plugin,RawExpression,parse_expression
from typing import Any,Dict,Type

class Vars(Plugin):
    def context(self) -> Any:
        return {}

@Vars.expression
class Get(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self,context_provider: ContextProvider) -> Any:
        return context_provider.get(self)[self._name]

@Vars.expression
class Set(Expression):
    name: str
    value: RawExpression

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
        self._value = parse_expression(expressions,self.value)
    
    def evaluate(self,context_provider: ContextProvider) -> Any:
        context_provider.get(self)[self._name] = self._value.evaluate(context_provider)