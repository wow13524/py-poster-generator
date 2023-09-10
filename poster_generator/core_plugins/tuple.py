from poster_generator.api import Expression, Plugin, REQUIRED, expression
from sys import maxsize
from typing import Any, Iterable

class New(Expression[tuple[Any, ...], Any]):
    def evaluate(self, *, context: Any, args: Iterable[Any]=REQUIRED) -> tuple[Any, ...]:
        return tuple(args)

class Count(Expression[int, None]):
    def evaluate(self, *, context: None, t: tuple[Any, ...]=REQUIRED, value: Any=REQUIRED) -> int:
        return t.count(value)

class Index(Expression[int, None]):
    def evaluate(self, *, context: None, t: tuple[Any, ...]=REQUIRED, value: Any=REQUIRED, start: int=0, stop: int=maxsize) -> int:
        return t.index(value, start, stop)

@expression(
    New,
    Count,
    Index
)
class Tuple(Plugin[None]):
    def new_context(self) -> None:
        return None