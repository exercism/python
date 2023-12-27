# About

A previous concept discussed the [concept:python/random]() module, which produces [pseudo-random numbers][pseudo-random-numbers] and pseudo-random list orderings.

The [`secrets`][secrets] module overlaps with `random` in some of its functionality, but the two modules are designed with very different priorities.

- `random` is optimized for high performance in modelling and simulation, with "good enough" pseudo-random number generation.
- `secrets` is designed to be crytographically secure for applications such as password hashing, security token generation, and account authentication.


Further details on why the addition of the `secrets` module proved necessary are given in [PEP 506][PEP506].

The `secrets` is relatively small and straightforward, with methods for generating random integers, bits, bytes or tokens, or a random entry from a given sequence.

To use `scerets`, you mush first `import` it:


```python
>>> import secrets

#Returns n, where 0 <=  n < 1000.
>>> secrets.randbelow(1000) 
577

#32-bit integers.
>>> secrets.randbits(32) 
3028709440

>>> bin(secrets.randbits(32))
'0b11111000101100101111110011110100'

#Pick at random from a sequence.
>>> secrets.choice(['my', 'secret', 'thing']) 
'thing'

#Generate a token made up of random hexadecimal digits.
>>> secrets.token_hex() 
'f683d093ea9aa1f2607497c837cf11d7afaefa903c5805f94b64f068e2b9e621'

#Generate a URL-safe token of random alphanumeric characters.
>>> secrets.token_urlsafe(16) 
'gkSUKRdiPDHqmImPi2HMnw'
```


If you are writing security-sensitive applications, you will certainly want to read the [full documentation][secrets], which gives further advice and examples.


[PEP506]: https://peps.python.org/pep-0506/
[pseudo-random-numbers]: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
[secrets]: https://docs.python.org/3/library/secrets.html
