import unittest

import diffie_hellman


class DiffieHellmanTest(unittest.TestCase):

    def test_private_in_range(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for i in primes:
            self.assertTrue(1 < diffie_hellman.private_key(i) < i)

    # Can fail due to randomness, but most likely will not,
    # due to pseudo-randomness and the large number chosen
    def test_private_key_randomness(self):
        p = 2147483647
        private_keys = []
        for i in range(5):
            private_keys.append(diffie_hellman.private_key(p))
        self.assertEqual(len(list(set(private_keys))), len(private_keys))

    def test_public_key_correct(self):
        p = 23
        g = 5
        private = 6
        expected = 8

        actual = diffie_hellman.public_key(p, g, private)
        self.assertEqual(actual, expected)

    def test_secret_key_correct(self):
        p = 23
        public = 19
        private = 6
        expected = 2

        actual = diffie_hellman.secret(p, public, private)
        self.assertEqual(actual, expected)

    def test_secret_key_correct_large_nums(self):
        p = int("""120227323036150778550155526710966921740030662\
        69457894729842354923526575959371158734103742634711454153\
        30066288563005527069961435922404533456428692335628867529\
        30249953227657883929905072620233073626594386072962776144\
        69143365881426187411323246174903542571280506720291038940\
        7991986070558964461330091797026762932543""".replace(
            "\n", "").replace(" ", ""))
        public = int("""7520544115435791944292554616920871123548\
        58559049691782063133092992058683123990461493675163366079\
        66149689640419216591714331722664409474612463910928128055\
        99415792293044373353565984826436410603792531597409532111\
        27577117569121441377056137760635413505489115127155125391\
        86192176020596861210448363099541947258202188""".replace(
            "\n", "").replace(" ", ""))
        private = int("""248347939362593293991108130435688850515\
        37971354473275017926961991904690152151776307586179022004\
        17377685436170904594686456961202706692908603181062371925\
        882""".replace("\n", "").replace(" ", ""))
        expected = int("""70900735223964890815905879227737819348\
        80851869892044649134650898046120174656773533145582564442\
        98779465564310958207858354973848497783442169812282262526\
        39932672153547963980483673419756271345828771971984887453\
        01448857224581986445413661898091472983952358126388674082\
        1363010486083940557620831348661126601106717071""".replace(
            "\n", "").replace(" ", ""))

        actual = diffie_hellman.secret(p, public, private)
        self.assertEqual(actual, expected)

    def test_exchange(self):
        p = 23
        g = 5

        privateA = diffie_hellman.private_key(p)
        privateB = diffie_hellman.private_key(p)

        publicA = diffie_hellman.public_key(p, g, privateA)
        publicB = diffie_hellman.public_key(p, g, privateB)

        secretA = diffie_hellman.secret(p, publicB, privateA)
        secretB = diffie_hellman.secret(p, publicA, privateB)

        self.assertEqual(secretA, secretB)


if __name__ == '__main__':
    unittest.main()
