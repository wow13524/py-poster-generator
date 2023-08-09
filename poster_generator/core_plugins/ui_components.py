from typing import Any, List, Optional, Tuple
from PIL import Image
from poster_generator.api import REQUIRED, compute_field, post_effect
from .classes import Dimension

class ChildrenComponent:
    @post_effect
    def apply_children(self, *, context: Any, evaluated: Image.Image, children: Optional[List[Image.Image]]=None) -> None:
        if children:
            for child in children:
                evaluated.alpha_composite(im=child, dest=child.info.get("position", (0, 0)))

class PositionComponent:
    @post_effect
    def apply_position(self, *, context: Any, evaluated: Image.Image, parent_size: Tuple[int, int]=REQUIRED, left: Dimension=Dimension(), top: Dimension=Dimension()) -> None:
        evaluated.info.update({"position": (left.to_pixels(parent_size[0]), top.to_pixels(parent_size[1]))})

class SizeComponent:
    @compute_field(forward=True)
    def parent_size(self, *, context: Any, size: Tuple[int, int]=(-1, -1)) -> Tuple[int, int]:
        return size
    
    @compute_field(forward=True)
    def size(self, *, context: Any, size: Tuple[int, int]=(-1, -1), width: Dimension=Dimension(), height: Dimension=Dimension()) -> Tuple[int, int]:
        assert size != (-1, -1), f"Parent Element did not forward 'size' field, does it subclass {__class__.__name__}?"
        return (width.to_pixels(size[0]), height.to_pixels(size[1]))