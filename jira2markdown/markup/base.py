from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, TypedDict

from pyparsing import Forward

if TYPE_CHECKING:
    from pyparsing import ParserElement


class MarkupContext(TypedDict):
    inline_markup: Forward
    markup: Forward
    usernames: dict[str, str]


class AbstractMarkup(ABC):
    is_inline_element: bool = True

    def __init__(
        self,
        inline_markup: Forward,
        markup: Forward,
        usernames: dict[str, str] | None = None,
    ) -> None:
        self.inline_markup = inline_markup
        self.markup = markup
        self.usernames: dict[str, str] = usernames or {}
        self.init_kwargs: MarkupContext = {
            "inline_markup": inline_markup,
            "markup": markup,
            "usernames": self.usernames,
        }

    @property
    @abstractmethod
    def expr(self) -> ParserElement: ...
