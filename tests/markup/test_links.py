import pytest

from jira2markdown.parser import convert

_USERNAMES: dict[str, str] = {"100:internal-id": "elliot"}


class TestMailTo:
    def test_basic_conversion(self) -> None:
        assert convert("[mailto:box@example.com]") == "<box@example.com>"

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("[box@example.com|mailto:box@example.com]", "<box@example.com>"),
            ("[Some text|mailto:home_box@domain-name.com]", "[Some text](mailto:home_box@domain-name.com)"),
        ],
    )
    def test_alias(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestLink:
    @pytest.mark.parametrize(
        "src,expected",
        [
            ("[http://example.com]", "<http://example.com>"),
            ("[ftp://example.com]", "<ftp://example.com>"),
            ("[WWW.EXAMPLE.COM]", "<https://WWW.EXAMPLE.COM>"),
        ],
    )
    def test_basic_conversion(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_alias(self) -> None:
        assert convert("[Example text|http://example.com]") == "[Example text](http://example.com)"

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("[Text in square brackets]", "[Text in square brackets]"),
            ("[Some text|]", r"[Some text\|]"),
            ("[Some text|More text]", r"[Some text\|More text]"),
        ],
    )
    def test_text(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestAttachment:
    def test_basic_conversion(self) -> None:
        assert convert("[^attachment.ext]") == "[attachment.ext](attachment.ext)"


class TestMention:
    USERNAMES = {
        "100:internal-id": "elliot",
    }

    @pytest.mark.parametrize("src,expected", [
        ("[~100:internal-id]", "@100:internal-id", id="without_usernames"),
        ("[~100:internal-id]", "@elliot", id="with_usernames"),
    ])
    def test_basic_conversion(self, src: str, expected: str) -> None:
        usernames = self.USERNAMES if expected == "@elliot" else None
        assert convert(src, usernames) == expected

    @pytest.mark.parametrize("src,expected", [
        ("[~accountId:100:internal-id]", "@100:internal-id", id="without_usernames"),
        ("[~accountid:100:internal-id]", "@elliot", id="with_usernames"),
    ])
    def test_prefix(self, src: str, expected: str) -> None:
        usernames = self.USERNAMES if expected == "@elliot" else None
        assert convert(src, usernames) == expected

    @pytest.mark.parametrize("src,expected", [
        ("[Firstname Lastname|~accountid:100:internal-id]", "@100:internal-id", id="without_usernames"),
        ("[Firstname Lastname|~accountid:100:internal-id]", "@elliot", id="with_usernames"),
    ])
    def test_alias(self, src: str, expected: str) -> None:
        usernames = self.USERNAMES if expected == "@elliot" else None
        assert convert(src, usernames) == expected

    @pytest.mark.parametrize("src,expected", [
        ("text[~userA]", "text @userA"),
        ("[~userA]text", "@userA text"),
        ("[~userA][~userB]", "@userA @userB"),
        ("[~userA] [~userB]", "@userA @userB"),
        ("[~userA]\t[~userB]", "@userA\t@userB"),
        ("[~userA]\n[~userB]", "@userA\n@userB"),
    ])
    def test_spacing(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("[~userA].", "@userA."),
        ("[~userA]:", "@userA:"),
        ("[~userA]?", "@userA?"),
    ])
    def test_punctuation(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize(
        "src,expected",
        [
            ("([~userA])", "(@userA)"),
            (",[ ~userA],", ",@userA,"),
            (";[~userA]", ";@userA"),
        ],
    )
    def test_preceding_punctuation(self, src: str, expected: str) -> None:
        assert convert(src) == expected
