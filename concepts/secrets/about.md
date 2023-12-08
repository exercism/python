# About

A previous concept discussed the `random` module, which produces random numbers and random list orderings.

The `secrets` module apparently overlaps with `random` in some of its functionality, but the two modules are designed with very different priorities.
- `random` is optimized for high perfomance in modelling and simulation uses.
- `secrets` is optimized to be crytographically secure, for security-critical applications.

Further details on why `secrets` proved necessary are given in [PEP 506][PEP506]

The [`secrets`][secrets] module is relatively small and simple, with methods for generating random integers, bits, bytes or tokens, or a random entry from a given sequence.

```python
>>> import secrets
>>> secrets.randbelow(1000) # returns n, where 0 <=  n < 1000
577

>>> secrets.randbits(32) # a 32-bit integer
3028709440
>>> bin(secrets.randbits(32))
'0b11111000101100101111110011110100'

>>> secrets.choice(['my', 'secret', 'thing']) # pick from a sequence
'thing'

>>> secrets.token_hex() # string of random hexadecimal digits
'f683d093ea9aa1f2607497c837cf11d7afaefa903c5805f94b64f068e2b9e621'

>>> secrets.token_urlsafe(16) # random alphanumeric characters
'gkSUKRdiPDHqmImPi2HMnw'
```

If you are writing sensitive applications, you will certainly want to read the [full documentation][secrets], which gives further advice and examples.


[secrets]: https://docs.python.org/3/library/secrets.html
[PEP506]: https://peps.python.org/pep-0506/