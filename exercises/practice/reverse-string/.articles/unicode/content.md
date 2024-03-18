# Working with Unicode Strings in Python


In this article, we'll discuss some considerations and challenges when working with the non-ASCII range of Unicode in Python.


But before we dig into Python, we need to talk about Unicode.
As [Wikipedia defines it][wiki-unicode]:

"_Unicode, formally **The Unicode Standard**, is a text encoding standard maintained by the [Unicode Consortium][unicode-consortium] designed to support the use of text written in all of the world's major writing systems._
_[Version 15.1 of the standard][Unicode 15.1] defines 149813 characters and 161 scripts used in various ordinary, literary, academic, and technical contexts._"


This [2003 article][what-every-developer-needs-to-know-about-unicode] by Joel Spolsky (_co-founder of Stack Overflow_) offers a great overview, and is still a "must read" over 20 years on.

Having a common standard did not suddenly "fix" all the world's text issues, and the Unicode standard is still being actively debated and improved today.
Due to the dominance of English and European languages in early computing, many misconceptions and challenges remain when coding applications and working with Unicode text in programming despite [UTF-8][UTF8] being "the encoding of the web".
The articles linked below describe the challenges better than this article can, and are well worth your time:

- [Eevee: Dark Corners of Unicode][dark-corners]
- [Manish Goregaokar: Let's Stop Ascribing Meaning to Code Points][lets-stop-ascribing-meaning-to-code-points]
- [Manish Goregaokar: Breaking our Latin-1 Assumptions][breaking-our-latin-1-assumptions]
- [W3C Internationalization: Typographic Character Units in Complex Scripts][typographic-character-units-in-complex-scripts]
- [W3C Internationalization: Languages Using Right-to-Left Scripts][w3c-qa-scripts]


One of the [primary motivations][why-python3-exists] for creating Python 3 was to fix the complication between bytes, strings, and Unicode in Python 2.x.
The divisions and implicit conversions were a mess, and the encoding/decoding was confusing and error-prone to use.
This 2012 presentation by Ned Batchelder [Pragmatic Unicode -or- How Do I Stop the Pain?][pragmatic-unicode] talks through these complications and offers some baseline advice for dealing with strings and Unicode in both Python 2.x and 3.x.

The default build of CPython 3.x now represents all strings internally as `UTF-8`, and defines different types for `str` vs `byte`.
Strings are 'seen' as sequences of Unicode [codepoints][what-is-a-codepoint], and default iteration, indexing, slicing, and regex are all designed to move over these codepoints (_the default iteration for bytes is over single bytes_).
For additional information about codepoints, Python offers access to versions of the Unicode properties database via the [`unicodedata`][unicodedata] module.
Python 3.11.5 supports [Unicode 14.0][unicode 14.0], and Python 3.12 will support [Unicode 15.1][unicode 15.1].


Python also ships with [100 additional encodings][standard-encodings] beyond UTF-8, and more can be added via the [codecs module][codecs-module].
However, unless there is strong need and expertise, it is advisable to not change Python's default encoding.

While this clarifies working with strings, it does not solve issues where one user-perceived




http://gernot-katzers-spice-pages.com/var/korean_hangul_unicode.html
https://nedbatchelder.com/text/unipain.html
https://en.wikipedia.org/wiki/Ruby_character
https://home.unicode.org/about-unicode/

https://docs.python.org/3.11/howto/unicode.html
https://docs.python.org/3.11/howto/unicode.html
https://github.com/squareweave/uniseg-python
https://pypi.org/project/regex/
https://icu.unicode.org/


## TODO:  Add details!!



[what-every-developer-needs-to-know-about-unicode]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[wiki-unicode]: https://en.wikipedia.org/wiki/Unicode
[unicode-consortium]: https://home.unicode.org/
[unicode 15.1]: http://blog.unicode.org/2023/09/announcing-unicode-standard-version-151.html
[unicode 14.0]: https://www.unicode.org/versions/Unicode14.0.0/
[why-python3-exists]: https://snarky.ca/why-python-3-exists/
[UTF8]: https://en.wikipedia.org/wiki/UTF-8
[dark-corners]: https://eev.ee/blog/2015/09/12/dark-corners-of-unicode/
[lets-stop-ascribing-meaning-to-code-points]: https://manishearth.github.io/blog/2017/01/14/stop-ascribing-meaning-to-unicode-code-points/
[breaking-our-latin-1-assumptions]: https://manishearth.github.io/blog/2017/01/15/breaking-our-latin-1-assumptions/
[typographic-character-units-in-complex-scripts]: https://www.w3.org/International/questions/qa-indic-graphemes.en
[w3c-qa-scripts]: https://www.w3.org/International/questions/qa-scripts
[pragmatic-unicode]: https://nedbatchelder.com/text/unipain.html
[what-is-a-codepoint]: https://stackoverflow.com/a/27331885
[standard-encodings]: https://docs.python.org/3/library/codecs.html#standard-encodings
[codecs-module]: https://docs.python.org/3/library/codecs.html#module-codecs
[unicodedata]: https://docs.python.org/3/library/unicodedata.html