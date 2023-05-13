import numpy as np
from .context_provider import ActiveContext
from .poster_template import PosterTemplate
from argparse import Namespace
from base import Args
from pyvips import Image
from typing import List

class PosterBuilder:
    def __init__(self,template: PosterTemplate,raw_args: List[str]) -> None:
        args: Namespace = template.parser.parse_args(raw_args)
        self._template: PosterTemplate = template
        self._context: ActiveContext = template.plugin_context.active_context()
        self._context.set_context(Args, vars(args))
        
        for expression in template.logic:
            self._context.evaluate_expression(expression)
    
    def build(self) -> Image:
        return Image.new_from_array(np.zeros((self._template.height, self._template.width, 3), dtype=np.uint8))