import pytest

from jira2markdown import convert


class TestNoformat:
    def test_basic_conversion(self) -> None:
        assert convert("{noformat}preformatted piece of text{noformat}") == "```\npreformatted piece of text\n```"

    @pytest.mark.parametrize("src,expected", [
        (
            "{noformat}\npreformatted piece\nof text\n{noformat}",
            "```\npreformatted piece\nof text\n```",
        ),
        (
            "{noformat}\n\n\n  preformatted piece\n   of text\n\n{noformat}",
            "```\n  preformatted piece\n   of text\n```",
        ),
        (
            "{noformat}  \n  \n  preformatted piece\n   of text\n{noformat}",
            "```\n  \n  \n  preformatted piece\n   of text\n```",
        ),
    ])
    def test_multiline(self, src: str, expected: str) -> None:
        assert convert(src) == expected

    def test_multiple_parameters(self) -> None:
        assert (
            convert(
                """
{noformat:borderStyle=dashed|borderColor=#ccc|title=My Title|titleBGColor=#F7D6C1|bgColor=#FFFFCE}
a block of code
surrounded with a noformat
{noformat}
""",
            )
            == """
```
a block of code
surrounded with a noformat
```
"""
        )


@pytest.mark.parametrize("src,expected", [
    (
        """
{code}
def test_code():
    assert convert(...)
{code}
""",
        """
```
def test_code():
    assert convert(...)
```
""",
        id="default_language",
    ),
    (
        """
{code:xml}
    <test>
        <another tag="attribute"/>
    </test>
{code}
""",
        """
```xml
    <test>
        <another tag="attribute"/>
    </test>
```
""",
        id="explicit_language",
    ),
    (
        """
{code:title=Bar.java|borderStyle=solid}
// Some comments here
public String getFoo()
{
    return foo;
}
{code}
""",
        """
```
// Some comments here
public String getFoo()
{
    return foo;
}
```
""",
        id="decorations_stripped",
    ),
    (
        """
{code:C++|title=test.cpp}
static int x = 10;

struct Foo {
    int x;
};
{code}
""",
        """
```C++
static int x = 10;

struct Foo {
    int x;
};
```
""",
        id="multiple_parameters",
    ),
])
def test_code(src: str, expected: str) -> None:
    assert convert(src) == expected


@pytest.mark.parametrize("src,expected", [
    (
        """
{panel}
  Some text
       more line
{panel}
""",
        """
> Some text
> more line
""",
        id="basic",
    ),
    (
        """
{panel:title=My Title}
Some text with a title
{panel}
""",
        """
> **My Title**
> Some text with a title
""",
        id="with_title",
    ),
    (
        """
{panel:borderStyle=dashed|borderColor=#ccc|title=My Title|titleBGColor=#F7D6C1|bgColor=#FFFFCE}
a block of text
surrounded with a panel
{panel}
""",
        """
> **My Title**
> a block of text
> surrounded with a panel
""",
        id="multiple_parameters",
    ),
])
def test_panel(src: str, expected: str) -> None:
    assert convert(src) == expected
