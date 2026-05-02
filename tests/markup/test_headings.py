import pytest

from jira2markdown.parser import convert


@pytest.mark.parametrize("src,expected", [
    ("h1. Title text", "# Title text"),
    ("h6. Title", "###### Title"),
    ("h7. Title", "h7. Title"),
    ("  h2. Title", "  ## Title"),
    (" A  h2. Title", " A  h2. Title"),
])
def test_headings(src: str, expected: str) -> None:
    assert convert(src) == expected
