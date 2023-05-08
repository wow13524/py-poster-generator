from .expression import Expression
from .raw_object import RawContent, RawObject
from pyvips import Image
from typing import Callable, Dict, Type, cast

ElementType = Type['Element']

class RawElement(RawObject):
    type: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Element(Expression, RawElement):
    def __init__(self, raw_element: RawElement, children: Dict[str, 'Element']) -> None:
        RawElement.__init__(self, raw_element.raw)
        self._children = children

    evaluate = cast(Callable[..., Image], None)