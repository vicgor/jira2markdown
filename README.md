# jira2markdown

> **Fork of [catcombo/jira2markdown](https://github.com/catcombo/jira2markdown)** with improvements for use in [jira-cli](https://github.com/vicgor/jira-cli): stricter typing, `uv` compatibility, and `Typer`-based CLI.

`jira2markdown` converts [Jira markup](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all) to [Markdown](https://spec.commonmark.org/) using parsing expression grammars (pyparsing). The Markdown output follows the [CommonMark specification](https://spec.commonmark.org/) with extensions, making it compatible with YouTrack, GitHub, GitLab, and most other Markdown renderers.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Command Line Tool](#command-line-tool)
- [Python API](#python-api)
- [Customization](#customization)
- [Conversion Tables](#conversion-tables)
  - [Headings](#headings)
  - [Text Effects](#text-effects)
  - [Text Breaks](#text-breaks)
  - [Links](#links)
  - [Lists](#lists)
  - [Images](#images)
  - [Tables](#tables)
  - [Advanced Formatting](#advanced-formatting)
- [Development](#development)
- [Running Tests](#running-tests)

---

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended for dependency management)

---

## Installation

### Via pip

```bash
pip install jira2markdown
```

### Via uv (recommended for jira-cli projects)

```bash
uv add jira2markdown
```

### Via pipx (isolated CLI install)

```bash
pipx install jira2markdown
```

---

## Command Line Tool

Three input modes are supported:

```bash
# 1. Inline text argument
jira2markdown "{quote}So many books, so little time{quote}"

# 2. File input
jira2markdown -f path/to/file.txt

# 3. Stdin (pipe)
echo "{quote}So many books, so little time{quote}" | jira2markdown
```

---

## Python API

```python
from jira2markdown import convert

# Basic conversion
convert("Some *Jira text* formatting [example|https://example.com].")
# >>> Some **Jira text** formatting [example](https://example.com).

# User mention mapping: Jira account id → username
convert(
    "[Winston Smith|~accountid:internal-id] woke up with the word 'Shakespeare' on his lips",
    usernames={"internal-id": "winston"},
)
# >>> @winston woke up with the word 'Shakespeare' on his lips
```

---

## Customization

Pass a custom `MarkupElements` list to control which elements are converted:

```python
from jira2markdown import convert
from jira2markdown.elements import MarkupElements
from jira2markdown.markup.links import Link
from jira2markdown.markup.text_effects import Bold

# Only Bold and Link tokens will be converted
elements = MarkupElements([Link, Bold])
convert("Some Jira text here", elements=elements)
```

> **Note:** The order of elements matters — elements match top-to-bottom.

Use `insert_after` / `replace` to override individual elements in the default list:

```python
from jira2markdown import convert
from jira2markdown.elements import MarkupElements
from jira2markdown.markup.base import AbstractMarkup
from jira2markdown.markup.links import Link
from jira2markdown.markup.text_effects import Color

class CustomColor(Color):
    ...

class MyElement(AbstractMarkup):
    ...

elements = MarkupElements()
elements.replace(Color, CustomColor)
elements.insert_after(Link, MyElement)
convert("Some Jira text here", elements=elements)
```

---

## Conversion Tables

### Headings

| Jira | Markdown |
|------|----------|
| `h1. Biggest heading` | `# Biggest heading` |
| `h2. Bigger heading` | `## Bigger heading` |
| `h3. Big heading` | `### Big heading` |
| `h4. Normal heading` | `#### Normal heading` |
| `h5. Small heading` | `##### Small heading` |
| `h6. Smallest heading` | `###### Smallest heading` |

### Text Effects

| Jira | Markdown |
|------|----------|
| `*strong*` | `**strong**` |
| `_emphasis_` | Not converted (same syntax) |
| `??citation??` | `<q>citation</q>` |
| `-deleted-` | `~~deleted~~` |
| `+inserted+` | `inserted` |
| `^superscript^` | `<sup>superscript</sup>` |
| `~subscript~` | `<sub>subscript</sub>` |
| `{{monospaced}}` | `` `monospaced` `` |
| `bq. Some block quoted text` | `> Some block quoted text` |
| `{quote}Content{quote}` | `> Content` |
| `{color:red}red text!{color}` | `<font color="red">red text!</font>` |

### Text Breaks

| Jira | Markdown |
|------|----------|
| `\\` | Line break |
| `---` | `—` |
| `--` | `–` |

### Links

| Jira | Markdown |
|------|----------|
| `[#anchor]` | Not converted |
| `[^attachment.ext]` | `[attachment.ext](attachment.ext)` |
| `[http://www.example.com]` | `<http://www.example.com>` |
| `[Example\|http://example.com]` | `[Example](http://example.com)` |
| `[mailto:box@example.com]` | `<box@example.com>` |
| `[file:///c:/temp/foo.txt]` | Not converted |
| `{anchor:anchorname}` | Not converted |
| `[~username]` | `@username` |

### Lists

<table>
<tr><th>Jira</th><th>Markdown</th></tr>
<tr>
<td>

```
* some
* bullet
** indented
** bullets
* points
```
</td>
<td>

```
- some
- bullet
  - indented
  - bullets
- points
```
</td>
</tr>
<tr>
<td>

```
# a
# numbered
# list
```
</td>
<td>

```
1. a
1. numbered
1. list
```
</td>
</tr>
<tr>
<td>

```
# a
# numbered
#* with
#* nested
#* bullet
# list
```
</td>
<td>

```
1. a
1. numbered
   - with
   - nested
   - bullet
1. list
```
</td>
</tr>
<tr>
<td>

```
* a
* bulleted
*# with
*# nested
*# numbered
* list
```
</td>
<td>

```
- a
- bulleted
  1. with
  1. nested
  1. numbered
- list
```
</td>
</tr>
</table>

### Images

<table>
<tr><th>Jira</th><th>Markdown</th></tr>
<tr>
<td>

```
!image.jpg!
!image.jpg|thumbnail!
!image.gif|align=right, vspace=4!
```
</td>
<td>

```
![image.jpg](image.jpg)
```
</td>
</tr>
<tr>
<td>

```
!image.jpg|width=300, height=200!
```
</td>
<td>

```
![image.jpg](image.jpg){width=300 height=200}
```
</td>
</tr>
</table>

### Tables

<table>
<tr><th>Jira</th><th>Markdown</th></tr>
<tr>
<td>

```
||heading 1||heading 2||heading 3||
|col A1|col A2|col A3|
|col B1|col B2|col B3|
```
</td>
<td>

```
|heading 1|heading 2|heading 3|
|---|---|---|
|col A1|col A2|col A3|
|col B1|col B2|col B3|
```
</td>
</tr>
</table>

### Advanced Formatting

<table>
<tr><th>Jira</th><th>Markdown</th></tr>
<tr>
<td>

```
{noformat}
preformatted piece of text
 so *no* further _formatting_ is done here
{noformat}
```
</td>
<td>

````
```
preformatted piece of text
 so *no* further _formatting_ is done here
```
````
</td>
</tr>
<tr>
<td>

```
{panel:title=My Title}
Some text with a title
{panel}
```
</td>
<td>

```
> **My Title**
> Some text with a title
```
</td>
</tr>
<tr>
<td>

```
{code:xml}
    <test>
        <another tag="attribute"/>
    </test>
{code}
```
</td>
<td>

````
```xml
    <test>
        <another tag="attribute"/>
    </test>
```
````
</td>
</tr>
</table>

---

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Clone the repository
git clone https://github.com/vicgor/jira2markdown.git
cd jira2markdown

# Sync dependencies (creates .venv automatically)
uv sync

# Add a runtime dependency
uv add some-package

# Add a dev dependency
uv add --dev some-dev-package
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Auto-fix lint issues
uv run ruff check --fix .
```

---

## Running Tests

```bash
uv run pytest
```

---

## License

MIT
