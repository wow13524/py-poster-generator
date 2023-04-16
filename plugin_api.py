from type_utils import PropertyDict
from typing import Any,Dict,List,Type,TypeVar

LogicContent = Dict[Any,Any]
PluginType = Type['Plugin']
T = TypeVar("T",bound="Expression")

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

class Plugin:
    expressions: List[Type[Expression]] = []
    
    @staticmethod
    def expression(expression: Type[T]) -> Type[T]:
        __class__.expressions.append(expression)
        return expression
    
    def context(self) -> LogicContent:
        return {}