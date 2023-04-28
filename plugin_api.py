from type_utils import PropertyDict
from typing import Any,Dict,Generator,List,Tuple,Type

ExpressionType = Type['Expression']
PluginType = Type['Plugin']
PluginTypeList = List[PluginType]

class RawObject(PropertyDict):
    def __init__(self,data: Dict[str,Any],path: str) -> None:
        super().__init__(data,path)
        self._raw = data
    
    @property
    def raw(self) -> Dict[str,Any]:
        return self._raw
    
    def __iter__(self) -> Generator[Tuple[str,Any],None,None]:
        for key,value in self.raw.items():
            yield key,value

class RawExpression(RawObject):
    action: str

class Expression(RawExpression):
    def __init__(self,expressions: Dict[str,ExpressionType],raw: Dict[str,Any]) -> None:
        super().__init__(raw,self.__class__.__name__)

    def evaluate(self: 'Expression',context_provider: 'ContextProvider') -> Any:
        pass

    @property
    def plugin(self) -> PluginType:
        return getattr(self.__class__,"_plugin")

class RawElement(RawObject):
    type: str

def parse_expression(expressions: Dict[str,ExpressionType],raw_expression: RawExpression) -> Expression:
    return expressions[raw_expression.action](expressions,raw_expression.raw)

class Plugin:
    @classmethod
    def expression(cls: PluginType,expression: ExpressionType) -> ExpressionType:
        assert cls is not __class__, "expressions should be registered using @PLUGIN_CLASS.expression, not @Plugin.expression"
        assert not hasattr(expression,"_plugin"), f"expression already registered under {getattr(expression,'_plugin').__name__}"
        setattr(expression,"_plugin",cls)

        if not hasattr(cls,"_expressions"):
            setattr(cls,"_expressions",[])
        expressions: List[ExpressionType] = getattr(cls,"_expressions")
        expressions.append(expression)
        return expression
    
    def context(self) -> Any:
        pass
    
    @property
    def expressions(self) -> List[ExpressionType]:
        return getattr(self.__class__,"_expressions",[])

class ContextProvider:
    def __init__(self,plugins: List[Plugin]) -> None:
        self._contexts = {plugin.__class__: plugin.context() for plugin in plugins}
    
    def get(self,expression: Expression) -> Any:
        plugin: PluginType = getattr(expression.__class__,"_plugin")
        assert plugin in self._contexts,f"expression {expression.__class__.__name__} depends on plugin {plugin.__name__} which is not present in this context"
        return self._contexts[plugin]
    
    def set(self,plugin: PluginType,data: Any) -> None:
        self._contexts[plugin] = data