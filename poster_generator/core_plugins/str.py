from poster_generator.api import Expression, Plugin, REQUIRED, expression
from typing import Dict, Iterable, List, Optional, Tuple, TypeVar, Union

T = TypeVar("T")

class Capitalize(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.capitalize()

class Casefold(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.casefold()

class Center(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, width: int=REQUIRED, fillchar: str="") -> str:
        return s.center(width, fillchar)

class Count(Expression[int, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, x: str=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> int:
        return s.count(x, start, end)

class Encode(Expression[bytes, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, encoding: str="utf-8", errors: str="strict") -> bytes:
        return s.encode(encoding, errors)

class Endswith(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, suffix: Union[str, Tuple[str, ...]]=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> bool:
        return s.endswith(suffix, start, end)

class Expandtabs(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, tabsize: int=8) -> str:
        return s.expandtabs(tabsize)

class Find(Expression[int, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sub: str=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> int:
        return s.find(sub, start, end)

class Format(Expression[str, None]):
    def evaluate(self,  *args: object, context: None, s: str=REQUIRED, **kwargs: object) -> str:
        return s.format(*args, **kwargs)

class FormatMap(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, map: Dict[str, object]=REQUIRED) -> str:
        return s.format_map(map)

class Index(Expression[int, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sub: str=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> int:
        return s.index(sub, start, end)

class Isalnum(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isalnum()

class Isalpha(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isalpha()

class Isascii(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isascii()

class Isdecimal(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isdecimal()

class Isdigit(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isdigit()

class Isidentifier(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isidentifier()

class Islower(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.islower()

class Isnumeric(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isnumeric()

class Isprintable(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isprintable()

class Isspace(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isspace()

class Istitle(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.istitle()

class Isupper(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> bool:
        return s.isupper()

class Join(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, iterable: Iterable[str]=REQUIRED) -> str:
        return s.join(iterable)

class Ljust(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, width: int=REQUIRED, fillchar: str="") -> str:
        return s.ljust(width, fillchar)

class Lower(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.lower()

class Lstrip(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, chars: Optional[str]=None) -> str:
        return s.lstrip(chars)

class Maketrans(Expression[Union[Dict[int, T], Dict[int, Optional[int]]], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, x: Union[Dict[int, T], Dict[str, T], Dict[Union[int, str], T], str]=REQUIRED, y: Optional[str]=None, z: Optional[str]=None) -> Union[Dict[int, T], Dict[int, Optional[int]]]:
        if type(x) == dict:
            return s.maketrans(x)
        elif type(x) == str and y and z:
            return s.maketrans(x, y, z)
        raise TypeError

class Partition(Expression[Tuple[str, str, str], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: str=REQUIRED) -> Tuple[str, str, str]:
        return s.partition(sep)

class Removeprefix(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: str=REQUIRED) -> str:
        return s.removeprefix(sep)

class Removesuffix(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: str=REQUIRED) -> str:
        return s.removesuffix(sep)

class Replace(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, old: str=REQUIRED, new: str=REQUIRED, count: int=-1) -> str:
        return s.replace(old, new, count)

class Rfind(Expression[int, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sub: str=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> int:
        return s.rfind(sub, start, end)

class Rindex(Expression[int, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sub: str=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> int:
        return s.rindex(sub, start, end)

class Rjust(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, width: int=REQUIRED, fillchar: str="") -> str:
        return s.rjust(width, fillchar)

class Rpartition(Expression[Tuple[str, str, str], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: str=REQUIRED) -> Tuple[str, str, str]:
        return s.rpartition(sep)

class Rsplit(Expression[List[str], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: Optional[str]=None, maxsplit: int=-1) -> List[str]:
        return s.rsplit(sep, maxsplit)

class Rstrip(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, chars: Optional[str]=None) -> str:
        return s.rstrip(chars)

class Split(Expression[List[str], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, sep: Optional[str]=REQUIRED, maxsplit: int=-1) -> List[str]:
        return s.split(sep, maxsplit)

class Splitlines(Expression[List[str], None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, keepends: bool=False) -> List[str]:
        return s.splitlines(keepends)

class Startswith(Expression[bool, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, prefix: Union[str, Tuple[str, ...]]=REQUIRED, start: Optional[int]=None, end: Optional[int]=None) -> bool:
        return s.startswith(prefix, start, end)

class Strip(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, chars: Optional[str]=None) -> str:
        return s.strip(chars)

class Swapcase(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.swapcase()

class Title(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.title()

class Translate(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, table: Dict[int, Optional[Union[str, int]]]=REQUIRED) -> str:
        return s.translate(table)

class Upper(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED) -> str:
        return s.upper()

class Zfill(Expression[str, None]):
    def evaluate(self, *, context: None, s: str=REQUIRED, width: int=REQUIRED) -> str:
        return s.zfill(width)

@expression(
    Capitalize,
    Casefold,
    Center,
    Count,
    Encode,
    Endswith,
    Expandtabs,
    Find,
    Format,
    FormatMap,
    Index,
    Isalnum,
    Isalpha,
    Isascii,
    Isdecimal,
    Isdigit,
    Isidentifier,
    Islower,
    Isnumeric,
    Isprintable,
    Isspace,
    Istitle,
    Isupper,
    Join,
    Ljust,
    Lower,
    Lstrip,
    Maketrans,
    Partition,
    Removeprefix,
    Removesuffix,
    Replace,
    Rfind,
    Rindex,
    Rjust,
    Rpartition,
    Rsplit,
    Rstrip,
    Split,
    Splitlines,
    Startswith,
    Strip,
    Swapcase,
    Title,
    Translate,
    Upper,
    Zfill
)
class Str(Plugin[None]):
    def new_context(self) -> None:
        return None