from types import NoneType
from typing import Any, List, Literal, Optional, Tuple, TypeVar
from PIL import Image
from poster_generator.api import Element, Plugin, REQUIRED, compute_field, element, post_effect
from .data import Dimension
from .ui_components import ChildrenComponent, PositionComponent, SizeComponent

UiContext = NoneType
T = TypeVar("T")

class Canvas(Element[UiContext], ChildrenComponent, SizeComponent):
    def __init__(self, width: int=-1, height: int=-1, children: List[Element[Any]]=[]) -> None:
        assert width >= 0, "Cannot include a Canvas in a template"
        self._fields = {
            "size": (width, height),
            "width": Dimension(percent=100),
            "height": Dimension(percent=100),
            "children": children
        }

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

class Container(Element[UiContext], ChildrenComponent, PositionComponent, SizeComponent):
    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED, background_color: Tuple[int, ...]=(0, 0, 0, 0)) -> Image.Image:
        return Image.new(mode="RGBA", size=size, color=background_color)

class ListLayout(Element[UiContext], SizeComponent):
    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: Dimension=Dimension(), height: Dimension= Dimension()) -> Tuple[int, int]:
        return SizeComponent.size(self, context=context, size=size, width=width, height=height)

    def evaluate(self, *, context: UiContext, size: Tuple[int, int]=REQUIRED) -> Image.Image:
        return Image.new(mode="RGBA", size=size)

    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None, direction: Literal["horizontal", "vertical"]="vertical", spacing: Dimension=Dimension()) -> None:
        if children:
            offset: int = 0
            for child in children:
                evaluated.alpha_composite(im=child, dest=(offset, 0) if direction == "horizontal" else (0, offset))
                offset += child.width if direction == "horizontal" else child.height
                offset += spacing.to_pixels(evaluated.width if direction == "horizontal" else evaluated.height)

@element(
    Canvas,
    Container,
    ListLayout
)
class Ui(Plugin[UiContext]):
    def new_context(self) -> UiContext:
        return None