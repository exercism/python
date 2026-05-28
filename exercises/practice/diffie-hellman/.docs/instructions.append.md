# Instructions Append

## Should I use random or secrets here?

As of Python 3.6, there are two different modules for producing "random" numbers:

The module called [`random`][random] is [_pseudo-random_][pseudo-random], meaning it **does not** generate
true randomness, but follows an algorithm that _simulates_ randomness.
Since these "random numbers" are generated through a known algorithm, they are not truly random.
As a result, th `random` module is not correctly suited for cryptography and should not be used,
precisely because it is pseudo-random.


The module called [`secrets`][secrets] generates
[cryptographically strong][crypto-strong] "random" numbers that provide the greater security required for cryptography.
They are still pseudo-random in the strictest sense — but they have guarantees that the numbers they produce are absolutely unpredictable.


Since this is only a practice exercise, using the `random` module is fine, but note that **it would be
very insecure if actually used for cryptography.**

[crypto-strong]: https://cryptobook.nakov.com/secure-random-generators/secure-random-generators-csprng
[pseudo-random]: https://en.wikipedia.org/wiki/Pseudorandomness
[random]: https://docs.python.org/3/library/random.html
[secrets]: https://docs.python.org/3/library/secrets.html
