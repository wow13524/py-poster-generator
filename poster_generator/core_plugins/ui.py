from types import NoneType
from typing import Any, List, Literal, Optional, Tuple, TypeVar
from PIL import Image
from poster_generator.api import Element, Plugin, REQUIRED, compute_field, element, post_effect

UiContext = NoneType
T = TypeVar("T")

class ChildrenComponent:
    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None) -> None:
        if children:
            for child in children:
                evaluated.alpha_composite(im=child, dest=child.info.get("position", (0, 0)))

class PositionComponent:
    @post_effect
    def apply_position(self, *, context: Any, evaluated: Image.Image, parent_size: Tuple[int, int]=REQUIRED, left: float=0, top: float=0) -> None:
        evaluated.info.update({"position": (int(parent_size[0] * left), int(parent_size[1] * top))})

class SizeComponent:
    @compute_field(forward=True)
    def parent_size(self, *, context: Any, size: Tuple[int, int]=(-1, -1)) -> Tuple[int, int]:
        return self.size(context=context, size=size, width=1, height=1)

    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: float=REQUIRED, height: float=REQUIRED) -> Tuple[int, int]:
        assert size != (-1, -1), f"Parent Element did not forward 'size' field, does it subclass {__class__.__name__}?"
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

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

class Container(Element[UiContext], ChildrenComponent, PositionComponent, SizeComponent):
    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED, background_color: Tuple[int, ...]=(0, 0, 0, 0)) -> Image.Image:
        return Image.new(mode="RGBA", size=size, color=background_color)

class ListLayout(Element[UiContext], SizeComponent):
    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: float=1, height: float=1) -> Tuple[int, int]:
        return SizeComponent.size(self, context=context, size=size, width=width, height=height)

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None, direction: Literal["horizontal", "vertical"]="vertical") -> None:
        if children:
            offset: int = 0
            for child in children:
                evaluated.alpha_composite(im=child, dest=(offset, 0) if direction == "horizontal" else (0, offset))
                offset += child.width if direction == "horizontal" else child.height

@element(
    Canvas,
    Container,
    ListLayout
)
class Ui(Plugin[UiContext]):
    def new_context(self) -> UiContext:
        return None