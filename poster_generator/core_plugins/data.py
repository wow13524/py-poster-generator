from types import NoneType
from poster_generator.api import Expression, Plugin, expression
from .classes import Dimension as CDimension

DataContext = NoneType

class Dimension(Expression[CDimension, DataContext]):
    def __init__(self, px: int=0, percent: float=0) -> None:
        self._fields = {}
        self._px = px
        self._percent = percent

    def evaluate(self, *, context: DataContext, px: int=0, percent: float=0) -> CDimension:
        return CDimension(px=px, percent=percent)
    
    def to_pixels(self, size: int) -> int:
        return int(self._px + self._percent * size / 100.)

@expression(
    Dimension
)
class Data(Plugin[DataContext]):
    def new_context(self) -> DataContext:
        return None