import argparse
import json
import sys
from typing import Any, List

def _load_json(file_path: str) -> Any:
    try:
        with open(file_path) as f:
            return json.load(f)
    except Exception:
        raise argparse.ArgumentTypeError("Invalid .json file")

def _parse_args(args: List[str]) -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Programmatically generate posters using templates and various online services."
    )
    parser.add_argument(
        "template",
        type=_load_json,
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