from plugin_api import AbstractExpression,Expression,parse_expression
from typing import Any,Dict,Type

class GetArg(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self) -> Any:
        return self._name

class Store(Expression):
    name: str
    value: AbstractExpression

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
        self._value = parse_expression(expressions,self.value)
    
    def evaluate(self) -> Any:
        return self._value.evaluate()