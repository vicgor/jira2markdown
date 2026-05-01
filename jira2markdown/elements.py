from __future__ import annotations

from collections.abc import Iterable

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


class MarkupElements(list[type[AbstractMarkup]]):
    def __init__(self, seq: Iterable[type[AbstractMarkup]] | None = None) -> None:
        super().__init__(seq if seq is not None else _DEFAULT_ELEMENTS)

    def insert_after(
        self,
        element: type[AbstractMarkup],
        new_element: type[AbstractMarkup],
    ) -> None:
        index = self.index(element)
        self.insert(index + 1, new_element)

    def replace(
        self,
        old_element: type[AbstractMarkup],
        new_element: type[AbstractMarkup],
    ) -> None:
        index = self.index(old_element)
        self[index] = new_element

    def expr(
        self,
        inline_markup: Forward,
        markup: Forward,
        usernames: dict[str, str],
        elements: Iterable[type[AbstractMarkup]],
    ) -> ParseExpression:
        return MatchFirst(
            [
                element(
                    inline_markup=inline_markup,
                    markup=markup,
                    usernames=usernames,
                ).expr
                for element in elements
            ],
        )
