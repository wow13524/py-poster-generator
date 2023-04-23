from plugin_api import Expression,LogicContent,Plugin,RawExpression,parse_expression
from typing import Any,Dict,Type

class Vars(Plugin):
    pass

@Vars.expression
class Get(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self,context: LogicContent) -> Any:
        return context[self._name]

@Vars.expression
class Set(Expression):
    name: str
    value: RawExpression

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
        self._value = parse_expression(expressions,self.value)
    
    def evaluate(self,context: LogicContent) -> Any:
        context[self._name] = self._value.evaluate(context)