import signal
import sys
from pathlib import Path  # noqa: TC003
from typing import Annotated

import typer

from jira2markdown import convert

# Let the OS handle SIGPIPE (e.g. jira2markdown -f big.txt | head)
# instead of Python printing an unhandled BrokenPipeError traceback.
# AttributeError guard: Windows has no SIGPIPE.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except AttributeError:
    pass


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
        try:
            content = file.read_text()
        except FileNotFoundError:
            raise typer.BadParameter(f"File not found: {file}", param_hint="'--file'")
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        raise typer.BadParameter("Provide TEXT, --file, or pipe input via stdin")

    typer.echo(convert(content), nl=False)


def cli() -> None:
    typer.run(main)


if __name__ == "__main__":
    cli()
