from ..type_utils import PropertyDict
from typing import Any, Dict, Generator, Tuple

RawContent = Dict[str, Any]

class RawObject(PropertyDict):
    def __init__(self, data: RawContent, path: str) -> None:
        super().__init__(data, path)
        self._raw = data
    
    @property
    def raw(self) -> RawContent:
        return self._raw
    
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]:
        for key, value in self.raw.items():
            yield key, value