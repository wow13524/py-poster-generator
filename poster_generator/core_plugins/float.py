from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any

class Construct(Expression[float, Any]):
    def evaluate(self, *, context: Any, object: Any=REQUIRED) -> float:
        return float(object)

class AsIntegerRatio(Expression[tuple[int, int], None]):
    def evaluate(self, *, context: None, f: float=REQUIRED) -> tuple[int, int]:
        return f.as_integer_ratio()

class Conjugate(Expression[float, None]):
    def evaluate(self, *, context: None, f: float=REQUIRED) -> float:
        return f.conjugate()

class FromHex(Expression[float, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> float:
        return float.fromhex(s)

class Hex(Expression[str, None]):
    def evaluate(self, *, context: None, f: float=REQUIRED) -> str:
        return f.hex()

class IsInteger(Expression[bool, None]):
    def evaluate(self, *, context: None, f: float=REQUIRED) -> bool:
        return f.is_integer()

@expression(
    Construct,
    AsIntegerRatio,
    Conjugate,
    FromHex,
    Hex,
    IsInteger
)
class Float(Plugin[None]):
    def new_context(self) -> None:
        return None