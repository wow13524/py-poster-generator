from typing_extensions import Buffer
from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Any, Iterable, Literal, SupportsBytes, SupportsIndex, Union

class New(Expression[bool, Any]):
    def evaluate(self, *, context: Any, object: Any=REQUIRED) -> bool:
        return bool(object)

class AsIntegerRatio(Expression[tuple[int, Literal[1]], None]):
    def evaluate(self, *, context: None, b: bool=REQUIRED) -> tuple[int, Literal[1]]:
        return b.as_integer_ratio()

class BitCount(Expression[int, None]):
    def evaluate(self, *, context: None, b: bool=REQUIRED) -> int:
        return b.bit_count()
    
class BitLength(Expression[int, None]):
    def evaluate(self, *, context: None, b: bool=REQUIRED) -> int:
        return b.bit_length()

class Conjugate(Expression[int, None]):
    def evaluate(self, *, context: None, b: bool=REQUIRED) -> int:
        return b.conjugate()

class FromBytes(Expression[bool, None]):
    def evaluate(self, *, context: None, bytes: Union[Iterable[SupportsIndex], SupportsBytes, Buffer]=REQUIRED, byteorder: Literal["little", "big"]="big", signed: bool=False) -> bool:
        return bool.from_bytes(bytes, byteorder, signed=signed)

class ToBytes(Expression[bytes, None]):
    def evaluate(self, *, context: None, b: bool=REQUIRED, length: SupportsIndex=1, byteorder: Literal["little", "big"]="big", signed: bool=False) -> bytes:
        return b.to_bytes(length, byteorder, signed=signed)

@expression(
    New,
    AsIntegerRatio,
    BitCount,
    BitLength,
    Conjugate,
    FromBytes,
    ToBytes
)
class Bool(Plugin[None]):
    def new_context(self) -> None:
        return None