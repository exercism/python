# Should I use random or secrets?

Python, as of version 3.6, includes two different random modules.

The module called `random` is pseudo-random, meaning it does not generate
true randomness, but follows an algorithm that simulates randomness.
Since random numbers are generated through a known algorithm, they are not truly random.

The `random` module is not correctly suited for cryptography and should not be used,
precisely because it is pseudo-random.

For this reason, in version 3.6, Python introduced the `secrets` module, which generates
cryptographically strong random numbers that provide the greater security required for cryptography.

Since this is only an exercise, `random` is fine to use, but note that **it would be
very insecure if actually used for cryptography.**
