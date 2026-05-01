from jira2markdown import convert


class TestNoformat:
    def test_basic_conversion(self) -> None:
        assert convert("{noformat}preformatted piece of text{noformat}") == "```\npreformatted piece of text\n```"

    def test_multiline(self) -> None:
        assert convert("{noformat}\npreformatted piece\nof text\n{noformat}") == "```\npreformatted piece\nof text\n```"
        assert (
            convert("{noformat}\n\n\n  preformatted piece\n   of text\n\n{noformat}")
            == "```\n  preformatted piece\n   of text\n```"
        )
        assert (
            convert("{noformat}  \n  \n  preformatted piece\n   of text\n{noformat}")
            == "```\n  \n  \n  preformatted piece\n   of text\n```"
        )

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


class TestCode:
    def test_default_language(self) -> None:
        assert (
            convert(
                """
{code}
def test_code():
    assert convert(...)
{code}
""",
            )
            == """
```
def test_code():
    assert convert(...)
```
"""
        )

    def test_explicit_language(self) -> None:
        assert (
            convert(
                """
{code:xml}
    <test>
        <another tag="attribute"/>
    </test>
{code}
""",
            )
            == """
```xml
    <test>
        <another tag="attribute"/>
    </test>
```
"""
        )

    def test_decorations(self) -> None:
        assert (
            convert(
                """
{code:title=Bar.java|borderStyle=solid}
// Some comments here
public String getFoo()
{
    return foo;
}
{code}
""",
            )
            == """
```
// Some comments here
public String getFoo()
{
    return foo;
}
```
"""
        )

    def test_multiple_parameters(self) -> None:
        assert (
            convert(
                """
{code:C++|title=test.cpp}
static int x = 10;

struct Foo {
    int x;
};
{code}
""",
            )
            == """
```C++
static int x = 10;

struct Foo {
    int x;
};
```
"""
        )


class TestPanel:
    def test_basic_conversion(self) -> None:
        assert (
            convert(
                """
{panel}
  Some text
       more line
{panel}
""",
            )
            == """
> Some text
> more line
"""
        )

    def test_title(self) -> None:
        assert (
            convert(
                """
{panel:title=My Title}
Some text with a title
{panel}
""",
            )
            == """
> **My Title**
> Some text with a title
"""
        )

    def test_multiple_parameters(self) -> None:
        assert (
            convert(
                """
{panel:borderStyle=dashed|borderColor=#ccc|title=My Title|titleBGColor=#F7D6C1|bgColor=#FFFFCE}
a block of text
surrounded with a panel
{panel}
""",
            )
            == """
> **My Title**
> a block of text
> surrounded with a panel
"""
        )
