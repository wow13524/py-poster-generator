from type_utils import PropertyDict
from typing import Any,Dict,Type

LogicContent = Dict[str,Any]

class RawExpression(PropertyDict):
    action: str

    def __init__(self,data: Dict[str,Any],path: str) -> None:
        super().__init__(data,path)
        self._raw = data
    
    @property
    def raw(self) -> Dict[str,Any]:
        return self._raw

class Expression(PropertyDict):
    def __init__(self,expressions: Dict[str,Type['Expression']],raw: Dict[str,Any]) -> None:
        super().__init__(raw,self.__class__.__name__)

    def evaluate(self: 'Expression',context: LogicContent) -> Any:
        pass

def parse_expression(expressions: Dict[str,Type[Expression]],raw_expression: RawExpression) -> Expression:
    return expressions[raw_expression.action](expressions,raw_expression.raw)