import unittest
import pytest
from strings import (add_prefix_un,
                     make_word_groups,
                     remove_suffix_ness,
                     adjective_to_verb)


class LittleSistersVocabTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_add_prefix_un(self):
        input_data = ['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
        result_data = [f'un{item}' for item in input_data]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, word, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f'variation #{variant}', word=word, result=result):
                self.assertEqual(add_prefix_un(word), result,
                                 msg=f'Expected: {result} but got a different word instead.')

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_en(self):
        input_data = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
        result_data = ('en :: encircle :: enfold :: enclose :: enjoy :: enlighten ::'
                       ' entangle :: enable :: encode :: enculture')

        self.assertEqual(make_word_groups(input_data), result_data,
                         msg=f'Expected {result_data} but got something else instead.')

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_pre(self):
        input_data = ['pre', 'serve', 'dispose', 'position', 'requisite', 'digest',
                      'natal', 'addressed', 'adolescent', 'assumption', 'mature', 'compute']
        result_data = ('pre :: preserve :: predispose :: preposition :: prerequisite :: '
                       'predigest :: prenatal :: preaddressed :: preadolescent :: preassumption :: '
                       'premature :: precompute')

        self.assertEqual(make_word_groups(input_data), result_data,
                         msg=f'Expected {result_data} but got something else instead.')

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_auto(self):
        input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
                      'echolalia', 'encoder', 'biography']
        result_data = ('auto :: autodidactic :: autograph :: automate :: autochrome :: '
                       'autocentric :: autocomplete :: autoecholalia :: autoencoder :: '
                       'autobiography')

        self.assertEqual(make_word_groups(input_data), result_data,
                         msg=f'Expected {result_data} but got something else instead.')

    @pytest.mark.task(taskno=2)
    def test_make_words_groups_inter(self):
        input_data = ['inter', 'twine', 'connected', 'dependent', 'galactic', 'action',
                      'stellar', 'cellular', 'continental', 'axial', 'operative', 'disciplinary']
        result_data = ('inter :: intertwine :: interconnected :: interdependent :: '
                       'intergalactic :: interaction :: interstellar :: intercellular :: '
                       'intercontinental :: interaxial :: interoperative :: interdisciplinary')

        self.assertEqual(make_word_groups(input_data), result_data,
                         msg=f'Expected {result_data} but got something else instead.')

    @pytest.mark.task(taskno=3)
    def test_remove_suffix_ness(self):
        input_data = ['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess']
        result_data = ['heavy', 'sad', 'soft', 'crabby', 'light', 'arty', 'edgy']
        number_of_variants = range(1, len(input_data) + 1)

        for variant, word, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f'variation #{variant}', word=word, result=result):
                self.assertEqual(remove_suffix_ness(word), result,
                                 msg=f'Expected: {result} but got a different word instead.')

    @pytest.mark.task(taskno=4)
    def test_adjective_to_verb(self):
        input_data = ['Look at the bright sky.',
                      'His expression went dark.',
                      'The bread got hard after sitting out.',
                      'The butter got soft in the sun.',
                      'Her eyes were light blue.',
                      'The morning fog made everything damp with mist.',
                      'He cut the fence pickets short by mistake.',
                      'Charles made weak crying noises.',
                      'The black oil got on the white dog.']
        index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
        result_data = ['brighten', 'darken', 'harden', 'soften',
                       'lighten', 'dampen', 'shorten', 'weaken', 'blacken']
        number_of_variants = range(1, len(input_data) + 1)

        for variant, sentence, index, result in zip(number_of_variants, input_data, index_data, result_data):
            with self.subTest(f'variation #{variant}', sentence=sentence, index=index, result=result):
                self.assertEqual(adjective_to_verb(sentence, index), result,
                                 msg=f'Expected: {result} but got a different word instead.')
