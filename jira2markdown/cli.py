import signal
import sys
from pathlib import Path  # noqa: TC003
from typing import Annotated

try:
    import typer
except ImportError:
    raise SystemExit(
        "The jira2markdown CLI requires extra dependencies.\n"
        "Install them with: pip install jira2markdown[cli]"
    )

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
    output: Annotated[Path | None, typer.Option("-o", "--output", help="Write output to file")] = None,
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

    result = convert(content)
    if output is not None:
        try:
            output.write_text(result)
        except OSError as exc:
            raise typer.BadParameter(f"Cannot write to {output}: {exc}", param_hint="'--output'") from exc
    else:
        typer.echo(result, nl=False)


def cli() -> None:
    typer.run(main)


if __name__ == "__main__":
    cli()
