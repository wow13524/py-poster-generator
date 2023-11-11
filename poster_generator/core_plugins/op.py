from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any as TAny, Callable as TCallable, Iterable, Iterator, List, Optional, Reversible, Sized, SupportsIndex, Tuple, Union

class Add(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x + y

class Sub(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x - y

class Mul(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x * y

class Div(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x / y

class Divmod(Expression[Tuple[TAny, TAny], None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> Tuple[TAny, TAny]:
        return divmod(x, y)
    
class Idiv(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x // y

class Mod(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x % y

class Pow(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> TAny:
        return x ** y

class Abs(Expression[TAny, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED) -> TAny:
        return abs(x)

class All(Expression[bool, None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED) -> bool:
        return all(iterable)

class Any(Expression[bool, None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED) -> bool:
        return any(iterable)

class Round(Expression[TAny, None]):
    def evaluate(self, *, context: None, a: TAny=REQUIRED, ndigits: Optional[int]=None) -> TAny:
        return round(a, ndigits=ndigits)

class Len(Expression[int, None]):
    def evaluate(self, *, context: None, obj: Sized=REQUIRED) -> int:
        return len(obj)
    
class Min(Expression[TAny, None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED, key: Optional[TCallable[[TAny], TAny]]=None) -> TAny:
        return min(iterable, key=key)
    
class Max(Expression[TAny, None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED, key: Optional[TCallable[[TAny], TAny]]=None) -> TAny:
        return max(iterable, key=key)

class Ascii(Expression[str, None]):
    def evaluate(self, *, context: None, obj: TAny=REQUIRED) -> str:
        return ascii(obj)

class Bin(Expression[str, None]):
    def evaluate(self, *, context: None, number: Union[int, SupportsIndex]=REQUIRED) -> str:
        return bin(number)

class Oct(Expression[str, None]):
    def evaluate(self, *, context: None, number: Union[int, SupportsIndex]=REQUIRED) -> str:
        return oct(number)

class Hex(Expression[str, None]):
    def evaluate(self, *, context: None, number: Union[int, SupportsIndex]=REQUIRED) -> str:
        return hex(number)
    
class Chr(Expression[str, None]):
    def evaluate(self, *, context: None, i: int=REQUIRED) -> str:
        return chr(i)

class Ord(Expression[int, None]):
    def evaluate(self, *, context: None, c: Union[str, bytes, bytearray]=REQUIRED) -> int:
        return ord(c)

class Hash(Expression[int, None]):
    def evaluate(self, *, context: None, obj: object=REQUIRED) -> int:
        return hash(obj)
    
class Repr(Expression[str, None]):
    def evaluate(self, *, context: None, obj: object=REQUIRED) -> str:
        return repr(obj)

class Id(Expression[int, None]):
    def evaluate(self, *, context: None, obj: object=REQUIRED) -> int:
        return id(obj)

class Gt(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x > y

class Gte(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x >= y

class Lt(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x < y

class Lte(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x <= y

class Eq(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x == y

class Neq(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x != y

class Is(Expression[bool, None]):
    def evaluate(self, *, context: None, x: TAny=REQUIRED, y: TAny=REQUIRED) -> bool:
        return x is y
    
class Callable(Expression[bool, None]):
    def evaluate(self, *, context: None, obj: TAny=REQUIRED) -> bool:
        return callable(obj)

class Sum(Expression[TAny, None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED, start: TAny=0) -> TAny:
        return sum(iterable, start=start)

class Enumerate(Expression[Iterator[tuple[int, TAny]], None]):
    def evaluate(self, *, context: None, iterable: Iterator[TAny]=REQUIRED, start: int=0) -> Iterator[tuple[int, TAny]]:
        return enumerate(iterable, start)

class Zip(Expression[Iterator[tuple[TAny, TAny]], None]):
    def evaluate(self, *, context: None, args: List[Iterable[TAny]]=REQUIRED) -> Iterator[tuple[TAny, TAny]]:
        return zip(*args)

class Print(Expression[None, None]):
    def evaluate(self, *, context: None, values: List[TAny]=[], sep: Optional[str]=" ", end: Optional[str]="\n", flush: bool=False) -> None:
        return print(*values, sep=sep, end=end, flush=flush)

class Reversed(Expression[None, None]):
    def evaluate(self, *, context: None, sequence: Reversible[TAny]=REQUIRED) -> None:
        reversed(sequence)

class Sorted(Expression[List[TAny], None]):
    def evaluate(self, *, context: None, iterable: Iterable[TAny]=REQUIRED, key: TAny=None, reverse: bool=False) -> List[TAny]:
        return sorted(iterable, key=key, reverse=reverse)

class Range(Expression[range, None]):
    def evaluate(self, *, context: None, start: SupportsIndex=0, stop: SupportsIndex=REQUIRED, step: SupportsIndex=1) -> range:
        return range(start, stop, step)

class Type(Expression[type, None]):
    def evaluate(self, *, context: None, o: object=REQUIRED) -> type:
        return type(o)

class Next(Expression[TAny, None]):
    def evaluate(self, *, context: None, i: TAny=REQUIRED) -> TAny:
        return next(i)

class Input(Expression[str, None]):
    def evaluate(self, *, context: None, prompt: object="") -> str:
        return input(prompt)

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
    Next,
    Input
)
class Op(Plugin[None]):
    def new_context(self) -> None:
        return None