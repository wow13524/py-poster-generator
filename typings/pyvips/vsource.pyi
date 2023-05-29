"""
This type stub file was generated by pyright.
"""

import pyvips
from logging import Logger

logger: Logger
class Source(pyvips.Connection):
    """An input connection.

    """
    def __init__(self, pointer: pyvips.CData) -> None:
        ...
    
    @staticmethod
    def new_from_descriptor(descriptor: int) -> Source:
        """Make a new source from a file descriptor (a small integer).

        Make a new source that is attached to the descriptor. For example::

            source = pyvips.Source.new_from_descriptor(0)

        Makes a descriptor attached to stdin.

        You can pass this source to (for example) :meth:`new_from_source`.

        """
        ...
    
    @staticmethod
    def new_from_file(filename: str) -> Source:
        """Make a new source from a filename.

        Make a new source that is attached to the named file. For example::

            source = pyvips.Source.new_from_file("myfile.jpg")

        You can pass this source to (for example) :meth:`new_from_source`.

        """
        ...
    
    @staticmethod
    def new_from_memory(data: memoryview) -> Source:
        """Make a new source from a memory object.

        Make a new source that is attached to the memory object. For example::

            source = pyvips.Source.new_from_memory("myfile.jpg")

        You can pass this source to (for example) :meth:`new_from_source`.

        The memory object can be anything that supports the Python buffer or
        memoryview protocol.

        """
        ...
    


__all__ = ['Source']
