from __future__ import annotations

from pyparsing import Forward, ParserElement

from jira2markdown.elements import MarkupElements

ParserElement.set_default_whitespace_chars("")


def convert(text: str, usernames: dict[str, str] | None = None, elements: MarkupElements | None = None) -> str:
    usernames = usernames or {}
    elements = elements or MarkupElements()

    inline_markup = Forward()
    markup = Forward()

    inline_markup << elements.expr(inline_markup, markup, usernames, filter(lambda e: e.is_inline_element, elements))
    markup << elements.expr(inline_markup, markup, usernames, elements)

    return markup.transform_string(text)
