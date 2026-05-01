import sys
from pathlib import Path  # noqa: TC003
from typing import Annotated

import typer

from jira2markdown import convert


def main(
    text: Annotated[str | None, typer.Argument(help="Jira markup text to convert")] = None,
    file: Annotated[Path | None, typer.Option("-f", "--file", help="File containing Jira markup")] = None,
) -> None:
    """Convert Jira markup to Markdown."""
    if text is not None and file is not None:
        raise typer.BadParameter("Use either TEXT or --file, not both")

    if text is not None:
        content = text
    elif file is not None:
        content = file.read_text()
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        raise typer.BadParameter("Provide TEXT, --file, or pipe input via stdin")

    typer.echo(convert(content), nl=False)


def cli() -> None:
    typer.run(main)


if __name__ == "__main__":
    cli()
