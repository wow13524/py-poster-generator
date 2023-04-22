from .plugin import Base
from .str_plugin import Str
from plugin_api import PluginTypeList

export_plugins: PluginTypeList = [
    Base,
    Str
]