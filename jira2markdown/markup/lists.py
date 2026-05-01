from __future__ import annotations

import re

from pyparsing import (
    Char,
    Combine,
    LineEnd,
    LineStart,
    Literal,
    MatchFirst,
    OneOrMore,
    Optional,
    ParserElement,
    ParseResults,
    Regex,
    SkipTo,
    StringEnd,
    Token,
)

from jira2markdown.markup.advanced import Panel
from jira2markdown.markup.base import AbstractMarkup
from jira2markdown.markup.text_effects import BlockQuote, Color


class ListIndentState:
    def __init__(self) -> None:
        self.indent: int = 0

    def reset(self) -> None:
        self.indent = 0


class ListIndent(Token):
    def __init__(self, indent_state: ListIndentState, tokens: str) -> None:
        super().__init__()
        self.indent_state = indent_state
        self.tokens = tokens

    def postParse(
        self,
        instring: str,
        loc: int,
        tokenlist: ParseResults,
    ) -> ParseResults:
        return tokenlist

    def parse_impl(self, instring: str, loc: int, do_actions: bool = True) -> tuple[int, ParseResults]:  # type: ignore[override]
        exprs = []
        for token in self.tokens:
            for indent in range(self.indent_state.indent + 1, max(0, self.indent_state.indent - 2), -1):
                exprs.append(Literal(token * indent + " "))

        loc, result = MatchFirst(exprs).parse_impl(instring, loc, do_actions)
        self.indent_state.indent = len(result[0]) - 1
        return loc, result


class List(AbstractMarkup):
    is_inline_element = False

    def __init__(
        self,
        nested_token: str,
        nested_indent: int,
        tokens: str,
        indent: int,
        bullet: str,
        *args: object,
        **kwargs: object,
    ) -> None:
        super().__init__(*args, **kwargs)  # type: ignore[arg-type]
        self.nested_token = nested_token
        self.nested_indent = nested_indent
        self.tokens = tokens
        self.indent = indent
        self.bullet = bullet
        self.indent_state = ListIndentState()

    def action(self, tokens: ParseResults) -> str:
        result = []

        for line in tokens:
            bullets, text = line.split(" ", maxsplit=1)

            nested_indent = 0
            while bullets[0] == self.nested_token:
                nested_indent += 1
                bullets = bullets[1:]

            count = nested_indent * self.nested_indent + len(bullets) * self.indent

            line_padding = " " * count
            item_padding = " " * (count - self.indent) + self.bullet + " "
            text_lines = self.markup.transform_string(text).splitlines() or [""]

            result.append(
                "\n".join(
                    [item_padding + ln if i == 0 else line_padding + ln for i, ln in enumerate(text_lines)],
                ),
            )

        self.indent_state.reset()
        text_end = "\n" if (tokens[-1][-1] == "\n") else ""
        return "\n".join(result) + text_end

    @property
    def expr(self) -> ParserElement:
        WHITESPACE = Regex(r"[ \t]+", flags=re.UNICODE)
        EOL = LineEnd()
        LIST_BREAK = EOL + Optional(WHITESPACE) + EOL | StringEnd()
        IGNORE = BlockQuote(**self.init_kwargs).expr | Panel(**self.init_kwargs).expr | Color(**self.init_kwargs).expr
        ROW = (
            LineStart()
            + Optional(WHITESPACE).suppress()
            + Combine(
                Optional(self.nested_token, default="")
                + ListIndent(self.indent_state, self.tokens)
                + SkipTo(
                    EOL + Optional(WHITESPACE) + Char(self.nested_token + self.tokens) | LIST_BREAK,
                    ignore=IGNORE,
                )
                + Optional(EOL),
            )
        )

        return OneOrMore(ROW, stop_on=LIST_BREAK).set_parse_action(self.action)


class UnorderedList(List):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(nested_token="#", nested_indent=3, tokens="*-", indent=2, bullet="-", *args, **kwargs)  # type: ignore[misc]

    def action(self, tokens: ParseResults) -> str:
        result = super().action(tokens)
        first_line = (result.splitlines() or [""])[0].strip()

        if first_line == "-":
            return "\n" + result
        else:
            return result


class OrderedList(List):
    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(nested_token="*", nested_indent=2, tokens="#", indent=3, bullet="1.", *args, **kwargs)  # type: ignore[misc]
