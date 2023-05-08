from .raw_object import RawContent, RawObject
from typing import Any, Callable, Dict, Type, TypeVar, cast

ExpressionType = Type['Expression']
TExpression = TypeVar("TExpression", bound='Expression')

class RawExpression(RawObject):
    action: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Expression(RawExpression):
    _ignore_annotations = [ #Untyped to avoid explicit expression parsing; TODO fix in type_utils.py
        "context",
        "return",
        "self"
    ]

    @classmethod
    def annotations(cls: ExpressionType) -> Dict[str, type]:
        return {
            key: value for key, value in cls.evaluate.__annotations__.items()
            if key not in cls._ignore_annotations
        }
    
    @classmethod
    def requires_context(cls: ExpressionType) -> bool:
        return "context" in cls.evaluate.__annotations__

    def __init__(self, raw_expression: RawExpression, children: Dict[str, TExpression]) -> None:
        super().__init__(raw_expression.raw, raw_expression.action)
        self._children = children
    
    @property
    def children(self: TExpression) -> Dict[str, TExpression]:
        return cast(Dict[str, TExpression], self._children)

    evaluate = cast(Callable[..., Any], None)