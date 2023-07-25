from argparse import ArgumentParser
from dataclasses import asdict
from PIL import Image
from pydoc import locate
from typing import Any, Dict, List, Optional, Type
from .models import PosterTemplate

def generate_poster(template: PosterTemplate, args: List[Any], debug: bool=False) -> Image.Image:
    parser: ArgumentParser = ArgumentParser(template.meta.name)

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
    
    print(parser.parse_args(args))
    return Image.new("RGB", (template.meta.width, template.meta.height))