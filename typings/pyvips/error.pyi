"""
This type stub file was generated by pyright.
"""

logger = ...
_is_PY3 = ...
if _is_PY3:
    text_type = ...
    byte_type = ...
else:
    text_type = ...
    byte_type = ...
class Error(Exception):
    """An error from vips.

    Attributes:
        message (str): a high-level description of the error
        detail (str): a string with some detailed diagnostics

    """
    def __init__(self, message, detail=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


__all__ = ['_to_bytes', '_to_string', '_to_string_copy', 'Error']
