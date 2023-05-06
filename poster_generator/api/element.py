from .raw_object import RawContent, RawObject
from typing import Any, Callable, Dict, Type, cast

ElementType = Type['Element']

class RawElement(RawObject):
    type: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Element(RawElement):
    @classmethod
    def annotations(cls: ElementType) -> Dict[str, type]:
        annotations: Dict[str, type] = cls.render.__annotations__.copy()
        if "self" in annotations:
            del annotations["self"]
        if "context" in annotations:
            del annotations["context"]
        if "return" in annotations:
            del annotations["return"]
        return annotations
    
    @classmethod
    def requires_context(cls: ElementType) -> bool:
        return "context" in cls.render.__annotations__

    def __init__(self, raw: RawContent, children: Dict[str, 'Element']) -> None:
        super().__init__(raw)
        self._children = children
    
    @property
    def children(self) -> Dict[str, 'Element']:
        return self._children

    render = cast(Callable[[Any], Any], None)