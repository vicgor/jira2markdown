import pytest

from jira2markdown.parser import convert


class TestLineBreak:
    def test_word_break(self) -> None:
        assert convert("abc\\\\def") == "abc\ndef"


class TestNdash:
    @pytest.mark.parametrize("src,expected", [
        ("--", "–"),
        ("abc -- def", "abc – def"),
    ])
    def test_basic_conversion(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("abc--def", "abc--def"),
        ("abc --def", "abc --def"),
        ("abc-- def", "abc-- def"),
    ])
    def test_word_connections(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestMdash:
    @pytest.mark.parametrize("src,expected", [
        ("---", "—"),
        ("abc --- def", "abc — def"),
    ])
    def test_basic_conversion(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    @pytest.mark.parametrize("src,expected", [
        ("abc---def", "abc---def"),
        ("abc ---def", "abc ---def"),
        ("abc--- def", "abc--- def"),
    ])
    def test_word_connections(self, src: str, expected: str) -> None:
        assert convert(src) == expected


class TestRuler:
    def test_basic_conversion(self) -> None:
        assert convert("----") == "\n----"

    def test_indent(self) -> None:
        assert convert(" ---- ") == "\n----"

    @pytest.mark.parametrize("src,expected", [
        ("abc----def", "abc----def"),
        ("abc ----def", "abc ----def"),
        ("abc---- def", "abc---- def"),
        ("abc ---- def", "abc ---- def"),
        ("abc ---- ", "abc ---- "),
        (" ---- def", " ---- def"),
    ])
    def test_word_connections(self, src: str, expected: str) -> None:
        assert convert(src) == expected
