# pyright: reportUnknownVariableType=false
# ^ the type of typeguard.check_type ironically can't be inferred :P

import json
from pydoc import locate
from typeguard import check_type
from typing import Any,Dict,Generator,List,Literal,Tuple,Type,TypeVar,Union,cast,get_args,get_origin,get_type_hints

T = TypeVar("T",bound="PropertyDict")

def _get_raw_origin(tp: Type[Any]) -> type:
    return get_origin(tp) or tp

def _parse_value(value: Any,tp: type,subpath: str) -> Any:
    origin: type = _get_raw_origin(tp)
    if isinstance(value,PropertyDict):
        value = dict(value)
    if origin == dict:
        value = value.copy()
    elif origin == list:
        value = [_parse_value(x,get_args(tp)[0],f"{subpath}[{i}]") for i,x in enumerate(value)]
    elif origin == Any or origin == Literal or origin == Union:
        pass
    elif issubclass(tp,PropertyDict):
        value = tp(value,subpath)
    return value

class TypedProperties:
    def __init__(self):
        self._types: Dict[str,type] = get_type_hints(self)
    
    def __iter__(self) -> Generator[Tuple[str,Any],None,None]:
        for attr,tp in self._types.items():
            value: Any = getattr(self,attr)
            if isinstance(value,TypedProperties):
                value = dict(value)
            elif isinstance(value,list) and issubclass(_get_raw_origin(get_args(tp)[0]),TypedProperties):
                value = list(map(dict,cast(List[TypedProperties],value)))
            yield attr, value

class PropertyDict(TypedProperties):
    def __init__(self,data: Dict[str,Any],path: str) -> None:
        super().__init__()
        missing_fields = [field for field,tp in self._types.items() if field not in data and type(None) not in get_args(tp)]
        assert not missing_fields, f"fields missing from {path}: {','.join(missing_fields)}"
        for attr,tp in self._types.items():
            subpath: str = f"{path}.{attr}"
            value: Any = data[attr] if attr in data else None if type(None) in get_args(tp) else getattr(self.__class__,attr)
            value = _parse_value(value,tp,subpath)
            check_type(subpath,value,tp)
            setattr(self,attr,value)

def parse_file(file_path: str, config_type: Type[T]) -> T:
    with open(file_path) as f:
        data: Dict[str,Any] = json.load(f)
    properties: T = config_type(data,config_type.__name__)
    return properties

def parse_type(type_string: str) -> Type[Any]:
    tp: Any = locate(type_string)
    assert isinstance(tp,Type), f"invalid type {type_string}"
    return tp