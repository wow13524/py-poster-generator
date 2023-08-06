from types import NoneType
from typing import Any, List, Optional, Tuple, TypeVar
from PIL import Image
from poster_generator.api import Element, Plugin, REQUIRED, compute_field, element, post_effect

UiContext = NoneType
T = TypeVar("T")

class ChildrenComponent:
    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Tuple[Image.Image, Tuple[int, int]]]]=None) -> None:
        if children:
            for child,box in children:
                evaluated.paste(im=child, box=box)

class SizeComponent:
    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=REQUIRED, width: float=REQUIRED, height: float=REQUIRED) -> Tuple[int, int]:
        return (int(size[0] * width), int(size[1] * height))

class Canvas(Element[UiContext], ChildrenComponent, SizeComponent):
    def __init__(self, width: int=-1, height: int=-1, children: List[Element[Any]]=[]) -> None:
        assert width >= 0, "Cannot include a Canvas in a template"
        self._fields = {
            "size": (width, height),
            "width": 1,
            "height": 1,
            "children": children
        }

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Tuple[Image.Image, Tuple[int, int]]:
        base: Image.Image = Image.new(mode="RGB", size=size)
        return (base, (0, 0))

class Box(Element[UiContext], ChildrenComponent, SizeComponent):
    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Tuple[Image.Image, Tuple[int, int]]:
        base: Image.Image = Image.new(mode="RGB", size=size, color=(0, 255, 0))
        return (base, (0, 0))

@element(Box, Canvas)
class Ui(Plugin[UiContext]):
    def new_context(self) -> UiContext:
        return None