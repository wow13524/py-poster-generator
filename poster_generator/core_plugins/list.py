from poster_generator.api import Expression, Plugin, REQUIRED, expression
from sys import maxsize
from typing import Any, Callable, Iterable, List as TList, Optional

class New(Expression[TList[Any], None]):
    def evaluate(self, *, context: None, iterable: Optional[Iterable[Any]]=None) -> TList[Any]:
        return list(iterable) if iterable else list()

class Append(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, value: Any=REQUIRED) -> None:
        l.append(value)

class Clear(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED) -> None:
        l.clear()

class Copy(Expression[TList[Any], None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED) -> TList[Any]:
        return l.copy()

class Count(Expression[int, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, value: Any=REQUIRED) -> int:
        return l.count(value)

class Extend(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, iterable: Iterable[Any]=REQUIRED) -> None:
        l.extend(iterable)

class Index(Expression[int, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, value: Any=REQUIRED, start: int=0, stop: int=maxsize) -> int:
        return l.index(value, start, stop)

class Insert(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, index: int=REQUIRED, object: Any=REQUIRED) -> None:
        l.insert(index, object)

class Pop(Expression[Any, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, index: int=-1) -> Any:
        return l.pop(index)

class Remove(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, value: Any=REQUIRED) -> None:
        l.remove(value)

class Reverse(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED) -> None:
        l.reverse()

class Sort(Expression[None, None]):
    def evaluate(self, *, context: None, l: TList[Any]=REQUIRED, key: Optional[Callable[[Any], Any]]=None, reverse: bool=False) -> None:
        l.sort(key=key, reverse=reverse)

@expression(
    New,
    Append,
    Clear,
    Copy,
    Count,
    Extend,
    Index,
    Insert,
    Pop,
    Remove,
    Reverse,
    Sort
)
class List(Plugin[None]):
    def new_context(self) -> None:
        return None