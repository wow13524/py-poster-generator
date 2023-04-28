import sys
import type_utils
from argparse import ArgumentParser,Namespace,REMAINDER
from base import Args
from plugin_api import ContextProvider
from poster_template import PosterTemplate,PosterTemplateModel
from typing import List

def _generate_poster(template: PosterTemplate,raw_args: List[str]) -> None:
    args: Namespace = template.parser.parse_args(raw_args)
    context_provider: ContextProvider = ContextProvider(template.plugins)
    context_provider.set(Args,vars(args))
    
    for expression in template.logic:
        expression.evaluate(context_provider)
    
    print(context_provider.__dict__)

def _parse_args(args: List[str]) -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        description="Programmatically generate posters using templates and various online services."
    )
    parser.add_argument(
        "template",
        help="path of the desired poster template"
    )
    parser.add_argument(
        "template_args",
        nargs=REMAINDER,
        help="arguments to pass to the poster template"
    )
    return parser.parse_args(args)

if __name__ == "__main__":
    args: Namespace = _parse_args(sys.argv[1:])
    model: PosterTemplateModel = type_utils.parse_file(args.template,PosterTemplateModel)
    template: PosterTemplate = PosterTemplate(model)
    _generate_poster(template,args.template_args)