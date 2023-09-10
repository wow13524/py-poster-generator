from typing_extensions import Buffer
from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any, Iterable, Literal, SupportsBytes, SupportsIndex, Union

class New(Expression[int, Any]):
    def evaluate(self, *, context: Any, object: Any=REQUIRED) -> int:
        return int(object)

class AsIntegerRatio(Expression[tuple[int, Literal[1]], None]):
    def evaluate(self, *, context: None, i: int=REQUIRED) -> tuple[int, Literal[1]]:
        return i.as_integer_ratio()

class BitCount(Expression[int, None]):
    def evaluate(self, *, context: None, i: int=REQUIRED) -> int:
        return i.bit_count()
    
class BitLength(Expression[int, None]):
    def evaluate(self, *, context: None, i: int=REQUIRED) -> int:
        return i.bit_length()

class Conjugate(Expression[int, None]):
    def evaluate(self, *, context: None, i: int=REQUIRED) -> int:
        return i.conjugate()

class FromBytes(Expression[int, None]):
    def evaluate(self, *, context: None, bytes: Union[Iterable[SupportsIndex], SupportsBytes, Buffer]=REQUIRED, byteorder: Literal["little", "big"]="big", signed: bool=False) -> int:
        return int.from_bytes(bytes, byteorder, signed=signed)

class ToBytes(Expression[bytes, None]):
    def evaluate(self, *, context: None, i: int=REQUIRED, length: SupportsIndex=1, byteorder: Literal["little", "big"]="big", signed: bool=False) -> bytes:
        return i.to_bytes(length, byteorder, signed=signed)

@expression(
    New,
    AsIntegerRatio,
    BitCount,
    BitLength,
    Conjugate,
    FromBytes,
    ToBytes
)
class Int(Plugin[None]):
    def new_context(self) -> None:
        return None