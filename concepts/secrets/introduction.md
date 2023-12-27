# Introduction

A previous concept discussed the [concept:python/random]() module, which produces [pseudo-random numbers][pseudo-random-numbers] and pseudo-random list orderings.

The [`secrets`][secrets] module overlaps with `random` in some of its functionality, but the two modules are designed with very different priorities.

- `random` is optimized for high performance in modelling and simulation, with "good enough" pseudo-random number generation.
- `secrets` is designed to be crytographically secure for applications such as password hashing, security token generation, and account authentication.


Further details on why the addition of the `secrets` module proved necessary are given in [PEP 506][PEP506].

If you are writing security-sensitive applications, you will certainly want to read the [full documentation][secrets], which gives further advice and examples.

[PEP506]: https://peps.python.org/pep-0506/
[pseudo-random-numbers]: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
[secrets]: https://docs.python.org/3/library/secrets.html
