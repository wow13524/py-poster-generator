"""
This type stub file was generated by pyright.
"""

import pyvips

class Connection(pyvips.VipsObject):
    """The abstract base Connection class.

    """
    def __init__(self, pointer: pyvips.CData) -> None:
        ...
    
    def filename(self) -> str | None:
        """Get the filename associated with a connection. Return None if there
        is no associated file.

        """
        ...
    
    def nick(self) -> str | None:
        """Make a human-readable name for a connection suitable for error
        messages.

        """
        ...
    


__all__ = ['Connection']
