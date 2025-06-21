# Instructions

Create an implementation of the [Vigenère cipher][wiki].
The Vigenère cipher is a simple substitution cipher.

## Cipher terminology

A cipher is an algorithm used to encrypt, or encode, a string.
The unencrypted string is called the _plaintext_ and the encrypted string is called the _ciphertext_.
Converting plaintext to ciphertext is called _encoding_ while the reverse is called _decoding_.

In a _substitution cipher_, each plaintext letter is replaced with a ciphertext letter which is computed with the help of a _key_.
(Note, it is possible for replacement letter to be the same as the original letter.)

## Encoding details

In this cipher, the key is a series of lowercase letters, such as `"abcd"`.
Each letter of the plaintext is _shifted_ or _rotated_ by a distance based on a corresponding letter in the key.
An `"a"` in the key means a shift of 0 (that is, no shift).
A `"b"` in the key means a shift of 1.
A `"c"` in the key means a shift of 2, and so on.

The first letter of the plaintext uses the first letter of the key, the second letter of the plaintext uses the second letter of the key and so on.
If you run out of letters in the key before you run out of letters in the plaintext, start over from the start of the key again.

If the key only contains one letter, such as `"dddddd"`, then all letters of the plaintext are shifted by the same amount (three in this example), which would make this the same as a rotational cipher or shift cipher (sometimes called a Caesar cipher).
For example, the plaintext `"iamapandabear"` would become `"ldpdsdqgdehdu"`.

If the key only contains the letter `"a"` (one or more times), the shift distance is zero and the ciphertext is the same as the plaintext.

Usually the key is more complicated than that, though!
If the key is `"abcd"` then letters of the plaintext would be shifted by a distance of 0, 1, 2, and 3.
If the plaintext is `"hello"`, we need 5 shifts so the key would wrap around, giving shift distances of 0, 1, 2, 3, and 0.
Applying those shifts to the letters of `"hello"` we get `"hfnoo"`.

## Random keys

If no key is provided, generate a key which consists of at least 100 random lowercase letters from the Latin alphabet.

[wiki]: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
