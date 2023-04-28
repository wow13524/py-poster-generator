from plugin_api import ContextProvider,Expression,Plugin
from typing import Any

class Base(Plugin):
    pass

@Base.expression
class Literal(Expression):
    value: Any
    
    def evaluate(self,context_provider: ContextProvider) -> Any:
        return self.value