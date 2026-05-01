from __future__ import annotations

from pyparsing import Keyword, LineEnd, LineStart, Optional, ParserElement, White, WordEnd, WordStart, replaceWith

from jira2markdown.markup.base import AbstractMarkup
from jira2markdown.markup.base import AbstractMarkup as _AbstractMarkup  # noqa: F401


class LineBreak(AbstractMarkup):
    @property
    def expr(self) -> ParserElement:
        return Keyword("\\\\", ident_chars="\\").set_parse_action(replaceWith("\n"))


class Ndash(AbstractMarkup):
    @property
    def expr(self) -> ParserElement:
        return WordStart() + Keyword("--", ident_chars="-").set_parse_action(replaceWith("\u2013")) + WordEnd()


class Mdash(AbstractMarkup):
    @property
    def expr(self) -> ParserElement:
        return WordStart() + Keyword("---", ident_chars="-").set_parse_action(replaceWith("\u2014")) + WordEnd()


class Ruler(AbstractMarkup):
    is_inline_element = False

    @property
    def expr(self) -> ParserElement:
        return (
            (LineStart() | LineBreak(**self.init_kwargs).expr)
            + (Optional(White()) + Keyword("----", ident_chars="-") + Optional(White())).set_parse_action(
                replaceWith("\n----"),
            )
            + LineEnd()
        )
