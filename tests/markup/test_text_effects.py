import pytest

from jira2markdown.parser import convert


class TestBold:
    def test_basic_conversion(self) -> None:
        assert convert("inside *some long* text") == "inside **some long** text"

    @pytest.mark.parametrize("src,expected", [
        ("*start string end*", "**start string end**"),
        ("\n*start line end*\n", "\n**start line end**\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("start * spacing*", r"start \* spacing\*"),
        ("pre*bold*", r"pre\*bold\*"),
        ("Я*bold*", r"Я\*bold\*"),
        ("!*bold*", "!**bold**"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("*bold *", r"\*bold \*"),
        ("*word*connector", r"\*word\*connector"),
        ("*skip *spacing * chars*", r"**skip \*spacing \* chars**"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("*multiline\nbold*") == "\\*multiline\nbold\\*"

    def test_single_token(self) -> None:
        assert convert("single *char") == r"single \*char"

    @pytest.mark.parametrize("src,expected", [
        ("*some**text*", "**some** **text**"),
        ("*some*   *text*", "**some**   **text**"),
        ("**text**", r"\***text**\*"),
        ("**some****text**", r"\***some**\*\***text**\*"),
    ])
    def test_adjacent_tokens(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("**", r"\*\*"),
        ("***", r"\*\*\*"),
    ])
    def test_empty_text(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestStrikethrough:
    def test_basic_conversion(self) -> None:
        assert convert("inside -some long- text") == "inside ~~some long~~ text"

    @pytest.mark.parametrize("src,expected", [
        ("-start string end-", "~~start string end~~"),
        ("\n-start line end-\n", "\n~~start line end~~\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("no - space after start-", "no - space after start-"),
        ("word-connector- markup", "word-connector- markup"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("-text -", "-text -"),
        ("-word-connector", "-word-connector"),
        ("-skip -spacing - chars-", "~~skip -spacing - chars~~"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("-multiline\nstrikethrough-") == "-multiline\nstrikethrough-"

    @pytest.mark.parametrize("src,expected", [
        ("-some--text-", "~~some~~ ~~text~~"),
        ("-some-   -text-", "~~some~~   ~~text~~"),
        ("--text--", "-~~text~~-"),
        ("--some----text--", "-~~some~~--~~text~~-"),
    ])
    def test_adjacent_tokens(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestUnderline:
    def test_basic_conversion(self) -> None:
        assert convert("inside +some long+ text") == "inside <u>some long</u> text"

    @pytest.mark.parametrize("src,expected", [
        ("+start string end+", "<u>start string end</u>"),
        ("\n+start line end+\n", "\n<u>start line end</u>\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("no + space after start+", "no + space after start+"),
        ("word+connector+ markup", "word+connector+ markup"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("+text +", "+text +"),
        ("+word+connector", "+word+connector"),
        ("+skip +spacing + char+", "<u>skip +spacing + char</u>"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("+multiline\nunderline+") == "+multiline\nunderline+"


class TestInlineQuote:
    def test_basic_conversion(self) -> None:
        assert convert("inside ??some long?? text") == "inside <q>some long</q> text"

    @pytest.mark.parametrize("src,expected", [
        ("??start string end??", "<q>start string end</q>"),
        ("\n??start string end??\n", "\n<q>start string end</q>\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("no ?? space after start??", "no ?? space after start??"),
        ("word??connector?? markup", "word??connector?? markup"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("??text ??", "??text ??"),
        ("??word??connector", "??word??connector"),
        ("??skip ??spacing ?? char??", "<q>skip ??spacing ?? char</q>"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("??multiline\nunderline??") == "??multiline\nunderline??"

    @pytest.mark.parametrize("src,expected", [
        ("??some????text??", "<q>some</q> <q>text</q>"),
        ("??some??   ??text??", "<q>some</q>   <q>text</q>"),
        ("????text????", "??<q>text</q>??"),
        ("????some????????text????", "??<q>some</q>????<q>text</q>??"),
    ])
    def test_adjacent_tokens(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestSuperscript:
    def test_basic_conversion(self) -> None:
        assert convert("inside ^some long^ text") == "inside <sup>some long</sup> text"

    @pytest.mark.parametrize("src,expected", [
        ("^start string end^", "<sup>start string end</sup>"),
        ("\n^start line end^\n", "\n<sup>start line end</sup>\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("no ^ space after start^", "no ^ space after start^"),
        ("word^connector^ markup", "word^connector^ markup"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("^text ^", "^text ^"),
        ("^word^connector", "^word^connector"),
        ("^skip ^spacing ^ char^", "<sup>skip ^spacing ^ char</sup>"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("^multiline\nunderline^") == "^multiline\nunderline^"

    @pytest.mark.parametrize("src,expected", [
        ("^some^^text^", "<sup>some</sup> <sup>text</sup>"),
        ("^some^   ^text^", "<sup>some</sup>   <sup>text</sup>"),
        ("^^text^^", "^<sup>text</sup>^"),
        ("^^some^^^^text^^", "^<sup>some</sup>^^<sup>text</sup>^"),
    ])
    def test_adjacent_tokens(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestSubscript:
    def test_basic_conversion(self) -> None:
        assert convert("inside ~some long~ text") == "inside <sub>some long</sub> text"

    @pytest.mark.parametrize("src,expected", [
        ("~start string end~", "<sub>start string end</sub>"),
        ("\n~start line end~\n", "\n<sub>start line end</sub>\n"),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("no ~ space after start~", "no ~ space after start~"),
        ("word~connector~ markup", "word~connector~ markup"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("~text ~", "~text ~"),
        ("~word~connector", "~word~connector"),
        ("~skip ~spacing ~ char~", "<sub>skip ~spacing ~ char</sub>"),
    ])
    def test_match_end_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiline(self) -> None:
        assert convert("~multiline\nunderline~") == "~multiline\nunderline~"

    @pytest.mark.parametrize("src,expected", [
        ("~some~~text~", "<sub>some</sub> <sub>text</sub>"),
        ("~some~   ~text~", "<sub>some</sub>   <sub>text</sub>"),
        ("~~text~~", "~<sub>text</sub>~"),
        ("~~some~~~~text~~", "~<sub>some</sub>~~<sub>text</sub>~"),
    ])
    def test_adjacent_tokens(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestColor:
    @pytest.mark.parametrize("src,expected", [
        (
            "start {color:#0077ff}hex color{color} text",
            'start <font color="#0077ff">hex color</font> text',
            id="hex_color",
        ),
        (
            "start {color:red}named color{color} text",
            'start <font color="red">named color</font> text',
            id="named_color",
        ),
        (
            "start {color:rgba(255, 127, 63, 0.3)}rgba color{color} text",
            'start <font color="#ff7f3f">rgba color</font> text',
            id="rgba_color",
        ),
    ])
    def test_color_value(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("{color:rgba(255,0,0,1)}x{color}", '<font color="#ff0000">x</font>'),
        ("{color:rgba(0,255,0,1)}x{color}", '<font color="#00ff00">x</font>'),
        ("{color:rgba(0,0,255,1)}x{color}", '<font color="#0000ff">x</font>'),
        ("{color:rgba(0,0,0,1)}x{color}", '<font color="#000000">x</font>'),
    ])
    def test_rgba_zero_padding(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        (
            "{color:#0077ff}colored{color}",
            '<font color="#0077ff">colored</font>',
            id="no_newlines",
        ),
        (
            "\n{color:#0077ff}colored{color}\n",
            '\n<font color="#0077ff">colored</font>\n',
            id="with_newlines",
        ),
    ])
    def test_line_endings(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_empty_text(self) -> None:
        assert convert("{color:#0077ff} {color}") == " "
        assert convert("{color:black}\n{color}") == "\n"

    def test_multiline(self) -> None:
        assert (
            convert(
                """
        {color:red}
            look ma, red text!
        {color}
        """,
            )
            == """
        <font color="red">
            look ma, red text!
        </font>
        """
        )


class TestQuote:
    def test_basic_conversion(self) -> None:
        assert convert("bq. Some quote") == "> Some quote"

    @pytest.mark.parametrize("src,expected", [
        ("  bq. Some quote", "  > Some quote"),
        ("text  bq. Some quote", "text  bq. Some quote"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_adjacent_text(self) -> None:
        assert (
            convert(
                """
Preceding line
bq. First quote
bq. Second quote
Next line
""",
            )
            == """
Preceding line
> First quote
> Second quote

Next line
"""
        )


class TestBlockQuote:
    def test_basic_conversion(self) -> None:
        assert (
            convert(
                """
{quote}
    here is quotable
        content to be quoted
{quote}
""",
            )
            == """
> here is quotable
> content to be quoted
"""
        )


class TestMonospaced:
    def test_basic_conversion(self) -> None:
        assert convert("{{some text inside}}") == "`some text inside`"
