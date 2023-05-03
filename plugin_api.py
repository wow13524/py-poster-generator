from PIL import Image
from type_utils import PropertyDict
from typing import Any,Dict,Generator,List,Tuple,Type

ElementType = Type['Element']
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
        self._evaluate = self.evaluate
        self.evaluate = self.safe_evaluate

    def evaluate(self,context_provider: 'ContextProvider') -> Any:
        pass

    def safe_evaluate(self,context_provider: 'ContextProvider') -> Any:
        try:
            return self._evaluate(context_provider)
        except:
            raise Exception(f"an exception occurred while evaluating expression: {self.raw}\ncurrent plugin context: {context_provider.get(self)}")

    @property
    def plugin(self) -> PluginType:
        return getattr(self.__class__,"_plugin")

class RawElement(RawObject):
    type: str
    position: Tuple[int,int] = (0,0)
    size: Tuple[int,int] = (64,64)
    rotation: float = 0

class Element(RawElement):
    def __init__(self,elements: Dict[str,ElementType],raw: Dict[str,Any]) -> None:
        super().__init__(raw,self.__class__.__name__)
        self._build = self.build
        self.build = self.safe_build
    
    def build(self,context_provider: 'ContextProvider') -> Image.Image:
        return Image.new("RGB",(0,0))
    
    def safe_build(self,context_provider: 'ContextProvider') -> Any:
        try:
            return self._build(context_provider)
        except:
            raise Exception(f"an exception occurred while building element: {self.raw}")

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