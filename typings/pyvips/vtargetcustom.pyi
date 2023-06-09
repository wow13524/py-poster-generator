"""
This type stub file was generated by pyright.
"""

import pyvips
from logging import Logger
from typing import Any, Callable, Literal, Optional

logger: Logger
class TargetCustom(pyvips.Target):
    """An output target you can connect action signals to to implement
    behaviour.

    """
    def __init__(self) -> None:
        """Make a new target you can customise.

        You can pass this target to (for example) :meth:`write_to_target`.

        """
        ...
    
    def on_write(self, handler: Callable[[bytes], int]) -> None:
        """Attach a write handler.

        The interface is exactly as io.write(). The handler is given a
        bytes-like object to write, and should return the number of bytes
        written.

        """
        ...
    
    def on_read(self, handler: Callable[[Optional[int]], Any]) -> None:
        """Attach a read handler.

        The interface is exactly as io.read(). The handler is given a number
        of bytes to fetch, and should return a bytes-like object containing up
        to that number of bytes. If there is no more data available, it should
        return None.

        Read handlers are optional for targets. If you do not set one, your
        target will be treated as unreadable and libvips will be unable to
        write some file types (just TIFF, as of the time of writing).

        """
        ...
    
    def on_seek(self, handler: Callable[[int, Optional[int]], int]) -> None:
        """Attach a seek handler.

        The interface is the same as io.seek(), so the handler is passed
        parameters for offset and whence with the same meanings.

        However, the handler MUST return the new seek position. A simple way
        to do this is to call io.tell() and return that result.

        Seek handlers are optional. If you do not set one, your target will be
        treated as unseekable and libvips will be unable to write some file
        types (just TIFF, as of the time of writing).

        """
        ...
    
    def on_end(self, handler: Callable[[], Literal[-1, 0]]) -> None:
        """Attach an end handler.

        This optional handler is called at the end of write. It should do any
        cleaning up necessary, and return 0 on success and -1 on error.

        """
        ...
    
    def on_finish(self, handler: Callable[[], Any]) -> None:
        """Attach a finish handler.

        For libvips 8.13 and later, this method is deprecated in favour of
        :meth:`on_end`.

        """
        ...
    


__all__ = ['TargetCustom']
