import dacite, json, sys
from argparse import ArgumentParser, Namespace, REMAINDER
from poster_generator.models import PosterTemplate
from poster_generator.poster_generator import generate_poster
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
    with open(args.template) as f:
        template: PosterTemplate = dacite.from_dict(PosterTemplate, json.load(f))
        generate_poster(template, args.template_args).save(f"{'DEBUG-' * args.debug}TEST.png")