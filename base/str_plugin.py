from plugin_api import Expression,LogicContent,Plugin,RawExpression,parse_expression
from typing import Any,Dict,Type

class Str(Plugin):
    pass

@Str.expression
class Join(Expression):
    separator: RawExpression
    value: RawExpression

    def __init__(self,expressions: Dict[str,Type[Expression]],raw: Dict[str,Any]) -> None:
        super().__init__(expressions,raw)
        self._separator = parse_expression(expressions,self.separator)
        self._value = parse_expression(expressions,self.value)
    
    def evaluate(self,context: LogicContent) -> Any:
        return self._separator.evaluate(context).join(self._value.evaluate(context))