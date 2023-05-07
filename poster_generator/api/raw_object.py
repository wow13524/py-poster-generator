from ..type_utils import PropertyDict
from typing import Any, Callable, Dict, Generator, Tuple, Type, TypeVar, cast

RawContent = Dict[str, Any]
TNestedObject = TypeVar("TNestedObject", bound='NestedObject')

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

class NestedObject:
    @classmethod
    def annotations(cls: Type['NestedObject']) -> Dict[str, type]:
        annotations: Dict[str, type] = cls._target().__annotations__.copy()
        if "self" in annotations:
            del annotations["self"]
        if "context" in annotations:
            del annotations["context"]
        if "return" in annotations:
            del annotations["return"]
        return annotations
    
    @classmethod
    def requires_context(cls: Type['NestedObject']) -> bool:
        return "context" in cls._target().__annotations__
    
    @classmethod
    def _target(cls: Type['NestedObject']) -> Callable[..., Any]:
        return cast(Any, None)

    def __init__(self, children: Dict[str, TNestedObject]) -> None:
        self._children = children

    @property
    def children(self: TNestedObject) -> Dict[str, TNestedObject]:
        return cast(Dict[str, TNestedObject], self._children)