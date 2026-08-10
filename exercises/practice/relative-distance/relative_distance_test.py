# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/relative-distance/canonical-data.json
# File last updated on 2026-01-30

import unittest

from relative_distance import (
    RelativeDistance,
)


class RelativeDistanceTest(unittest.TestCase):
    def test_direct_parent_child_relation(self):
        family_tree = {
            "Vera": ["Tomoko"],
            "Tomoko": ["Aditi"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Vera", "Tomoko"), 1
        )

    def test_sibling_relationship(self):
        family_tree = {
            "Dalia": ["Olga", "Yassin"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Olga", "Yassin"), 1
        )

    def test_two_degrees_of_separation_grandchild(self):
        family_tree = {
            "Khadija": ["Mateo"],
            "Mateo": ["Rami"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Khadija", "Rami"), 2
        )

    def test_complex_graph_cousins(self):
        family_tree = {
            "Aiko": ["Bao", "Carlos"],
            "Bao": ["Dalia", "Elias"],
            "Carlos": ["Fatima", "Gustavo"],
            "Dalia": ["Hassan", "Isla"],
            "Elias": ["Javier"],
            "Fatima": ["Khadija", "Liam"],
            "Gustavo": ["Mina"],
            "Hassan": ["Noah", "Olga"],
            "Isla": ["Pedro"],
            "Javier": ["Quynh", "Ravi"],
            "Khadija": ["Sofia"],
            "Liam": ["Tariq", "Uma"],
            "Mina": ["Viktor", "Wang"],
            "Noah": ["Xiomara"],
            "Olga": ["Yuki"],
            "Pedro": ["Zane", "Aditi"],
            "Quynh": ["Boris"],
            "Ravi": ["Celine"],
            "Sofia": ["Diego", "Elif"],
            "Tariq": ["Farah"],
            "Uma": ["Giorgio"],
            "Viktor": ["Hana", "Ian"],
            "Wang": ["Jing"],
            "Xiomara": ["Kaito"],
            "Yuki": ["Leila"],
            "Zane": ["Mateo"],
            "Aditi": ["Nia"],
            "Boris": ["Oscar"],
            "Celine": ["Priya"],
            "Diego": ["Qi"],
            "Elif": ["Rami"],
            "Farah": ["Sven"],
            "Giorgio": ["Tomoko"],
            "Hana": ["Umar"],
            "Ian": ["Vera"],
            "Jing": ["Wyatt"],
            "Kaito": ["Xia"],
            "Leila": ["Yassin"],
            "Mateo": ["Zara"],
            "Nia": ["Antonio"],
            "Oscar": ["Bianca"],
            "Priya": ["Cai"],
            "Qi": ["Dimitri"],
            "Rami": ["Ewa"],
            "Sven": ["Fabio"],
            "Tomoko": ["Gabriela"],
            "Umar": ["Helena"],
            "Vera": ["Igor"],
            "Wyatt": ["Jun"],
            "Xia": ["Kim"],
            "Yassin": ["Lucia"],
            "Zara": ["Mohammed"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Dimitri", "Fabio"), 9
        )

    def test_complex_graph_no_shortcut_far_removed_nephew(self):
        family_tree = {
            "Aiko": ["Bao", "Carlos"],
            "Bao": ["Dalia", "Elias"],
            "Carlos": ["Fatima", "Gustavo"],
            "Dalia": ["Hassan", "Isla"],
            "Elias": ["Javier"],
            "Fatima": ["Khadija", "Liam"],
            "Gustavo": ["Mina"],
            "Hassan": ["Noah", "Olga"],
            "Isla": ["Pedro"],
            "Javier": ["Quynh", "Ravi"],
            "Khadija": ["Sofia"],
            "Liam": ["Tariq", "Uma"],
            "Mina": ["Viktor", "Wang"],
            "Noah": ["Xiomara"],
            "Olga": ["Yuki"],
            "Pedro": ["Zane", "Aditi"],
            "Quynh": ["Boris"],
            "Ravi": ["Celine"],
            "Sofia": ["Diego", "Elif"],
            "Tariq": ["Farah"],
            "Uma": ["Giorgio"],
            "Viktor": ["Hana", "Ian"],
            "Wang": ["Jing"],
            "Xiomara": ["Kaito"],
            "Yuki": ["Leila"],
            "Zane": ["Mateo"],
            "Aditi": ["Nia"],
            "Boris": ["Oscar"],
            "Celine": ["Priya"],
            "Diego": ["Qi"],
            "Elif": ["Rami"],
            "Farah": ["Sven"],
            "Giorgio": ["Tomoko"],
            "Hana": ["Umar"],
            "Ian": ["Vera"],
            "Jing": ["Wyatt"],
            "Kaito": ["Xia"],
            "Leila": ["Yassin"],
            "Mateo": ["Zara"],
            "Nia": ["Antonio"],
            "Oscar": ["Bianca"],
            "Priya": ["Cai"],
            "Qi": ["Dimitri"],
            "Rami": ["Ewa"],
            "Sven": ["Fabio"],
            "Tomoko": ["Gabriela"],
            "Umar": ["Helena"],
            "Vera": ["Igor"],
            "Wyatt": ["Jun"],
            "Xia": ["Kim"],
            "Yassin": ["Lucia"],
            "Zara": ["Mohammed"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Lucia", "Jun"), 14
        )

    def test_complex_graph_some_shortcuts_cross_down_and_cross_up_cousins_several_times_removed_with_unrelated_family_tree(
        self,
    ):
        family_tree = {
            "Aiko": ["Bao", "Carlos"],
            "Bao": ["Dalia"],
            "Carlos": ["Fatima", "Gustavo"],
            "Dalia": ["Hassan", "Isla"],
            "Fatima": ["Khadija", "Liam"],
            "Gustavo": ["Mina"],
            "Hassan": ["Noah", "Olga"],
            "Isla": ["Pedro"],
            "Javier": ["Quynh", "Ravi"],
            "Khadija": ["Sofia"],
            "Liam": ["Tariq", "Uma"],
            "Mina": ["Viktor", "Wang"],
            "Noah": ["Xiomara"],
            "Olga": ["Yuki"],
            "Pedro": ["Zane", "Aditi"],
            "Quynh": ["Boris"],
            "Ravi": ["Celine"],
            "Sofia": ["Diego", "Elif"],
            "Tariq": ["Farah"],
            "Uma": ["Giorgio"],
            "Viktor": ["Hana", "Ian"],
            "Wang": ["Jing"],
            "Xiomara": ["Kaito"],
            "Yuki": ["Leila"],
            "Zane": ["Mateo"],
            "Aditi": ["Nia"],
            "Boris": ["Oscar"],
            "Celine": ["Priya"],
            "Diego": ["Qi"],
            "Elif": ["Rami"],
            "Farah": ["Sven"],
            "Giorgio": ["Tomoko"],
            "Hana": ["Umar"],
            "Ian": ["Vera"],
            "Jing": ["Wyatt"],
            "Kaito": ["Xia"],
            "Leila": ["Yassin"],
            "Mateo": ["Zara"],
            "Nia": ["Antonio"],
            "Oscar": ["Bianca"],
            "Priya": ["Cai"],
            "Qi": ["Dimitri"],
            "Rami": ["Ewa"],
            "Sven": ["Fabio"],
            "Tomoko": ["Gabriela"],
            "Umar": ["Helena"],
            "Vera": ["Igor"],
            "Wyatt": ["Jun"],
            "Xia": ["Kim"],
            "Yassin": ["Lucia"],
            "Zara": ["Mohammed"],
        }
        self.assertEqual(
            RelativeDistance(family_tree).degree_of_separation("Wyatt", "Xia"), 12
        )

    # Additional track-specific tests
    def test_person_a_not_in_tree(self):
        family_tree = {
            "Priya": ["Rami"],
        }
        with self.assertRaises(ValueError) as err:
            RelativeDistance(family_tree).degree_of_separation("Kaito", "Priya")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Person A not in family tree.")

    def test_person_b_not_in_tree(self):
        family_tree = {
            "Priya": ["Rami"],
        }
        with self.assertRaises(ValueError) as err:
            RelativeDistance(family_tree).degree_of_separation("Priya", "Kaito")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Person B not in family tree.")

    def test_no_connection_between_individuals(self):
        family_tree = {
            "Priya": ["Rami"],
            "Kaito": ["Elif"],
        }
        with self.assertRaises(ValueError) as err:
            RelativeDistance(family_tree).degree_of_separation("Priya", "Kaito")
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(
            err.exception.args[0], "No connection between person A and person B."
        )
