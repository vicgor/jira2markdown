import pytest

from jira2markdown.parser import convert

_USERNAMES: dict[str, str] = {"100:internal-id": "elliot"}


class TestMailTo:
    def test_basic_conversion(self) -> None:
        assert convert("[mailto:box@example.com]") == "<box@example.com>"

    @pytest.mark.parametrize("src,expected", [
        ("[box@example.com|mailto:box@example.com]", "<box@example.com>"),
        ("[Some text|mailto:home_box@domain-name.com]", "[Some text](mailto:home_box@domain-name.com)"),
    ])
    def test_alias(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestLink:
    @pytest.mark.parametrize("src,expected", [
        ("[http://example.com]", "<http://example.com>"),
        ("[ftp://example.com]", "<ftp://example.com>"),
        ("[WWW.EXAMPLE.COM]", "<https://WWW.EXAMPLE.COM>"),
    ])
    def test_basic_conversion(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_alias(self) -> None:
        assert convert("[Example text|http://example.com]") == "[Example text](http://example.com)"

    @pytest.mark.parametrize("src,expected", [
        ("[Text in square brackets]", "[Text in square brackets]"),
        ("[Some text|]", r"[Some text\|]"),
        ("[Some text|More text]", r"[Some text\|More text]"),
    ])
    def test_text(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestAttachment:
    def test_basic_conversion(self) -> None:
        assert convert("[^attachment.ext]") == "[attachment.ext](attachment.ext)"


class TestMention:
    USERNAMES = {
        "100:internal-id": "elliot",
    }

    def test_basic_conversion(self) -> None:
        assert convert("[~100:internal-id]") == "@100:internal-id"
        assert convert("[~100:internal-id]", self.USERNAMES) == "@elliot"

    def test_prefix(self) -> None:
        assert convert("[~accountId:100:internal-id]") == "@100:internal-id"
        assert convert("[~accountid:100:internal-id]", self.USERNAMES) == "@elliot"

    def test_alias(self) -> None:
        assert convert("[Firstname Lastname|~accountid:100:internal-id]") == "@100:internal-id"
        assert convert("[Firstname Lastname|~accountid:100:internal-id]", self.USERNAMES) == "@elliot"

    def test_spacing(self) -> None:
        assert convert("text[~userA]") == "text @userA"
        assert convert("[~userA]text") == "@userA text"
        assert convert("[~userA][~userB]") == "@userA @userB"
        assert convert("[~userA] [~userB]") == "@userA @userB"
        assert convert("[~userA]\t[~userB]") == "@userA\t@userB"
        assert convert("[~userA]\n[~userB]") == "@userA\n@userB"

    def test_punctuation(self) -> None:
        assert convert("[~userA].") == "@userA."
        assert convert("[~userA]:") == "@userA:"
        assert convert("[~userA]?") == "@userA?"
    @pytest.mark.parametrize("src,expected", [
        ("([~userA])", "(@userA)"),
        (",[~userA],", ",@userA,"),
        (";[~userA]", ";@userA"),
    ])
    def test_preceding_punctuation(self, src: str, expected: str) -> None:
        assert convert(src) == expected
