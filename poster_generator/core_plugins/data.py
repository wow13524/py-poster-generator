from types import NoneType
from poster_generator.api import Expression, Plugin, expression

DataContext = NoneType

class Dimension(Expression['Dimension', DataContext]):
    def __init__(self, px: int=0, percent: float=0) -> None:
        self._fields = {}
        self._px = px
        self._percent = percent

    def evaluate(self, *, context: DataContext, px: int=0, percent: float=0) -> 'Dimension':
        return Dimension(px, percent)
    
    def to_pixels(self, size: int) -> int:
        return int(self._px + self._percent * size / 100.)

@expression(
    Dimension
)
class Data(Plugin[DataContext]):
    def new_context(self) -> DataContext:
        return None