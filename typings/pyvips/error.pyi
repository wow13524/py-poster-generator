"""
This type stub file was generated by pyright.
"""

from logging import Logger
from typing import Type

logger: Logger

text_type: Type[str]
byte_type: Type[bytes]


def _to_bytes(x: str) -> bytes:
    """Convert to a byte string.

    Convert a Python unicode string or a pathlib.Path to a utf-8-encoded
    byte string. You must call this on strings you pass to libvips.

    """
    ...


def _to_string(x: bytes) -> str:
    """Convert to a unicode string.

    If x is a byte string, assume it is utf-8 and decode to a Python unicode
    string. You must call this on text strings you get back from libvips.

    """
    ...


def _to_string_copy(x: bytes) -> str:
    """Convert to a unicode string, and auto-free.

    As _to_string(), but also tag x as a pointer to a memory area that must
    be freed with g_free().

    """
    ...

class Error(Exception):
    """An error from vips.

    Attributes:
        message (str): a high-level description of the error
        detail (str): a string with some detailed diagnostics

    """
    def __init__(self, message: str, detail: str=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


__all__ = ['_to_bytes', '_to_string', '_to_string_copy', 'Error']
