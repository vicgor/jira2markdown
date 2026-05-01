from pyparsing import Forward, ParserElement

from jira2markdown.elements import MarkupElements
from jira2markdown.markup.base import AbstractMarkup


def _make_stub(name: str) -> type[AbstractMarkup]:
    """Create a minimal concrete AbstractMarkup subclass for testing."""

    def expr(self: AbstractMarkup) -> ParserElement:
        return Forward()

    return type(name, (AbstractMarkup,), {"expr": property(expr)})


ElementA = _make_stub("ElementA")
ElementB = _make_stub("ElementB")
ElementC = _make_stub("ElementC")


class TestMarkupElements:
    def test_insert_after(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        elements.insert_after(ElementA, ElementC)
        assert list(elements) == [ElementA, ElementC, ElementB]

    def test_replace(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        elements.replace(ElementB, ElementC)
        assert list(elements) == [ElementA, ElementC]
