from types import NoneType
from poster_generator.api import Expression, Plugin, expression
from .classes import Dimension as CDimension

DataContext = NoneType

class Dimension(Expression[CDimension, DataContext]):
    def evaluate(self, *, context: DataContext, px: int=0, percent: float=0) -> CDimension:
        return CDimension(px=px, percent=percent)

@expression(
    Dimension
)
class Data(Plugin[DataContext]):
    def new_context(self) -> DataContext:
        return None