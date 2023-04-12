import argparse
import poster_template
import sys
import type_utils
from typing import List

def _parse_args(args: List[str]) -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Programmatically generate posters using templates and various online services."
    )
    parser.add_argument(
        "template",
        help="path of the desired poster template"
    )
    parser.add_argument(
        "template_args",
        nargs=argparse.REMAINDER,
        help="arguments to pass to the poster template"
    )
    return parser.parse_args(args)

if __name__ == "__main__":
    args: argparse.Namespace = _parse_args(sys.argv[1:])
    print(args)

    model: poster_template.PosterTemplateModel = type_utils.parse_file(args.template,poster_template.PosterTemplateModel)