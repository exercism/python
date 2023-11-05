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

        for variant, (word, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', word=word, expected=expected):

                actual_result = add_prefix_un(word)
                error_message = (f'Called add_prefix_un("{word}"). '
                                f'The function returned "{actual_result}", but the '
                                f'tests expected "{expected}" after adding "un" as a prefix.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_en(self):
        input_data = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
        expected = ('en :: encircle :: enfold :: enclose :: enjoy :: enlighten ::'
                       ' entangle :: enable :: encode :: enculture')

        actual_result = make_word_groups(input_data)
        error_message = (f'Called make_word_groups({input_data}). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the '
                         'word groups.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_pre(self):
        input_data = ['pre', 'serve', 'dispose', 'position', 'requisite', 'digest',
                      'natal', 'addressed', 'adolescent', 'assumption', 'mature', 'compute']
        expected = ('pre :: preserve :: predispose :: preposition :: prerequisite :: '
                    'predigest :: prenatal :: preaddressed :: preadolescent :: preassumption :: '
                    'premature :: precompute')

        actual_result = make_word_groups(input_data)
        error_message = (f'Called make_word_groups({input_data}). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the '
                         'word groups.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_auto(self):
        input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
                      'echolalia', 'encoder', 'biography']
        expected = ('auto :: autodidactic :: autograph :: automate :: autochrome :: '
                    'autocentric :: autocomplete :: autoecholalia :: autoencoder :: '
                    'autobiography')

        actual_result = make_word_groups(input_data)
        error_message = (f'Called make_word_groups({input_data}). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the '
                         'word groups.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_make_words_groups_inter(self):
        input_data = ['inter', 'twine', 'connected', 'dependent', 'galactic', 'action',
                      'stellar', 'cellular', 'continental', 'axial', 'operative', 'disciplinary']
        expected = ('inter :: intertwine :: interconnected :: interdependent :: '
                    'intergalactic :: interaction :: interstellar :: intercellular :: '
                    'intercontinental :: interaxial :: interoperative :: interdisciplinary')

        actual_result = make_word_groups(input_data)
        error_message = (f'Called make_word_groups({input_data}). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the '
                         'word groups.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_remove_suffix_ness(self):
        input_data = ['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess']
        result_data = ['heavy', 'sad', 'soft', 'crabby', 'light', 'arty', 'edgy']

        for variant, (word, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', word=word, expected=expected):
                actual_result = remove_suffix_ness(word)
                error_message = (f'Called remove_suffix_ness("{word}"). '
                                 f'The function returned "{actual_result}", '
                                 f'but the tests expected "{expected}" after the '
                                 'suffix was removed.')

                self.assertEqual(actual_result, expected, msg=error_message)

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

        for variant, (sentence, index, expected) in enumerate(zip(input_data, index_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', sentence=sentence, index=index, expected=expected):
                actual_result = adjective_to_verb(sentence, index)
                error_message = (f'Called adjective_to_verb("{sentence}", {index}). '
                                 f'The function returned "{actual_result}", but the tests '
                                 f'expected "{expected}" as the verb for '
                                 f'the word at index {index}.')

                self.assertEqual(actual_result, expected, msg=error_message)
