"""
This type stub file was generated by pyright.
"""

from cffi import FFI

CData = FFI.CData
GEnum = int
GType = int

from typing import Any, Callable, List

def leak_set(leak: bool) -> None:
    """Enable or disable libvips leak checking.

    With this enabled, libvips will check for object and area leaks on exit.
    Enabling this option will make libvips run slightly more slowly.
    """
    ...

def version(flag: int) -> int:
    """Get the major, minor or micro version number of the libvips library.

    Args:
        flag (int): Pass flag 0 to get the major version number, flag 1 to
            get minor, flag 2 to get micro.

    Returns:
        The version number,

    Raises:
        :class:`.Error`
    """
    ...

def get_suffixes() -> List[str]:
    """Get a list of all the filename suffixes supported by libvips.

    Returns:
        [string]

    """
    ...

def at_least_libvips(x: int, y: int) -> bool:
    """Is this at least libvips x.y?"""
    ...

def path_filename7(filename: str) -> str:
    ...

def path_mode7(filename: str) -> str:
    ...

def type_find(basename: str, nickname: str) -> GType:
    """Get the GType for a name.

    Looks up the GType for a nickname. Types below basename in the type
    hierarchy are searched.
    """
    ...

def type_name(gtype: GType) -> str:
    """Return the name for a GType."""
    ...

def nickname_find(gtype: GType) -> str:
    """Return the nickname for a GType."""
    ...

def type_from_name(name: str) -> GType:
    """Return the GType for a name."""
    ...

def type_map(gtype: GType, fn: Callable[[GType, Any, Any], Any]) -> Any:
    """Map fn over all child types of gtype."""
    ...

def values_for_enum(gtype: GType) -> list[str]:
    """Get all values for a enum (gtype)."""
    ...

def values_for_flag(gtype: GType) -> list[str]:
    """Get all values for a flag (gtype)."""
    ...

__all__ = ['leak_set', 'version', 'at_least_libvips', 'path_filename7', 'path_mode7', 'type_find', 'nickname_find', 'get_suffixes', 'type_name', 'type_map', 'type_from_name', 'values_for_enum', 'values_for_flag']