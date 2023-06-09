"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict

def cdefs(features: Dict[str, Any]) -> str:
    """Return the C API declarations for libvips.

    features is a dict with the features we want. Some features were only
    added in later libvips, for example, and some need to be disabled in
    some FFI modes.

    """
    ...

__all__ = ['cdefs']
