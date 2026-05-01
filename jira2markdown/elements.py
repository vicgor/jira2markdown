from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING

from pyparsing import Forward, MatchFirst, ParseExpression

from jira2markdown.markup.advanced import Code, Noformat, Panel
from jira2markdown.markup.base import AbstractMarkup
from jira2markdown.markup.headings import Headings
from jira2markdown.markup.images import Image
from jira2markdown.markup.links import Attachment, Link, MailTo, Mention
from jira2markdown.markup.lists import OrderedList, UnorderedList
from jira2markdown.markup.tables import Table
from jira2markdown.markup.text_breaks import LineBreak, Mdash, Ndash, Ruler
from jira2markdown.markup.text_effects import (
    BlockQuote,
    Bold,
    Color,
    EscSpecialChars,
    InlineQuote,
    Monospaced,
    Quote,
    Strikethrough,
    Subscript,
    Superscript,
    Underline,
)

if TYPE_CHECKING:
    pass

_DEFAULT_ELEMENTS: list[type[AbstractMarkup]] = [
    UnorderedList,
    OrderedList,
    Code,
    Noformat,
    Monospaced,
    Mention,
    MailTo,
    Attachment,
    Link,
    Image,
    Table,
    Headings,
    Quote,
    BlockQuote,
    Panel,
    Bold,
    Ndash,
    Mdash,
    Ruler,
    Strikethrough,
    Underline,
    InlineQuote,
    Superscript,
    Subscript,
    Color,
    LineBreak,
    EscSpecialChars,
]


class MarkupElements:
    """Ordered, typed container for markup element classes."""

    def __init__(self, elements: list[type[AbstractMarkup]] | None = None) -> None:
        self._elements: list[type[AbstractMarkup]] = list(elements or _DEFAULT_ELEMENTS)

    def __iter__(self) -> Iterator[type[AbstractMarkup]]:
        return iter(self._elements)

    def __len__(self) -> int:
        return len(self._elements)

    def insert_after(
        self,
        element: type[AbstractMarkup],
        new_element: type[AbstractMarkup],
    ) -> None:
        index = self._elements.index(element)
        self._elements.insert(index + 1, new_element)

    def replace(
        self,
        old_element: type[AbstractMarkup],
        new_element: type[AbstractMarkup],
    ) -> None:
        index = self._elements.index(old_element)
        self._elements[index] = new_element

    def expr(
        self,
        inline_markup: Forward,
        markup: Forward,
        usernames: dict[str, str],
        elements: Iterable[type[AbstractMarkup]],
    ) -> ParseExpression:
        return MatchFirst(
            [
                element(inline_markup=inline_markup, markup=markup, usernames=usernames).expr
                for element in elements
            ],
        )
