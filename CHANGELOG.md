# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

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

### Other

- Merge pull request #23 from vicgor/refactor/parametrize-markup-tests

refactor: replace multi-assert test methods with parametrize ([`a10b58f`](https://github.com/vicgor/jira2markdown/commit/a10b58f6da56f8461f82cce811d45b4d70f6955e))
- Merge pull request #1 from vicgor/chore/migrate-to-hatchling

chore: migrate build backend from poetry-core to hatchling + uv compatibility ([`f502c58`](https://github.com/vicgor/jira2markdown/commit/f502c58b51d6115c205904b0827fe1fcd1732929))

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
- **jira2markdown:** Add CLI command ([`31272f8`](https://github.com/vicgor/jira2markdown/commit/31272f887e21d26383f9e7879a59df5ae5428644))
- **jira2markdown:** Bump Python version (#40) ([`734b7d0`](https://github.com/vicgor/jira2markdown/commit/734b7d075f1b96beb4f5aaf50d404a60112cf94a))
- **jira2markdown:** Bump minimal Python version to 3.9 ([`49600ec`](https://github.com/vicgor/jira2markdown/commit/49600ece8a820e19c7cb8eead1fe9ac5d8f5be1d))

### Other

- Feature/use ruff (#38) ([`8d25b4d`](https://github.com/vicgor/jira2markdown/commit/8d25b4d4e548d7a46afd9d2ea21d4fd7803d67a3))

## [0.4] - 2024-11-23

### Chores

- **poetry:** Bump project version to 0.4 ([`80f39b8`](https://github.com/vicgor/jira2markdown/commit/80f39b8f66ff76fe4c352904700141417fc4699c))
- **ci:** Bump actions version ([`662ad7c`](https://github.com/vicgor/jira2markdown/commit/662ad7c4ec480c5140e244bf689055b7174a0d04))

### Documentation

- **readme:** Use YouTrack format to render image with attributes ([`184f7cf`](https://github.com/vicgor/jira2markdown/commit/184f7cf7b4e0d27916c9e4103ad268a13f5e2211))

### Features

- **images:** Use YouTrack format to render image with attributes ([`70af01f`](https://github.com/vicgor/jira2markdown/commit/70af01ffbd63ff17ab07cd0b31349b1749f1af18))

### Other

- Use youtrack format to render image with properties (#37) ([`644d6cf`](https://github.com/vicgor/jira2markdown/commit/644d6cfbebfb19073336cd14ea5000f8e863bab6))

## [0.3.7] - 2024-09-30

### Chores

- **poetry:** Bump project version to 0.3.7 ([`5971ced`](https://github.com/vicgor/jira2markdown/commit/5971ced658847785d2488333a86038028cdb5be0))

### Documentation

- **readme:** Update table header conversion docs ([`bc9cf8a`](https://github.com/vicgor/jira2markdown/commit/bc9cf8ac0cce70934b22a445faf381af589c3aea))

### Features

- **tables:** Change table header delimiter to triple hyphen ([`4dde3eb`](https://github.com/vicgor/jira2markdown/commit/4dde3eb8c2961a8361c223a1c81b8f9fc29c44b0))

### Other

- Changed table separator from single-hyphen (`-`) to triple-hyphen (`---`) (#30) ([`bd50126`](https://github.com/vicgor/jira2markdown/commit/bd5012615d1bb0f689f140efd20aecd3cb19ad84))

## [0.3.6] - 2023-07-30

### Chores

- **poetry:** Unpin pyparsing after fixing a bug ([`decc031`](https://github.com/vicgor/jira2markdown/commit/decc031dc7a6595c9fc6eddcefcdf7bcb5e3b9a3))

## [0.3.5] - 2023-07-26

### Chores

- **poetry:** Temporary pin pyparsing to version 3.0.9 ([`4aa8ea4`](https://github.com/vicgor/jira2markdown/commit/4aa8ea4378de7689d92f5b33019241df08b8aa2e))

## [0.3.4] - 2023-04-13

### Features

- **license:** Add license (#21) ([`170e92d`](https://github.com/vicgor/jira2markdown/commit/170e92d3578396c43d4b5327cfce786f6e91fe74))
- **license:** Add license ([`fc5d49f`](https://github.com/vicgor/jira2markdown/commit/fc5d49fcf9407459f89ec7a516101c3821389a5a))

## [0.3.3] - 2023-04-06

### Chores

- **poetry:** Bump project version to 0.3.3 ([`cfbe436`](https://github.com/vicgor/jira2markdown/commit/cfbe4368da3603ff7b889047e66e3fa6706ad52c))
- **poetry:** Bump dependencies ([`5bad2ac`](https://github.com/vicgor/jira2markdown/commit/5bad2acabd546d2ebc821e417f8254f6cac4144f))
- **poetry:** Bump dependencies ([`943b217`](https://github.com/vicgor/jira2markdown/commit/943b217251a7c3176684c82a06ccccf1098d470d))

### Features

- **text-effects:** Add indentation after quote if missing (#19) ([`9aef6eb`](https://github.com/vicgor/jira2markdown/commit/9aef6eb2e7ee6b3417ee3148357f887c9b6b73be))
- **text-effects:** Add indentation after quote if missing ([`7b9e1a5`](https://github.com/vicgor/jira2markdown/commit/7b9e1a5f37b9c793e014697c74008500ac11e34a))
- **text-effects:** Add indentation after quote if missing ([`dba5b1a`](https://github.com/vicgor/jira2markdown/commit/dba5b1a28d19164446823c3dcbc51336a7bd8436))
- **images:** Image with attributes (#18) ([`35b60ca`](https://github.com/vicgor/jira2markdown/commit/35b60cafb157b3f9fd9ac8310944ee9fb8d27a64))
- **images:** Add image attributes support ([`513c4e7`](https://github.com/vicgor/jira2markdown/commit/513c4e76a086f5d0d812f19cca85bff91ac41432))

## [0.3.2] - 2023-02-03

### Chores

- **poetry:** Bump project version to 0.3.2 ([`aba9901`](https://github.com/vicgor/jira2markdown/commit/aba990176d3fb6f09cbb5781327f834127045a25))
- **poetry:** Bump dependencies ([`3653004`](https://github.com/vicgor/jira2markdown/commit/3653004c92733d4e63ab500d8dda4a151542d736))

### Features

- **text-effects:** Use <u> tag in markdown to convert underline toke (#15) ([`64dcf0b`](https://github.com/vicgor/jira2markdown/commit/64dcf0bbbc7519ddecd985017748f73ef7678c33))
- **links:** Add support for email tags ([`903d0a6`](https://github.com/vicgor/jira2markdown/commit/903d0a609cb7c84f848bace392f364ed598ac101))
- **text-effects:** Use <u> tag in markdown to convert underline token ([`bfe78f4`](https://github.com/vicgor/jira2markdown/commit/bfe78f49aa11f6926a33b65a95b23b05802f1fa8))

## [0.3.1] - 2022-12-10

### Chores

- **poetry:** Bump project version to 0.3.1 ([`0b90199`](https://github.com/vicgor/jira2markdown/commit/0b90199c9d02e3936f1daa185f8a0b74771f345f))

### Features

- **lists:** Add optional space indentation for list items (#13) ([`2b46327`](https://github.com/vicgor/jira2markdown/commit/2b463279c2c2bda6ef7422094d77fe935f9e1e5e))
- **lists:** Add optional space indentation for list items ([`8511370`](https://github.com/vicgor/jira2markdown/commit/85113701255fa1dd2f5b47285cb136e8b09c7e4c))

## [0.3] - 2022-12-06

### Chores

- **ci:** Run CI for new commits and pull requests ([`e917170`](https://github.com/vicgor/jira2markdown/commit/e9171702508ebeadcad8d86d5259ceb458be14d5))
- Add black and isort ([`815b11e`](https://github.com/vicgor/jira2markdown/commit/815b11e76760dc7ea33acf92632027c64ad97ba0))

### Other

- Migrate to pyparsing 3 (#12)

* chore(poetry): bump pyparsing to version 3 and Python to 3.7
* feat: rename methods and arguments names according to new pyparsing naming convention
* feat: switch from ParserElement to Token for ListIndent
* feat: update parsing rules
* chore(poetry): bump project version to 0.3 ([`8146051`](https://github.com/vicgor/jira2markdown/commit/8146051b13f119fb6187ca745886da02783fc8f8))
- Merge branch 'feature/add-code-formatters' ([`58e3c1b`](https://github.com/vicgor/jira2markdown/commit/58e3c1b4fdd228412da0fb3f53c727dc3727bddc))

## [0.2.1] - 2022-01-12

### Features

- **code:** Add parsing for the code language with extra parameters in the tag definition ([`c3ece44`](https://github.com/vicgor/jira2markdown/commit/c3ece44c960ecbf7756cee60afa2335ad98bddf6))
- Parse optional parameters of noformat tag #5 ([`3edd92f`](https://github.com/vicgor/jira2markdown/commit/3edd92fcb748210c0e08907e45498ab9f9fd9646))

### Other

- Bump version to 0.2.1 ([`89f7f54`](https://github.com/vicgor/jira2markdown/commit/89f7f54b681d96557bda1f46aae0bd2caac3e471))
- Merge pull request #6 from catcombo/feature/parse-noformat-params

feat: parse noformat and code optional parameters ([`e780075`](https://github.com/vicgor/jira2markdown/commit/e78007594dc1575acaefbf61b38263db1ae2eeae))
- Bump dependencies ([`f90b9e4`](https://github.com/vicgor/jira2markdown/commit/f90b9e4290cf5f0b4601c9bb7472069260bc7e65))

## [0.2.0] - 2021-03-11

### Other

- Merge branch 'develop' ([`d906dfb`](https://github.com/vicgor/jira2markdown/commit/d906dfb9b385d25e508ff9dbddf4b365c20a4994))
- Bump version to 0.2.0 ([`bd9add9`](https://github.com/vicgor/jira2markdown/commit/bd9add992a78d83fc05762b95c09a7bc6d0d91c8))
- Rename IS_INLINE_ELEMENT to is_inline_element ([`d911057`](https://github.com/vicgor/jira2markdown/commit/d9110577ce165836081150991c79d9a4d662b710))
- Exclude pytest tests and special directories from flake8 ([`4e4aa5b`](https://github.com/vicgor/jira2markdown/commit/4e4aa5bc972acdc88c82ba05e561d3652d22470d))
- Add inline and block elements pasring rules ([`df99a09`](https://github.com/vicgor/jira2markdown/commit/df99a09db76bdb41c5cc9a20c5358866606e0fbc))
- Add escaping for broken links and multiple prefixes parsing ([`4676eb4`](https://github.com/vicgor/jira2markdown/commit/4676eb42ec1112bc4cbb44ecde598d4d54241e2b))
- Add alias for MailTo links ([`4913a2d`](https://github.com/vicgor/jira2markdown/commit/4913a2d4db3262a12d436314643db81a04da264f))
- Remove leading whitespaces for every line in Panel and Blockquote before parsing the content ([`edee2f6`](https://github.com/vicgor/jira2markdown/commit/edee2f6fdd17f252b690537d92d4ea07d26deae6))
- Fix adjacent bold tokens parsing ([`7ea5840`](https://github.com/vicgor/jira2markdown/commit/7ea58406d062088931cc44486c71be76627798e4))
- Add parser elements customization ([`a835133`](https://github.com/vicgor/jira2markdown/commit/a835133c72846f7d028bcd5cd1883f15b1d16e87))

## [0.1.8] - 2021-02-28

### Other

- Merge branch 'develop' ([`41a6604`](https://github.com/vicgor/jira2markdown/commit/41a660427a76d540ff36c9bd5cda6ded51ed7310))
- Bump version to 0.1.8 ([`c0f2e0c`](https://github.com/vicgor/jira2markdown/commit/c0f2e0cf19d8255a7aac3c80aba478f761826b42))
- #3 Add panel conversion ([`57e926a`](https://github.com/vicgor/jira2markdown/commit/57e926a658c2138a9350ca495651d6e6482134e7))
- Allow punctuation marks come after the user mention without spaces ([`49e499e`](https://github.com/vicgor/jira2markdown/commit/49e499eb76a26ad7771ccc00952af59d11ed63c3))
- Add a space after user mention if it adjacent to the text ([`d34e2b2`](https://github.com/vicgor/jira2markdown/commit/d34e2b2bc31b2f6254b4e7ddfdfe52de00f15654))
- Add a line break before and after a table if only it adjacent to a text ([`92d66cc`](https://github.com/vicgor/jira2markdown/commit/92d66cc4796b4e296ccaf08dba770a7f094c371a))
- Add a space before user mention if it adjacent to the previous text ([`56a8fe6`](https://github.com/vicgor/jira2markdown/commit/56a8fe6a5faf99e54981e12b120086c33c961a96))
- Remove StepBack expression by fixing StepTo expression for tables ([`bcc0e01`](https://github.com/vicgor/jira2markdown/commit/bcc0e01fc5ec424e4a3ac43ee693734334685181))
- Replace NotUnicodeAlphaNum with PrecededBy element ([`06d7498`](https://github.com/vicgor/jira2markdown/commit/06d7498b71af0830c9145c9d644394aa8bc3d1f4))
- #2 Add subscript conversion ([`7295889`](https://github.com/vicgor/jira2markdown/commit/72958892a7c9b3de0ff91b785b327c53c68972c8))
- #2 Add superscript conversion ([`925141f`](https://github.com/vicgor/jira2markdown/commit/925141f2f184d5eb132e9c7f4428a54c69421dfe))
- Update dependencies ([`6b86dc8`](https://github.com/vicgor/jira2markdown/commit/6b86dc846af2f14cb1bb3dd641a2ed8350f87696))
- Add citation conversion

Close #4 ([`cde0834`](https://github.com/vicgor/jira2markdown/commit/cde083471245c65f189fab91a0f9101c74c25684))
- Merge pull request #1 from zyv/patch-1

Update README.md ([`bcee772`](https://github.com/vicgor/jira2markdown/commit/bcee772b84da4c1d40c36b87b03aa093f83749f8))
- Update README.md ([`c4993a7`](https://github.com/vicgor/jira2markdown/commit/c4993a7f0ce4b553a9a1a58b9cf580c32903bfe1))

## [0.1.7] - 2021-02-22

### Other

- Merge branch 'develop' ([`5d22525`](https://github.com/vicgor/jira2markdown/commit/5d2252532bec38e8d68bf4c54af8169f11cbf0f1))
- Bump version to 0.1.7 ([`53e7bae`](https://github.com/vicgor/jira2markdown/commit/53e7baeeb40d6fa2875077abbbb1e8ffa9d0ad76))
- Remove image attributes conversion ([`8ba5df1`](https://github.com/vicgor/jira2markdown/commit/8ba5df1a9fb528ae36dea0a563f86950c4ddfbd5))
- Add ruler explanatory comment ([`291c411`](https://github.com/vicgor/jira2markdown/commit/291c411554f4f8155ea1bcbead8217e688dc2d9a))

## [0.1.6] - 2021-02-18

### Other

- Merge branch 'develop' ([`6a78269`](https://github.com/vicgor/jira2markdown/commit/6a7826990e16d01399458aa58bf4034e3cc8f7f5))
- Bump version to 0.1.6 ([`e88de67`](https://github.com/vicgor/jira2markdown/commit/e88de67368385667387ef22c0c6246c951c29917))
- Add conversion tables to README.md ([`6ada85a`](https://github.com/vicgor/jira2markdown/commit/6ada85a72f7947dce05fedcbcf2270b6b65f1751))
- Combine tests to classes by token ([`abe05ab`](https://github.com/vicgor/jira2markdown/commit/abe05ab0c257ec6172c311a1985fa03f11e7224e))
- Code style formatting ([`1ac5ad5`](https://github.com/vicgor/jira2markdown/commit/1ac5ad587da1fa52e92f3769881fa3301bebf897))
- Ruler can now started with whitespace chars or linebreak token ([`fb64e42`](https://github.com/vicgor/jira2markdown/commit/fb64e4224320488b4098c4c74a99e4e8c7bd5946))
- Quate can now started with whitespace chars ([`09a4616`](https://github.com/vicgor/jira2markdown/commit/09a4616db9cf9128d60eab5e1fc55178db89aeff))
- Add mailto token to table ignores for cell content ([`a4d9779`](https://github.com/vicgor/jira2markdown/commit/a4d9779571c1c96f9e39e9ac6d7e22bed6f78c18))
- Add unicode support to start match for image and bold tokens ([`41760f3`](https://github.com/vicgor/jira2markdown/commit/41760f3ae026898883594b99e8631ea4c84be3ed))
- Headings can now start with whitespace chars ([`3e400ce`](https://github.com/vicgor/jira2markdown/commit/3e400ced5985cca163b30a716c810d5420422ceb))
- Add default language (Java) for code block ([`210b213`](https://github.com/vicgor/jira2markdown/commit/210b2137ac7a706e07a23554e4d23b274bd39e89))

## [0.1.5] - 2021-02-16

### Other

- Merge branch 'develop'

# Conflicts:
#	pyproject.toml ([`5b562ac`](https://github.com/vicgor/jira2markdown/commit/5b562ac15119575b76e00b688ab3acc728af6c79))
- Bump version to 0.1.5 ([`26d434d`](https://github.com/vicgor/jira2markdown/commit/26d434d06da239cabbc951f4f0d8ec4e3705d095))
- Add underline (inserted) text conversion ([`e823446`](https://github.com/vicgor/jira2markdown/commit/e823446f721a51913e8751c16069598d46db6e98))

## [0.1.4] - 2021-02-15

### Other

- Bump version to 0.1.4 ([`918d3da`](https://github.com/vicgor/jira2markdown/commit/918d3da4dfcd2d5381f8e76081c77286d9a8bd38))
- Merge branch 'develop' ([`1f2c537`](https://github.com/vicgor/jira2markdown/commit/1f2c53775ceee9d73fe32672591a0536e5a7a318))
- Improve link tag parsing ([`7e1a9e1`](https://github.com/vicgor/jira2markdown/commit/7e1a9e16f767d45c9f5bbfcb02132dc7ad1af234))
- Update mailto tag to parse prefix text ([`51f2310`](https://github.com/vicgor/jira2markdown/commit/51f23102362df435972a5d72271ff89e088f293a))

## [0.1.3] - 2021-02-14

### Other

- Merge branch 'develop' ([`4da9349`](https://github.com/vicgor/jira2markdown/commit/4da93490ebfa974a46282c355998f1dd5ac1f28c))
- Bump version to 0.1.3 ([`80ba811`](https://github.com/vicgor/jira2markdown/commit/80ba811a4931820806bbf2da226ee637f32732cc))
- Leave whitespaces around text in color tag ([`2792105`](https://github.com/vicgor/jira2markdown/commit/2792105c992cee341e3d45c153aedc1accd1e4f6))

## [0.1.2] - 2021-02-14

### Other

- Merge branch 'develop' ([`b8f90a7`](https://github.com/vicgor/jira2markdown/commit/b8f90a7ed716e2bfd34efe82731432aef970fedf))
- Bump version to 0.1.2 ([`2287a27`](https://github.com/vicgor/jira2markdown/commit/2287a277f25a1b234e44f3a2d66e167e28b8be9a))
- Return whitespace chars from empty color tag (if any) ([`2c57c7a`](https://github.com/vicgor/jira2markdown/commit/2c57c7a51e9d83908d0f967f4690e8b9a7e73dab))
- Disable link conversion for simple text in square brackets ([`ea6dd1a`](https://github.com/vicgor/jira2markdown/commit/ea6dd1af97bd2c0b234723260de5bcbb54420709))

## [0.1.1] - 2021-02-06

### Other

- Merge branch 'develop' ([`e076dce`](https://github.com/vicgor/jira2markdown/commit/e076dce179873ea2dcc871f4c80686cde0ae5314))
- Bump version to 0.1.1 ([`b8da671`](https://github.com/vicgor/jira2markdown/commit/b8da671c84b3201312f4ec7e1735afa6cf3295ca))
- Add rgba color parsing for color tag ([`8e1d6a9`](https://github.com/vicgor/jira2markdown/commit/8e1d6a9b7f6966cbb6e3a2e77b2972e1c4492b8c))
- Fix linter errors ([`afd6b1e`](https://github.com/vicgor/jira2markdown/commit/afd6b1eeaa460b9cdf4ebae715f01e8c97302182))

## [0.1.0] - 2021-02-04

### Other

- Initial commit ([`e151a98`](https://github.com/vicgor/jira2markdown/commit/e151a984212cfa547c98db727dd3cb67c547b6b7))

[unreleased]: https://github.com/vicgor/jira2markdown/compare/v0.5..HEAD
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
[0.2.0]: https://github.com/vicgor/jira2markdown/compare/v0.1.8..v0.2.0
[0.1.8]: https://github.com/vicgor/jira2markdown/compare/v0.1.7..v0.1.8
[0.1.7]: https://github.com/vicgor/jira2markdown/compare/v0.1.6..v0.1.7
[0.1.6]: https://github.com/vicgor/jira2markdown/compare/v0.1.5..v0.1.6
[0.1.5]: https://github.com/vicgor/jira2markdown/compare/v0.1.4..v0.1.5
[0.1.4]: https://github.com/vicgor/jira2markdown/compare/v0.1.3..v0.1.4
[0.1.3]: https://github.com/vicgor/jira2markdown/compare/v0.1.2..v0.1.3
[0.1.2]: https://github.com/vicgor/jira2markdown/compare/v0.1.1..v0.1.2
[0.1.1]: https://github.com/vicgor/jira2markdown/compare/v0.1.0..v0.1.1

