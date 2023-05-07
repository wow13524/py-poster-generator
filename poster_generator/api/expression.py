from .raw_object import RawContent, NestedObject, RawObject
from typing import Any, Callable, Dict, Type, cast

ExpressionType = Type['Expression']

class RawExpression(RawObject):
    action: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Expression(NestedObject, RawObject):
    @classmethod
    def _target(cls: Type['Expression']) -> Callable[..., Any]:
        return cls.evaluate
        
    def __init__(self, raw_expression: RawExpression, children: Dict[str, 'Expression']) -> None:
        NestedObject.__init__(self, children)
        RawObject.__init__(self, raw_expression.raw, raw_expression.action)

    evaluate = cast(Callable[..., Any], None)