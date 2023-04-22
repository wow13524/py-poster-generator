from plugin_api import Expression,LogicContent,Plugin,RawExpression,parse_expression
from typing import Any,Dict,Type

class Base(Plugin):
    def context(self) -> LogicContent:
        return {
            "args": {},
            "vars": {}
        }

@Base.expression
class Literal(Expression):
    value: Any
    
    def evaluate(self,context: LogicContent) -> Any:
        return self.value

@Base.expression
class GetArg(Expression):
    name: str

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
    
    def evaluate(self,context: LogicContent) -> Any:
        return context["args"][self._name]

@Base.expression
class SetVar(Expression):
    name: str
    value: RawExpression

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._name = self.name
        self._value = parse_expression(expressions,self.value)
    
    def evaluate(self,context: LogicContent) -> Any:
        context["vars"][self._name] = self._value.evaluate(context)