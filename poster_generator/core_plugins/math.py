from poster_generator.api import Expression, Plugin, REQUIRED, expression

class Add(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a + b

class Sub(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a - b

class Mul(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a * b

class Div(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a / b

class Mod(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a % b

class Pow(Expression[float, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> float:
        return a ** b

class Gt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a > b

class Gte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a >= b

class Lt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a < b

class Lte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a <= b

class Eq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a == b

class Neq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: float=REQUIRED, b: float=REQUIRED) -> bool:
        return a != b


@expression(
    Add,
    Sub,
    Mul,
    Div,
    Mod,
    Pow,
    Gt,
    Gte,
    Lt,
    Lte,
    Eq,
    Neq
)
class Math(Plugin[None]):
    def new_context(self) -> None:
        return None