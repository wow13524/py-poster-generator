from .raw_object import RawContent, NestedObject, RawObject
from pyvips import Image
from typing import Any, Callable, Dict, Type, cast

ElementType = Type['Element']

class RawElement(RawObject):
    type: str

    def __init__(self, raw: RawContent, path: str = "") -> None:
        super().__init__(raw, path or self.__class__.__name__)

class Element(NestedObject, RawObject):
    @classmethod
    def _target(cls: Type['Element']) -> Callable[..., Any]:
        return cls.render

    def __init__(self, raw_element: RawElement, children: Dict[str, 'Element']) -> None:
        NestedObject.__init__(self, children)
        RawObject.__init__(self, raw_element.raw, raw_element.type)

    render = cast(Callable[..., Image], None)