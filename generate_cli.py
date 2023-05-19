import sys
from argparse import ArgumentParser, Namespace, REMAINDER
from poster_generator.poster_builder import PosterBuilder
from poster_generator.poster_template import PosterTemplate, PosterTemplateModel
from poster_generator.type_utils import parse_file
from typing import List

def _parse_args(args: List[str]) -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        description="Programmatically generate templated posters while leveraging plugin features."
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="enable debug mode during poster generation"
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
    model: PosterTemplateModel = parse_file(args.template, PosterTemplateModel)
    template: PosterTemplate = PosterTemplate(model)
    builder: PosterBuilder = PosterBuilder(template, args.template_args)
    builder.build().write_to_file(f"TEST{'_DEBUG' * args.debug}.png")