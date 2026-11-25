# LeanVM security definitions

**Status: draft v0.**

The basic definitions for the security statement of LeanVM: non-interactive argument,
completeness and straightline knowledge soundness, in a general oracle setting.

## Contents

1. [Preliminaries](src/preliminaries.md)
2. [Non-interactive arguments](src/arguments.md)
3. [Knowledge soundness](src/knowledge-soundness.md)

## Source and licence

The text of the definitions is from Alessandro Chiesa and Eylon Yogev,
*Building Cryptographic Proofs from Hash Functions*, version 1.2 (25 March 2026),
Sections 1.1, 1.3, 2.1, 4.1, 5.1 and 7.1. Text marked "not in the book" is new.

- Book: <https://snargsbook.org/>
- Source: <https://github.com/hash-based-snargs-book/hash-based-snargs-book>
- Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

This text is under the same licence.

## Build

GitHub shows the chapters and the math directly.

For an HTML book, install [mdBook](https://rust-lang.github.io/mdBook/) and run `mdbook serve`.
The build needs Python 3: `mdbook-math.py` passes the math to MathJax unchanged.
