from types import NoneType
from typing import Any, List, Tuple, TypeVar

from PIL import Image
from poster_generator.api import Element, Plugin, REQUIRED, element,  field

UiContext = NoneType
T = TypeVar("T")

class ChildrenComponent:
    @field(forward=True)
    def children(self, *, context: Any, children: List[Tuple[Image.Image, Tuple[int, int]]]=REQUIRED) -> List[Tuple[Image.Image, Tuple[int, int]]]:
        return children
    
    @staticmethod
    def apply_children(base: Image.Image, children: List[Tuple[Image.Image, Tuple[int, int]]]) -> None:
        for child,box in children:
            base.paste(im=child, box=box)

class SizeComponent:
    @field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=REQUIRED, width: float=REQUIRED, height: float=REQUIRED) -> Tuple[int, int]:
        return (int(size[0] * width), int(size[1] * height))

class Canvas(Element[UiContext], ChildrenComponent, SizeComponent):
    _width: int
    _height: int

    def __init__(self, width: int=-1, height: int=-1, children: List[Element[Any]]=[]) -> None:
        assert width >= 0, "Cannot include a Canvas in a template"
        self._fields = {"children": children}
        self._width = width
        self._height = height
    
    @field(forward=True)
    def size(self, *, context: UiContext) -> Tuple[int, int]:
        return (self._width, self._height)

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED, children: List[Tuple[Image.Image, Tuple[int, int]]]=REQUIRED) -> Tuple[Image.Image, Tuple[int, int]]:
        base: Image.Image = Image.new(mode="RGB", size=size)
        self.apply_children(base, children)
        return (base, (0, 0))

@element(Canvas)
class Ui(Plugin[UiContext]):
    def new_context(self) -> UiContext:
        return None