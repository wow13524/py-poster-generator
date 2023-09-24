from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any as TAny, Iterable, Iterator, List, Optional, Reversible, Sized, SupportsIndex, Tuple, Union, cast

class Add(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a + b

class Sub(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a - b

class Mul(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a * b

class Div(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a / b

class Divmod(Expression[Tuple[TAny, TAny], None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> Tuple[TAny, TAny]:
        return divmod(a, b)
    
class Idiv(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a // b

class Mod(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a % b

class Pow(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> TAny:
        return a ** b

class Abs(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> TAny:
        return abs(a)

class All(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Iterable[TAny]=REQUIRED) -> bool:
        return all(a)

class Any(Expression[bool, None]):
    def evaluate(self, *, context: None, a: Iterable[TAny]=REQUIRED) -> bool:
        return any(a)

class Round(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> TAny:
        return round(a)

class Len(Expression[int, None]):
    def evaluate(self, *, context: None, a: Sized=REQUIRED) -> int:
        return len(a)
    
class Min(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> TAny:
        return min(a)
    
class Max(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> TAny:
        return max(a)

class Ascii(Expression[str, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> str:
        return ascii(a)

class Bin(Expression[str, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> str:
        return bin(a)

class Oct(Expression[str, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> str:
        return oct(a)

class Hex(Expression[str, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> str:
        return hex(a)
    
class Chr(Expression[str, None]):
    def evaluate(self, *, context: None, a: int=REQUIRED) -> str:
        return chr(a)

class Ord(Expression[int, None]):
    def evaluate(self, *, context: None, a: Union[str, bytes, bytearray]=REQUIRED) -> int:
        return ord(a)

class Hash(Expression[int, None]):
    def evaluate(self, *, context: None, a: object=REQUIRED) -> int:
        return hash(a)
    
class Repr(Expression[str, None]):
    def evaluate(self, *, context: None, a: object=REQUIRED) -> str:
        return repr(a)

class Id(Expression[int, None]):
    def evaluate(self, *, context: None, a: object=REQUIRED) -> int:
        return id(a)

class Gt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a > b

class Gte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a >= b

class Lt(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a < b

class Lte(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a <= b

class Eq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a == b

class Neq(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a != b

class Is(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, b: TAny=REQUIRED) -> bool:
        return a is b
    
class Callable(Expression[bool, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> bool:
        return callable(a)

class Sum(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: Iterable[TAny]=REQUIRED, start: TAny=0) -> TAny:
        return sum(a, start=start)

class Enumerate(Expression[Iterator[tuple[int, TAny]], None]):
    def evaluate(self, *, context: None, a: Iterator[TAny]=REQUIRED, start: int=0) -> Iterator[tuple[int, TAny]]:
        return enumerate(a, start)

class Zip(Expression[Iterator[tuple[TAny, TAny]], None]):
    def evaluate(self, *, context: None, a: Iterator[TAny]=REQUIRED, b: Iterator[TAny]=REQUIRED, strict: bool=False) -> Iterator[tuple[TAny, TAny]]:
        return zip(a, b, strict=strict)

class Print(Expression[None, None]):
    def evaluate(self, *, context: None, a: List[TAny]=[], sep: Optional[str]=" ", end: Optional[str]="\n") -> None:
        return print(*a, sep=sep, end=end)

class Reversed(Expression[None, None]):
    def evaluate(self, *, context: None, a: Reversible[TAny]=REQUIRED) -> None:
        reversed(a)

class Sorted(Expression[None, None]):
    def evaluate(self, *, context: None, a: Iterable[TAny]=REQUIRED, key: TAny=None, reverse: bool=False) -> None:
        sorted(a)

class Range(Expression[range, None]):
    def evaluate(self, *, context: None, start: SupportsIndex=0, stop: SupportsIndex=REQUIRED, step: SupportsIndex=1) -> range:
        return range(start, stop, step)

class Type(Expression[type, None]):
    def evaluate(self, *, context: None, a: object=REQUIRED) -> type:
        return type(a)

class Next(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED) -> TAny:
        return next(a)

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
    All,
    Any,
    Round,
    Len,
    Min,
    Max,
    Ascii,
    Bin,
    Oct,
    Hex,
    Chr,
    Ord,
    Hash,
    Repr,
    Id,
    Gt,
    Gte,
    Lt,
    Lte,
    Eq,
    Neq,
    Is,
    Callable,
    Sum,
    Enumerate,
    Zip,
    Print,
    Reversed,
    Sorted,
    Range,
    Type,
    Next
)
class Op(Plugin[None]):
    def new_context(self) -> None:
        return None