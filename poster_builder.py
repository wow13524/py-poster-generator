from argparse import Namespace
from base import Args
from plugin_api import ContextProvider
from poster_template import PosterTemplate
from PIL import Image
from typing import List

class PosterBuilder:
    def __init__(self,template: PosterTemplate,raw_args: List[str]) -> None:
        args: Namespace = template.parser.parse_args(raw_args)
        self._template: PosterTemplate = template
        self._context: ContextProvider = ContextProvider(template.plugins)
        self._context.set(Args,vars(args))
        
        for expression in template.logic:
            expression.evaluate(self._context)
        
        print(vars(self._context))
    
    def build(self) -> Image.Image:
        return Image.new("RGB",(self._template.width,self._template.height))