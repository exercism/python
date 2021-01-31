import unittest

from dominoes import (
    can_chain,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class DominoesTest(unittest.TestCase):
    def test_empty_input_empty_output(self):
        input_dominoes = []
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_singleton_input_singleton_output(self):
        input_dominoes = [(1, 1)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_singleton_that_can_t_be_chained(self):
        input_dominoes = [(1, 2)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_three_elements(self):
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_can_reverse_dominoes(self):
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_can_t_be_chained(self):
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_simple(self):
        input_dominoes = [(1, 1), (2, 2)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_double_loop(self):
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_disconnected_single_isolated(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
        output_chain = can_chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    def test_need_backtrack(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_separate_loops(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    def test_nine_elements(self):
        input_dominoes = [
            (1, 2),
            (5, 3),
            (3, 1),
            (1, 2),
            (2, 4),
            (1, 6),
            (2, 3),
            (3, 4),
            (5, 6),
        ]
        output_chain = can_chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    # Utility methods

    def normalize_dominoes(self, dominoes):
        return list(sorted(tuple(sorted(domino)) for domino in dominoes))

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
        output_normal = self.normalize_dominoes(output_chain)
        self.assertEqual(input_normal, output_normal, msg)

    def assert_consecutive_dominoes_match(self, output_chain):
        for i in range(len(output_chain) - 1):
            msg = (
                "In chain {}, right end of domino {} ({}) "
                "and left end of domino {} ({}) must match"
            )
            msg = msg.format(
                output_chain, i, output_chain[i], i + 1, output_chain[i + 1]
            )
            self.assertEqual(output_chain[i][1], output_chain[i + 1][0], msg)

    def assert_dominoes_at_ends_match(self, output_chain):
        msg = (
            "In chain {}, left end of first domino ({}) and "
            "right end of last domino ({}) must match"
        )
        msg = msg.format(output_chain, output_chain[0], output_chain[-1])
        self.assertEqual(output_chain[0][0], output_chain[-1][1], msg)

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
        self.assert_same_dominoes(input_dominoes, output_chain)
        if not any(output_chain):
            return
        self.assert_consecutive_dominoes_match(output_chain)
        self.assert_dominoes_at_ends_match(output_chain)

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
        self.assertIsNone(output_chain, msg)


if __name__ == "__main__":
    unittest.main()
