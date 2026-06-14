import pytest
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

    def test_remove(self) -> None:
        elements = MarkupElements([ElementA, ElementB, ElementC])
        elements.remove(ElementB)
        assert list(elements) == [ElementA, ElementC]

    def test_remove_first(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        elements.remove(ElementA)
        assert list(elements) == [ElementB]

    def test_remove_last(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        elements.remove(ElementB)
        assert list(elements) == [ElementA]

    def test_remove_unknown_raises(self) -> None:
        elements = MarkupElements([ElementA])
        with pytest.raises(ValueError, match="ElementC"):
            elements.remove(ElementC)

    def test_len(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        assert len(elements) == 2

    def test_default_elements_nonempty(self) -> None:
        elements = MarkupElements()
        assert len(elements) > 0

    def test_iter(self) -> None:
        elements = MarkupElements([ElementA, ElementB])
        assert list(elements) == [ElementA, ElementB]
