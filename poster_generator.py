import sys
import type_utils
from argparse import ArgumentParser,Namespace,REMAINDER
from poster_builder import PosterBuilder
from poster_template import PosterTemplate,PosterTemplateModel
from typing import List

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
    builder: PosterBuilder = PosterBuilder(template,args.template_args)
    builder.build().save("TEST.png")