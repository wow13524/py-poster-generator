from argparse import ArgumentParser
from dataclasses import asdict
from PIL import Image
from pydoc import locate
from typing import Any, Dict, List, Optional, Type
from .api.models import Element, Expression
from .core_plugins import Args
from .models import PosterTemplate
from .plugin_context import ActiveContext, PluginContext

def generate_poster(template: PosterTemplate, args: List[Any], debug: bool=False) -> Image.Image:
    parser: ArgumentParser = ArgumentParser(template.meta.name)
    plugin_context: PluginContext = PluginContext(template.meta.required_plugins)
    content: List[Element[Any]] = [plugin_context.parse_element(raw_obj) for raw_obj in template.content]
    logic: List[Expression[Any, Any]] = [plugin_context.parse_expression(raw_obj) for raw_obj in template.logic]
    active_context: ActiveContext = plugin_context.new_active_context()

    #Build parser
    for arg in template.meta.cli_args:
        name_or_flags: List[str] = arg.name_or_flags if isinstance(arg.name_or_flags, List) else [arg.name_or_flags]
        kwargs: Dict[str, Any] = {k: v for k,v in asdict(arg).items() if v is not None}
        del kwargs["name_or_flags"]
        if arg.type:
            t: Optional[object] = locate(arg.type)
            assert isinstance(t, Type), f"invalid type {arg.type}"
            kwargs["type"] = t
        parser.add_argument(*name_or_flags, **kwargs)
    
    active_context.update(Args, vars(parser.parse_args(args)))
    list(map(active_context.evaluate, logic + content))

    return Image.new("RGB", (template.meta.width, template.meta.height))