# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.7.0] - 2026-06-14

### Features

- Add `MarkupElements.remove()` method for removing elements by type ([`551cb08`](https://github.com/vicgor/jira2markdown/commit/551cb0819dc6508a5a706bcf54145a065d9db456))

### Bug Fixes

- Restore `typer.BadParameter` in CLI for proper stderr output and `--help` hint ([`a233de9`](https://github.com/vicgor/jira2markdown/commit/a233de9f13ff64dcf62c68ecaa1e49bc3853865a))
- Strip ANSI escape codes in `test_help` assertion ([`38aeb90`](https://github.com/vicgor/jira2markdown/commit/38aeb905418d01e991cd50f2c8cd8f18f8767c4f))

### CI/CD

- Upgrade GitHub Actions to Node 24 (`actions/checkout@v6`) ([`adb730b`](https://github.com/vicgor/jira2markdown/commit/adb730b23d48144b851a8807a49f6b4c94314238))
- Add `pytest --cov` coverage report to CI ([`adb730b`](https://github.com/vicgor/jira2markdown/commit/adb730b23d48144b851a8807a49f6b4c94314238))
- Add `pytest-cov` to dev dependencies ([`4ad9f42`](https://github.com/vicgor/jira2markdown/commit/4ad9f42bb2fe5cfe5dfcad13d40a14a84120d854))

### Tests

- Add direct unit tests for `convert()` independent of CLI layer ([`551cb08`](https://github.com/vicgor/jira2markdown/commit/551cb0819dc6508a5a706bcf54145a065d9db456))
- Strengthen `test_remove_bold_leaves_asterisks` assertion to exact value `r"\*not bold\*"`

## [0.6] - 2026-06-13

### Bug Fixes

- Add missing blank line and reformat parametrize calls in test_links ([`2c40969`](https://github.com/vicgor/jira2markdown/commit/2c4096967477e76d8ecadd35590800bbd5de9a97))
- Use explicit utf-8 encoding when writing output file ([`438f8e6`](https://github.com/vicgor/jira2markdown/commit/438f8e6672ce46d7b3502bac6c61d0e1167ffbe2))
- Show helpful message when typer is not installed ([`f224d49`](https://github.com/vicgor/jira2markdown/commit/f224d490f24379d57a4f33d1db5f8754c9819c8e))
- Remove hardcoded Java default in Code block ([`72157a5`](https://github.com/vicgor/jira2markdown/commit/72157a522379fb5d07d2239da3003509429b7b26))
- Do not inject space before mention when preceded by punctuation (#21) ([`df20935`](https://github.com/vicgor/jira2markdown/commit/df20935b6c8377ad42d37f6bc571e843f5b0e542))
- Zero-pad hex components in rgba → hex conversion (#20) ([`e2966bd`](https://github.com/vicgor/jira2markdown/commit/e2966bd434c98fe1c192c2cc1b554bcb2f857ba1))
- Handle FileNotFoundError and BrokenPipeError in cli.py (#15) ([`fa88d11`](https://github.com/vicgor/jira2markdown/commit/fa88d113ed7d486f178aa69872ba9bd3ce7ed84c))
- Replace click.UsageError with typer.BadParameter in cli.py (#14) ([`883a67b`](https://github.com/vicgor/jira2markdown/commit/883a67b4803e3b9e78bf2d3fe1cbb03c002f3add))
- Add type annotations to all test methods (#12) ([`925b2d9`](https://github.com/vicgor/jira2markdown/commit/925b2d9cfdb7160ba8b5449c54174a149676883c))
- Suppress no-untyped-call for ParseResults.get in advanced.py (#11) ([`8b19d03`](https://github.com/vicgor/jira2markdown/commit/8b19d03950d79d56f1be5ab931b7b85d2e4a1f50))
- Move Forward/ParserElement imports to TYPE_CHECKING in base.py (#10) ([`52a4d93`](https://github.com/vicgor/jira2markdown/commit/52a4d93f640db5a08875e1ca1bc70c560328acc6))
- Use filtered lines for max_columns_count in Table.action (#9) ([`41660c6`](https://github.com/vicgor/jira2markdown/commit/41660c6e587f60c0580c0c4e599fa8b2f105cf6a))
- Clean up elements.py and add __all__ to __init__.py (#8) ([`d927fc1`](https://github.com/vicgor/jira2markdown/commit/d927fc17eb6a6b15b42296f6cfa1e8a39cb43543))
- Correct type annotations in parser.py and elements.py (#7) ([`7f87622`](https://github.com/vicgor/jira2markdown/commit/7f87622aae926e81218925b000d5d62607819d6f))
- Add type annotations to lists.py and fix constructor signatures (#6) ([`d2f34d4`](https://github.com/vicgor/jira2markdown/commit/d2f34d4a406f8f279171118a958129e209e0e61f))
- Add return type annotation and fix argument reading in cli.py (#5) ([`aee31c3`](https://github.com/vicgor/jira2markdown/commit/aee31c34f99c7ff37bf35ffe60184c040028c939))
- Replace deprecated typing.Dict/List with built-in dict/list in images.py (#4) ([`acf249d`](https://github.com/vicgor/jira2markdown/commit/acf249d292086658ce922bc26f5bed8ba28ec24a))
- Replace deprecated replaceWith with replace_with (#2) ([`597025c`](https://github.com/vicgor/jira2markdown/commit/597025c06e8477c4081bbd74222260564767cbee))

### CI/CD

- Split lint/test jobs, add Python 3.13 and 3.14 matrix (#22) ([`eb66a2c`](https://github.com/vicgor/jira2markdown/commit/eb66a2c973a3f03c5f60c55f726505a29b43c715))
- Replace poetry workflow with uv + hatchling, add mypy step ([`6d6e326`](https://github.com/vicgor/jira2markdown/commit/6d6e326ffeaf278394cb1a4c6a4cc9f1413816d7))

### Chores

- Remove poetry.lock, bump status to Beta, make typer optional ([`380d652`](https://github.com/vicgor/jira2markdown/commit/380d6520ed40e37dcc8bd72965abb2ba54b13870))
- Remove obsolete ANN101/ANN102 from ruff ignore list (#3) ([`e0b3e5d`](https://github.com/vicgor/jira2markdown/commit/e0b3e5d633e7f5613456af0be9104c441504530f))
- Remove .idea from tracking ([`b4dc2c8`](https://github.com/vicgor/jira2markdown/commit/b4dc2c8f5940d5684fd521f6ff2547beec9eaab7))
- Migrate build backend from poetry-core to hatchling, uv-compatible dev deps ([`e77cd68`](https://github.com/vicgor/jira2markdown/commit/e77cd68822cc184320cf98bccbf501218b4b614c))
- **poetry:** Change license format in pyproject.toml ([`0faa09c`](https://github.com/vicgor/jira2markdown/commit/0faa09cde20852121e5d1b222c2c4182dcfd33b1))

### Documentation

- Update README — uv workflow, Python 3.12+, jira-cli integration, fork notice ([`1b92eb6`](https://github.com/vicgor/jira2markdown/commit/1b92eb601ebcee97dc6a00f9fee2ab8dd051adaf))

### Features

- Add -o / --output flag to write result to a file ([`521a49e`](https://github.com/vicgor/jira2markdown/commit/521a49ef1777de0c9392943b95245c328feca28f))
- Replace argparse with Typer in CLI (#13) ([`e036a95`](https://github.com/vicgor/jira2markdown/commit/e036a95a3ee027610e4e77d27665958049d20dfb))

### Refactoring

- Replace multi-assert test methods with pytest.mark.parametrize ([`50149b6`](https://github.com/vicgor/jira2markdown/commit/50149b6506da1f8be7f4d1924862bf871e832fb3))
- Document intentional use of parseImpl in ListIndent (#19) ([`99dbd1a`](https://github.com/vicgor/jira2markdown/commit/99dbd1a6a83c65ce8f4d49aaa96e7abec9c30b54))
- Replace MarkupElements(list) with typed wrapper class ([`e254f2d`](https://github.com/vicgor/jira2markdown/commit/e254f2d936ca7d0dae827a4fe6431c6156b3a977))
- Add type hints and ABC to AbstractMarkup ([`55cc3fa`](https://github.com/vicgor/jira2markdown/commit/55cc3fa3e7fae93ac2a47345a1ea6c5d2e5c3ad2))
- **jira2markdown:** Rename main.py to cli.py ([`22f045b`](https://github.com/vicgor/jira2markdown/commit/22f045be0f3db2722f98f7052247449e8524809b))

## [0.5] - 2025-04-21

### Chores

- **poetry:** Bump project version to 0.5 ([`520a913`](https://github.com/vicgor/jira2markdown/commit/520a91306c3de637dbe2f28ab0ee1e44cd81f7f0))
- **poetry:** Bump target Python version for ruff to 3.9 ([`15d2089`](https://github.com/vicgor/jira2markdown/commit/15d2089b8a0fc34face96724076719d3f7067370))
- **poetry:** Migrate project metadata to project section ([`8eabc0d`](https://github.com/vicgor/jira2markdown/commit/8eabc0d59d7fb09f4d653f14a39a5fd37b6a5765))
- **linter:** Replace black with ruff ([`5038fdc`](https://github.com/vicgor/jira2markdown/commit/5038fdcbb24783ca04bfafeaa965dc7411057c63))

### Features

- **jira2markdown:** Add CLI command (#41) ([`1f05ad1`](https://github.com/vicgor/jira2markdown/commit/1f05ad1467affae6d1643c41b1d41e5b3a5f423f))
- **jira2markdown:** Bump Python version (#40) ([`734b7d0`](https://github.com/vicgor/jira2markdown/commit/734b7d075f1b96beb4f5aaf50d404a60112cf94a))

## [0.4] - 2024-11-23

### Chores

- **poetry:** Bump project version to 0.4 ([`80f39b8`](https://github.com/vicgor/jira2markdown/commit/80f39b8f66ff76fe4c352904700141417fc4699c))
- **ci:** Bump actions version ([`662ad7c`](https://github.com/vicgor/jira2markdown/commit/662ad7c4ec480c5140e244bf689055b7174a0d04))

### Features

- **images:** Use YouTrack format to render image with attributes ([`70af01f`](https://github.com/vicgor/jira2markdown/commit/70af01ffbd63ff17ab07cd0b31349b1749f1af18))

## [0.3.7] - 2024-09-30

### Features

- **tables:** Change table header delimiter to triple hyphen ([`4dde3eb`](https://github.com/vicgor/jira2markdown/commit/4dde3eb8c2961a8361c223a1c81b8f9fc29c44b0))

## [0.3.6] - 2023-07-30

### Chores

- **poetry:** Unpin pyparsing after fixing a bug ([`decc031`](https://github.com/vicgor/jira2markdown/commit/decc031dc7a6595c9fc6eddcefcdf7bcb5e3b9a3))

## [0.3.5] - 2023-07-26

### Chores

- **poetry:** Temporary pin pyparsing to version 3.0.9 ([`4aa8ea4`](https://github.com/vicgor/jira2markdown/commit/4aa8ea4378de7689d92f5b33019241df08b8aa2e))

## [0.3.4] - 2023-04-13

### Features

- **license:** Add license (#21) ([`170e92d`](https://github.com/vicgor/jira2markdown/commit/170e92d3578396c43d4b5327cfce786f6e91fe74))

## [0.3.3] - 2023-04-06

### Features

- **text-effects:** Add indentation after quote if missing (#19) ([`9aef6eb`](https://github.com/vicgor/jira2markdown/commit/9aef6eb2e7ee6b3417ee3148357f887c9b6b73be))
- **images:** Image with attributes (#18) ([`35b60ca`](https://github.com/vicgor/jira2markdown/commit/35b60cafb157b3f9fd9ac8310944ee9fb8d27a64))

## [0.3.2] - 2023-02-03

### Features

- **text-effects:** Use <u> tag in markdown to convert underline token ([`bfe78f4`](https://github.com/vicgor/jira2markdown/commit/bfe78f49aa11f6926a33b65a95b23b05802f1fa8))
- **links:** Add support for email tags ([`903d0a6`](https://github.com/vicgor/jira2markdown/commit/903d0a609cb7c84f848bace392f364ed598ac101))

## [0.3.1] - 2022-12-10

### Features

- **lists:** Add optional space indentation for list items (#13) ([`2b46327`](https://github.com/vicgor/jira2markdown/commit/2b463279c2c2bda6ef7422094d77fe935f9e1e5e))

## [0.3] - 2022-12-06

### Other

- Migrate to pyparsing 3 (#12) ([`8146051`](https://github.com/vicgor/jira2markdown/commit/8146051b13f119fb6187ca745886da02783fc8f8))

## [0.2.1] - 2022-01-12

### Features

- **code:** Add parsing for the code language with extra parameters ([`c3ece44`](https://github.com/vicgor/jira2markdown/commit/c3ece44c960ecbf7756cee60afa2335ad98bddf6))

## [0.2.0] - 2021-03-11

### Features

- Add inline and block elements parsing rules ([`df99a09`](https://github.com/vicgor/jira2markdown/commit/df99a09db76bdb41c5cc9a20c5358866606e0fbc))
- Add parser elements customization ([`a835133`](https://github.com/vicgor/jira2markdown/commit/a835133c72846f7d028bcd5cd1883f15b1d16e87))

## [0.1.0] - 2021-02-04

### Other

- Initial commit ([`e151a98`](https://github.com/vicgor/jira2markdown/commit/e151a984212cfa547c98db727dd3cb67c547b6b7))

[unreleased]: https://github.com/vicgor/jira2markdown/compare/v0.7.0..HEAD
[0.7.0]: https://github.com/vicgor/jira2markdown/compare/v0.6..v0.7.0
[0.6]: https://github.com/vicgor/jira2markdown/compare/v0.5..v0.6
[0.5]: https://github.com/vicgor/jira2markdown/compare/v0.4..v0.5
[0.4]: https://github.com/vicgor/jira2markdown/compare/v0.3.7..v0.4
[0.3.7]: https://github.com/vicgor/jira2markdown/compare/v0.3.6..v0.3.7
[0.3.6]: https://github.com/vicgor/jira2markdown/compare/v0.3.5..v0.3.6
[0.3.5]: https://github.com/vicgor/jira2markdown/compare/v0.3.4..v0.3.5
[0.3.4]: https://github.com/vicgor/jira2markdown/compare/v0.3.3..v0.3.4
[0.3.3]: https://github.com/vicgor/jira2markdown/compare/v0.3.2..v0.3.3
[0.3.2]: https://github.com/vicgor/jira2markdown/compare/v0.3.1..v0.3.2
[0.3.1]: https://github.com/vicgor/jira2markdown/compare/v0.3..v0.3.1
[0.3]: https://github.com/vicgor/jira2markdown/compare/v0.2.1..v0.3
[0.2.1]: https://github.com/vicgor/jira2markdown/compare/v0.2.0..v0.2.1
[0.2.0]: https://github.com/vicgor/jira2markdown/compare/v0.1.0..v0.2.0
[0.1.0]: https://github.com/vicgor/jira2markdown/releases/tag/v0.1.0
