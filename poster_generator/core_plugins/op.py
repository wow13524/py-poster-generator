from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any, Tuple

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

class Divmod(Expression[Tuple[Any, Any], None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Tuple[Any, Any]:
        return divmod(a, b)
    
class Idiv(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a // b

class Mod(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a % b

class Pow(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED, b: Any=REQUIRED) -> Any:
        return a ** b

class Abs(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> Any:
        return abs(a)

class Round(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> Any:
        return round(a)
    
class Min(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> Any:
        return min(a)
    
class Max(Expression[Any, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> Any:
        return max(a)
    
class Bin(Expression[str, None]):
    def evaluate(self, *, context: None, a: Any=REQUIRED) -> str:
        return bin(a)

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
    Divmod,
    Idiv,
    Mod,
    Pow,
    Abs,
    Round,
    Min,
    Max,
    Bin,
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