from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any, Iterable, Optional, Set as TSet

class New(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, iterable: Optional[Iterable[Any]]=None) -> TSet[Any]:
        return set(iterable) if iterable else set()

class Add(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, element: Any=REQUIRED) -> None:
        s.add(element)

class Clear(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED) -> None:
        s.clear()

class Copy(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED) -> TSet[Any]:
        return s.copy()

class Difference(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> TSet[Any]:
        return s.difference(*t)

class DifferenceUpdate(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> None:
        s.difference_update(*t)

class Discard(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, value: Any=REQUIRED) -> None:
        s.discard(value)

class Intersection(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> TSet[Any]:
        return s.intersection(*t)
    
class IntersectionUpdate(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> None:
        s.intersection_update(*t)

class Isdisjoint(Expression[bool, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: TSet[Any]=REQUIRED) -> bool:
        return s.isdisjoint(t)

class Issubset(Expression[bool, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: TSet[Any]=REQUIRED) -> bool:
        return s.issubset(t)

class Issuperset(Expression[bool, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: TSet[Any]=REQUIRED) -> bool:
        return s.issuperset(t)

class Pop(Expression[Any, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED) -> Any:
        return s.pop()

class Remove(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, element: Any=REQUIRED) -> None:
        s.remove(element)

class SymmetricDifference(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> TSet[Any]:
        return s.symmetric_difference(*t)

class SymmetricDifferenceUpdate(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> None:
        s.symmetric_difference_update(*t)

class Union(Expression[TSet[Any], None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> TSet[Any]:
        return s.union(*t)

class Update(Expression[None, None]):
    def evaluate(self, *, context: None, s: TSet[Any]=REQUIRED, t: Iterable[TSet[Any]]=REQUIRED) -> None:
        s.update(*t)

@expression(
    New,
    Add,
    Clear,
    Copy,
    Difference,
    DifferenceUpdate,
    Discard,
    Intersection,
    IntersectionUpdate,
    Isdisjoint,
    Issubset,
    Issuperset,
    Pop,
    Remove,
    SymmetricDifference,
    SymmetricDifferenceUpdate,
    Union,
    Update
)
class Set(Plugin[None]):
    def new_context(self) -> None:
        return None