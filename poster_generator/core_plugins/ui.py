from types import NoneType
from typing import Any, List, Literal, Optional, Tuple, TypeVar
from PIL import Image
from poster_generator.api import Element, Expression, Plugin, REQUIRED, compute_field, element, expression, post_effect

UiContext = NoneType
T = TypeVar("T")

def to_pixels(size: int, dim: Tuple[int, float]) -> int:
    return int(dim[0] + size * dim[1] / 100.)

class Dimension(Expression[Tuple[int, float], UiContext]):
    def evaluate(self, *, context: UiContext, px: int=0, percent: float=0) -> Tuple[int, float]:
        return (px, percent)

class ChildrenComponent:
    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None) -> None:
        if children:
            for child in children:
                evaluated.alpha_composite(im=child, dest=child.info.get("position", (0, 0)))

class PositionComponent:
    @post_effect
    def apply_position(self, *, context: Any, evaluated: Image.Image, parent_size: Tuple[int, int]=REQUIRED, left: Tuple[int, float]=(0, 0), top: Tuple[int, float]=(0, 0)) -> None:
        evaluated.info.update({"position": (to_pixels(parent_size[0], left), to_pixels(parent_size[1], top))})

class SizeComponent:
    @compute_field(forward=True)
    def parent_size(self, *, context: Any, size: Tuple[int, int]=(-1, -1)) -> Tuple[int, int]:
        return self.size(context=context, size=size, width=(0, 100), height=(0, 100))

    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: Tuple[int, float]=(0, 0), height: Tuple[int, float]=(0, 0)) -> Tuple[int, int]:
        assert size != (-1, -1), f"Parent Element did not forward 'size' field, does it subclass {__class__.__name__}?"
        return (to_pixels(size[0], width), to_pixels(size[1], height))

class Canvas(Element[UiContext], ChildrenComponent, SizeComponent):
    def __init__(self, width: int=-1, height: int=-1, children: List[Element[Any]]=[]) -> None:
        assert width >= 0, "Cannot include a Canvas in a template"
        self._fields = {
            "size": (width, height),
            "width": (0, 100),
            "height": (0, 100),
            "children": children
        }

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

class Container(Element[UiContext], ChildrenComponent, PositionComponent, SizeComponent):
    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED, background_color: Tuple[int, ...]=(0, 0, 0, 0)) -> Image.Image:
        return Image.new(mode="RGBA", size=size, color=background_color)

class ListLayout(Element[UiContext], SizeComponent):
    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: Tuple[int, float]=(0, 100), height: Tuple[int, float]=(0, 100)) -> Tuple[int, int]:
        return SizeComponent.size(self, context=context, size=size, width=width, height=height)

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None, direction: Literal["horizontal", "vertical"]="vertical", spacing: Tuple[int, float]=(0, 0)) -> None:
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
@expression(
    Dimension
)
class Ui(Plugin[UiContext]):
    def new_context(self) -> UiContext:
        return None