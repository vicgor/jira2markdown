import pytest

from jira2markdown import convert


class TestImage:
    @pytest.mark.parametrize("src,expected", [
        (
            "!http://www.example.com/image.png!",
            "![http://www.example.com/image.png](http://www.example.com/image.png)",
        ),
        ("!attached-image.gif!", "![attached-image.gif](attached-image.gif)"),
    ])
    def test_basic_conversion(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_thumbnail(self) -> None:
        assert convert("!image.jpg|thumbnail!") == "![image.jpg](image.jpg)"

    @pytest.mark.parametrize("src,expected", [
        ("Hello!image.png!", "Hello!image.png!"),
        ("Я!image.png!", "Я!image.png!"),
        ("}!image.png!", "}![image.png](image.png)"),
    ])
    def test_match_start_conditions(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_url_line_break(self) -> None:
        assert convert("!http://example.\ncom/image.png!") == "!http://example.\ncom/image.png!"

    @pytest.mark.parametrize("src,expected", [
        ("!image.jpg|width=300!", "![image.jpg](image.jpg){width=300}"),
        ("!image.jpg| WIDTH  =  300 , HEIGHT=200!", "![image.jpg](image.jpg){width=300 height=200}"),
        ("!image.jpg|align=right, vspace=4!", "![image.jpg](image.jpg)"),
    ])
    def test_image_attributes(self, src: str, expected: str) -> None:
        assert convert(src) == expected
