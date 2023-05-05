from .args_plugin import Args
from .base_plugin import Base
from .str_plugin import Str
from .vars_plugin import Vars
from poster_generator.api import PluginTypeList

export_plugins: PluginTypeList = [
    Args,
    Base,
    Str,
    Vars
]