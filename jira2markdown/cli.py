import argparse
import sys
from pathlib import Path

from jira2markdown import convert


def main() -> None:
    if sys.stdin.isatty():
        parser = argparse.ArgumentParser(description="Converts text from JIRA markup to Markdown")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("text", nargs="?", type=str)
        group.add_argument("-f", "--file", nargs="?", type=Path)

        args = parser.parse_args()
        text = args.file.read_text() if args.file else args.text
    else:
        text = sys.stdin.read()

    sys.stdout.write(convert(text))


if __name__ == "__main__":
    main()
