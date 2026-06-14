"""Direct unit tests for convert() — independent of CLI layer."""

import pytest

from jira2markdown import MarkupElements, convert
from jira2markdown.markup.text_effects import Bold


class TestConvertBasic:
    def test_empty_string(self) -> None:
        assert convert("") == ""

    def test_plain_text_passthrough(self) -> None:
        assert convert("hello world") == "hello world"

    def test_bold(self) -> None:
        assert convert("*bold*") == "**bold**"

    def test_heading_h1(self) -> None:
        assert convert("h1. Title") == "# Title"

    def test_heading_h3(self) -> None:
        assert convert("h3. Section") == "### Section"

    def test_monospaced(self) -> None:
        assert convert("{{code}}") == "`code`"

    def test_strikethrough(self) -> None:
        assert convert("-deleted-") == "~~deleted~~"

    def test_link_with_alias(self) -> None:
        assert convert("[Example|https://example.com]") == "[Example](https://example.com)"

    def test_link_bare_url(self) -> None:
        assert convert("[https://example.com]") == "<https://example.com>"

    def test_inline_code(self) -> None:
        assert convert("{code}print('hi'){code}") == "```\nprint('hi')\n```"

    def test_ndash(self) -> None:
        assert convert("foo -- bar") == "foo \u2013 bar"

    def test_mdash(self) -> None:
        assert convert("foo --- bar") == "foo \u2014 bar"


class TestConvertUsernames:
    def test_mention_with_mapping(self) -> None:
        result = convert("[~accountid:abc123]", usernames={"abc123": "alice"})
        assert result == "@alice"

    def test_mention_without_mapping(self) -> None:
        result = convert("[~accountid:abc123]")
        assert result == "@abc123"


class TestConvertCustomElements:
    def test_custom_elements_subset(self) -> None:
        """Only Bold is active — heading should pass through unchanged."""
        elements = MarkupElements([Bold])
        result = convert("h1. Title", elements=elements)
        assert result == "h1. Title"

    def test_custom_elements_bold_only(self) -> None:
        elements = MarkupElements([Bold])
        assert convert("*bold*", elements=elements) == "**bold**"

    def test_remove_bold_leaves_asterisks(self) -> None:
        """After removing Bold, asterisks are escaped by EscSpecialChars."""
        elements = MarkupElements()
        elements.remove(Bold)
        result = convert("*not bold*", elements=elements)
        assert result == r"\*not bold\*"


class TestConvertEdgeCases:
    def test_multiline(self) -> None:
        result = convert("h1. Title\n*bold*")
        assert result == "# Title\n**bold**"

    def test_table(self) -> None:
        jira = "||col1||col2||\n|a|b|"
        md = convert(jira)
        assert "|col1|col2|" in md
        assert "|---|" in md

    def test_code_block_with_language(self) -> None:
        result = convert("{code:python}\nx = 1\n{code}")
        assert result == "```python\nx = 1\n```"

    def test_nested_unordered_list(self) -> None:
        jira = "* item\n** nested"
        result = convert(jira)
        assert "- item" in result
        assert "- nested" in result

    @pytest.mark.parametrize(
        ("jira", "expected"),
        [
            ("h1. A", "# A"),
            ("h2. B", "## B"),
            ("h6. F", "###### F"),
            ("*x*", "**x**"),
            ("-x-", "~~x~~"),
            ("{{x}}", "`x`"),
        ],
    )
    def test_parametrized_conversions(self, jira: str, expected: str) -> None:
        assert convert(jira) == expected
