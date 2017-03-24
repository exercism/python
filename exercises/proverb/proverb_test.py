import unittest

from proverb import proverb


class ProverbTest(unittest.TestCase):
    def test_a_single_consequence(self):
        expected = 'For want of a nail the shoe was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe']), expected)

    def test_short_list(self):
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe', 'horse']), expected)

    def test_long_list(self):
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(proverb(['nail', 'shoe', 'horse', 'rider']), expected)

    def test_new_itens(self):
        expected = 'For want of a key the value was lost.\n'\
                   'And all for the want of a key.'
        self.assertEqual(proverb(['key', 'value']), expected)

    def test_whole_proverb(self):
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a nail.'
        self.assertEqual(
            proverb([
                'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                'kingdom'
            ]), expected)

    def test_qualifier(self):
        expected = 'For want of a nail the shoe was lost.\n'\
                   'For want of a shoe the horse was lost.\n'\
                   'For want of a horse the rider was lost.\n'\
                   'For want of a rider the message was lost.\n'\
                   'For want of a message the battle was lost.\n'\
                   'For want of a battle the kingdom was lost.\n'\
                   'And all for the want of a horseshoe nail.'
        self.assertEqual(
            proverb(
                [
                    'nail', 'shoe', 'horse', 'rider', 'message', 'battle',
                    'kingdom'
                ],
                qualifier='horseshoe'), expected)


if __name__ == '__main__':
    unittest.main()
