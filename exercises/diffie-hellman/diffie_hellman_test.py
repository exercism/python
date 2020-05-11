import unittest

from diffie_hellman import private_key, public_key, secret

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0


class DiffieHellmanTest(unittest.TestCase):
    def test_private_key_is_in_range_1_p(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for i in primes:
            self.assertTrue(1 < private_key(i) < i)

    def test_private_key_is_random(self):
        p = 2147483647
        private_keys = []
        for i in range(5):
            private_keys.append(private_key(p))
        self.assertEqual(len(set(private_keys)), len(private_keys))

    def test_can_calculate_public_key_using_private_key(self):
        self.assertEqual(8, public_key(*[23, 5, 6]))

    def test_can_calculate_secret_using_other_party_s_public_key(self):
        self.assertEqual(2, secret(*[23, 19, 6]))

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


if __name__ == "__main__":
    unittest.main()
