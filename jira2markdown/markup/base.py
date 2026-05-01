from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyparsing import Forward, ParserElement


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
        self.init_kwargs: dict[str, Any] = {
            "inline_markup": inline_markup,
            "markup": markup,
            "usernames": self.usernames,
        }

    @property
    @abstractmethod
    def expr(self) -> ParserElement: ...
