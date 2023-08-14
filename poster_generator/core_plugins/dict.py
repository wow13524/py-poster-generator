from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any, Dict as TDict, ItemsView, Iterable, KeysView, Optional, Tuple, ValuesView

class Clear(Expression[None, None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> None:
        d.clear()

class Copy(Expression[TDict[Any, Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> TDict[Any, Any]:
        return d.copy()

class Fromkeys(Expression[TDict[Any, Any], None]):
    def evaluate(self, *, context: None, iterable: Iterable[Any]=REQUIRED, value: Any=None) -> TDict[Any, Any]:
        return dict.fromkeys(iterable, value)

class Get(Expression[Any, None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED, key: Any=REQUIRED) -> Any:
        return d.get(key)

class Items(Expression[ItemsView[Any, Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> ItemsView[Any, Any]:
        return d.items()

class Keys(Expression[KeysView[Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> KeysView[Any]:
        return d.keys()

class Pop(Expression[Any, None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED, key: Any=REQUIRED) -> Any:
        return d.pop(key)

class Popitem(Expression[Tuple[Any, Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> Tuple[Any, Any]:
        return d.popitem()

class Setdefault(Expression[Optional[Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED, key: Any=REQUIRED, default: Any=None) -> Optional[Any]:
        d.setdefault(key, default)

class Update(Expression[None, None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED, kwargs: TDict[Any, Any]=REQUIRED) -> None:
        d.update(**kwargs)

class Values(Expression[ValuesView[Any], None]):
    def evaluate(self, *, context: None, d: TDict[Any, Any]=REQUIRED) -> ValuesView[Any]:
        return d.values()

@expression(
    Clear,
    Copy,
    Fromkeys,
    Get,
    Items,
    Keys,
    Pop,
    Popitem,
    Setdefault,
    Update,
    Values
)
class Dict(Plugin[None]):
    def new_context(self) -> None:
        return None