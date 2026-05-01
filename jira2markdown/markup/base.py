from __future__ import annotations

from typing import Any

from pyparsing import Forward, ParserElement, ParseResults


class AbstractMarkup:
    is_inline_element: bool = True

    def __init__(self, inline_markup: Forward, markup: Forward, usernames: dict[str, str]) -> None:
        self.inline_markup = inline_markup
        self.markup = markup
        self.usernames = usernames
        self.init_kwargs: dict[str, Any] = {
            "inline_markup": inline_markup,
            "markup": markup,
            "usernames": usernames,
        }

    def action(self, tokens: ParseResults) -> str:
        raise NotImplementedError

    @property
    def expr(self) -> ParserElement:
        raise NotImplementedError
