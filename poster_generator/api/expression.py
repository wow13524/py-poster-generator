from .raw_object import RawContent, RawObject
from typing import Any, Callable, Dict, Generator, Type, cast

ExpressionType = Type['Expression']
ParseGenerator = Generator[RawContent, 'Expression', None]

class RawExpression(RawObject):
    action: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Expression(RawExpression):
    @classmethod
    def annotations(cls: ExpressionType) -> Dict[str, type]:
        annotations: Dict[str, type] = cls.evaluate.__annotations__.copy()
        if "self" in annotations:
            del annotations["self"]
        if "context" in annotations:
            del annotations["context"]
        if "return" in annotations:
            del annotations["return"]
        return annotations
    
    @classmethod
    def requires_context(cls: ExpressionType) -> bool:
        return "context" in cls.evaluate.__annotations__

    def __init__(self, raw: RawContent, children: Dict[str, 'Expression']) -> None:
        super().__init__(raw)
        self._children = children
    
    @property
    def children(self) -> Dict[str, 'Expression']:
        return self._children

    evaluate = cast(Callable[[Any], Any], None)