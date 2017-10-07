import unittest

import diffie_hellman

class DiffieHellmanTest(unittest.TestCase):

    def test_private_in_range(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for i in primes:
            self.assertTrue(1 < diffie_hellman.private_key(i) < i)

    # Can fail due to randomness, but most likely will not, due to pseudo-randomness
    # and the large number chosen
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
        p = 120227323036150778550155526710966921740030662694578947298423549235265759593711587341037426347114541533006628856300552706996143592240453345642869233562886752930249953227657883929905072620233073626594386072962776144691433658814261874113232461749035425712805067202910389407991986070558964461330091797026762932543
        public = 75205441154357919442925546169208711235485855904969178206313309299205868312399046149367516336607966149689640419216591714331722664409474612463910928128055994157922930443733535659848264364106037925315974095321112757711756912144137705613776063541350548911512715512539186192176020596861210448363099541947258202188
        private = 2483479393625932939911081304356888505153797135447327501792696199190469015215177630758617902200417377685436170904594686456961202706692908603181062371925882
        expected = 70900735223964890815905879227737819348808518698920446491346508980461201746567735331455825644429877946556431095820785835497384849778344216981228226252639932672153547963980483673419756271345828771971984887453014488572245819864454136618980914729839523581263886740821363010486083940557620831348661126601106717071

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