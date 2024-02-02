import unittest
import pytest
from dicts import (create_inventory,
                   add_items,
                   decrement_items,
                   remove_item,
                   list_inventory)


class InventoryTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_create_inventory(self):

        actual_result = create_inventory(["wood", "iron", "iron", "diamond", "diamond"])
        expected = {"wood": 1, "iron": 2, "diamond": 2}
        error_message = ('Called create_inventory(["wood", "iron", "iron", "diamond", "diamond"]). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_add_one_item(self):
        actual_result = add_items({"wood": 4, "iron": 2}, ["iron", "iron"])
        expected = {"wood": 4, "iron": 4}
        error_message = ('Called add_items({"wood": 4, "iron": 2}, ["iron", "iron"]). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_add_multiple_items(self):
        actual_result = add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"])
        expected =  {"wood": 3, "gold": 3, "diamond": 3}
        error_message = ('Called add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"]). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_add_new_item(self):
        actual_result = add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"])
        expected = {"iron": 2, "diamond": 2, "wood": 2}
        error_message = ('Called add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"]). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_add_from_empty_dict(self):
        actual_result = add_items({}, ["iron", "iron", "diamond"])
        expected = {"iron": 2, "diamond": 1}
        error_message = ('Called add_items({}, ["iron", "iron", "diamond"]). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_decrement_items(self):
        actual_result = decrement_items({"iron": 3, "diamond": 4, "gold": 2},
                                        ["iron", "iron", "diamond", "gold", "gold"])
        expected = {"iron": 1, "diamond": 3, "gold": 0}
        error_message = ('Called decrement_items({"iron": 3, "diamond": 4, "gold": 2},'
                         '["iron", "iron", "diamond", "gold", "gold"]). The function '
                         f'returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_not_below_zero(self):
        actual_result = decrement_items({"wood": 2, "iron": 3, "diamond": 1},
                                      ["wood", "wood", "wood", "iron", "diamond", "diamond"])
        expected = {"wood": 0, "iron": 2, "diamond": 0}
        error_message = ('Called decrement_items({"wood": 2, "iron": 3, "diamond": 1}, '
                         '["wood", "wood", "wood", "iron", "diamond", "diamond"]). The '
                         f'function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_decrement_items_not_in_inventory(self):
        actual_result = decrement_items({"iron": 3, "gold": 2},
                                        ["iron", "wood", "iron", "diamond"])

        expected = {"iron": 1, "gold": 2}
        error_message = ('Called decrement_items({"iron": 3, "gold": 2}, '
                         '["iron", "wood", "iron", "diamond"]). The function '
                         f'returned {actual_result}, but the tests '
                         f'expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_item(self):
        actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond")
        expected =  {"iron": 1, "gold": 1}
        error_message = ('Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_item_not_in_inventory(self):
        actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")
        expected = {"iron": 1, "gold": 1, "diamond": 2}
        error_message = ('Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood"). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_list_inventory(self):
        actual_result = list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0})
        expected = [("coal", 15), ("diamond", 3), ("wood", 67)]
        error_message = ('Called list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected}.')

        self.assertEqual(actual_result, expected, msg=error_message)
