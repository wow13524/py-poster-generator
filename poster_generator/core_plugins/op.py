from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any

class Add(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a + b

class Sub(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a - b

class Mul(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a * b

class Div(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a / b

class Mod(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a % b

class Pow(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a ** b

class Round(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> Any:
        return round(a)

class Gt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a > b

class Gte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a >= b

class Lt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a < b

class Lte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a <= b

class Eq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a == b

class Neq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a != b

class Is(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> bool:
        return a is b

@expression(
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    Pow,
    Round,
    Gt,
    Gte,
    Lt,
    Lte,
    Eq,
    Neq,
    Is
)
class Op(Plugin[None]):
    def new_context(self) -> None:
        return None