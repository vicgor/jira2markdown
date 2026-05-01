from pathlib import Path

import typer
from typer.testing import CliRunner

from jira2markdown.cli import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()


class TestInlineText:
    def test_bold(self) -> None:
        result = runner.invoke(app, ["*bold*"])
        assert result.exit_code == 0
        assert result.output == "**bold**"

    def test_heading(self) -> None:
        result = runner.invoke(app, ["h1. Title"])
        assert result.exit_code == 0
        assert result.output == "# Title"

    def test_link(self) -> None:
        result = runner.invoke(app, ["[Example|http://example.com]"])
        assert result.exit_code == 0
        assert result.output == "[Example](http://example.com)"


class TestFileInput:
    def test_basic(self, tmp_path: Path) -> None:
        f = tmp_path / "input.txt"
        f.write_text("*bold*")
        result = runner.invoke(app, ["-f", str(f)])
        assert result.exit_code == 0
        assert result.output == "**bold**"

    def test_multiline(self, tmp_path: Path) -> None:
        f = tmp_path / "input.txt"
        f.write_text("h1. Title\n*bold*")
        result = runner.invoke(app, ["--file", str(f)])
        assert result.exit_code == 0
        assert result.output == "# Title\n**bold**"


class TestStdinInput:
    def test_basic(self) -> None:
        result = runner.invoke(app, [], input="*bold*")
        assert result.exit_code == 0
        assert result.output == "**bold**"

    def test_multiline(self) -> None:
        result = runner.invoke(app, [], input="h1. Title\n*bold*")
        assert result.exit_code == 0
        assert result.output == "# Title\n**bold**"


class TestMutuallyExclusive:
    def test_text_and_file_fails(self, tmp_path: Path) -> None:
        f = tmp_path / "input.txt"
        f.write_text("*bold*")
        result = runner.invoke(app, ["*bold*", "-f", str(f)])
        assert result.exit_code != 0
        assert "Use either TEXT or --file" in result.output


class TestErrorHandling:
    def test_file_not_found(self) -> None:
        result = runner.invoke(app, ["-f", "/nonexistent/path.txt"])
        assert result.exit_code != 0
        assert "File not found" in result.output

    def test_file_not_found_shows_path(self) -> None:
        result = runner.invoke(app, ["-f", "/nonexistent/path.txt"])
        assert "/nonexistent/path.txt" in result.output


class TestHelpOutput:
    def test_help(self) -> None:
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Jira markup" in result.output
        assert "--file" in result.output
