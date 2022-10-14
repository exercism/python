import unittest

from diffie_hellman import (
    private_key,
    public_key,
    secret,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class DiffieHellmanTest(unittest.TestCase):
    def test_private_key_is_greater_than_1_and_less_than_p(self):
        for prime in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            with self.subTest(f"prime={prime}"):
                key = private_key(prime)
                self.assertTrue(1 < key < prime, msg=f"{key} out of range, expected to be >1 and <{prime}")  # fmt: skip

    def test_private_key_is_random(self):
        """
        Can fail due to randomness, but most likely will not,
        due to pseudo-randomness and the large number chosen
        """
        private_keys = [private_key(2147483647) for _ in range(5)]
        self.assertEqual(len(set(private_keys)), len(private_keys))

    def test_can_calculate_public_key_using_private_key(self):
        p = 23
        g = 5
        private_key = 6
        self.assertEqual(8, public_key(p, g, private_key, ))  # fmt: skip

    def test_can_calculate_public_key_when_given_a_different_private_key(self):
        p = 23
        g = 5
        private_key = 15
        self.assertEqual(19, public_key(p, g, private_key, ))  # fmt: skip

    def test_can_calculate_secret_using_other_party_s_public_key(self):
        p = 23
        their_public_key = 19
        my_private_key = 6
        self.assertEqual(2, secret(p, their_public_key, my_private_key, ))  # fmt: skip

    def test_key_exchange(self):
        p = 23
        g = 5
        alice_private_key = private_key(p)
        bob_private_key = private_key(p)
        alice_public_key = public_key(p, g, alice_private_key)
        bob_public_key = public_key(p, g, bob_private_key)
        secret_a = secret(p, bob_public_key, alice_private_key)
        secret_b = secret(p, alice_public_key, bob_private_key)
        self.assertTrue(secret_a == secret_b)
