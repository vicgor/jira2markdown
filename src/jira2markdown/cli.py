import signal
import sys
from pathlib import Path  # noqa: TC003
from typing import Annotated

try:
    import typer
except ImportError as exc:
    raise SystemExit(
        "The jira2markdown CLI requires extra dependencies.\nInstall them with: pip install jira2markdown[cli]",
    ) from exc

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
        typer.echo("Error: Use either TEXT or --file, not both")
        raise typer.Exit(code=2)

    if text is not None:
        content = text
    elif file is not None:
        try:
            content = file.read_text()
        except FileNotFoundError:
            typer.echo(f"Error: File not found: {file}")
            raise typer.Exit(code=2)
    elif not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        typer.echo("Error: Provide TEXT, --file, or pipe input via stdin")
        raise typer.Exit(code=2)

    result = convert(content)
    if output is not None:
        try:
            output.write_text(result, encoding="utf-8")
        except OSError as exc:
            typer.echo(f"Error: Cannot write to {output}: {exc}")
            raise typer.Exit(code=2)
    else:
        typer.echo(result, nl=False)


def cli() -> None:
    typer.run(main)


if __name__ == "__main__":
    cli()
