from __future__ import annotations

from pyparsing import Forward, ParserElement

from jira2markdown.elements import MarkupElements

ParserElement.set_default_whitespace_chars("")


def convert(
    text: str,
    usernames: dict[str, str] | None = None,
    elements: MarkupElements | None = None,
) -> str:
    _usernames: dict[str, str] = usernames or {}
    _elements: MarkupElements = elements or MarkupElements()

    inline_markup = Forward()
    markup = Forward()

    inline_markup <<= _elements.expr(
        inline_markup,
        markup,
        _usernames,
        filter(lambda e: e.is_inline_element, _elements),
    )
    markup <<= _elements.expr(inline_markup, markup, _usernames, _elements)

    return markup.transform_string(text)
