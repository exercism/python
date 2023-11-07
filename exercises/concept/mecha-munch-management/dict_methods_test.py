import unittest
import pytest
from collections import OrderedDict
from dict_methods import (add_item,
                          read_notes,
                          update_recipes,
                          sort_entries,
                          send_to_store,
                          update_store_inventory)


class MechaMunchManagementTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_add_item(self):
        input_data = [
                      ({'Apple': 1, 'Banana': 4 }, ('Apple', 'Banana', 'Orange')),
                      ({'Orange': 1, 'Raspberry': 1, 'Blueberries': 10}, ['Raspberry', 'Blueberries', 'Raspberry']),
                      ({'Broccoli': 1, 'Banana': 1}, ('Broccoli', 'Kiwi', 'Kiwi', 'Kiwi', 'Melon', 'Apple', 'Banana', 'Banana'))
                      ]
        
        output_data = [{'Apple': 2, 'Banana': 5, 'Orange': 1},
                       {'Orange': 1, 'Raspberry': 3, 'Blueberries': 11},
                       {'Broccoli': 2, 'Banana': 3, 'Kiwi': 3, 'Melon': 1, 'Apple': 1}]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = add_item(input_data[0], input_data[1])
                error_msg= (f'Called add_item({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the item was added.')

                self.assertEqual(actual_result, expected, msg=error_msg)
        

    @pytest.mark.task(taskno=2)
    def test_read_notes(self):
        input_data = [('Apple', "Banana"), ('Orange', 'Raspberry', 'Blueberries'),
                      ['Broccoli', 'Kiwi', 'Melon', 'Apple', 'Banana']]

        output_data = [{'Apple': 1, 'Banana': 1}, {'Orange': 1, 'Raspberry': 1, 'Blueberries': 1},
                       {'Broccoli': 1, 'Kiwi': 1, 'Melon': 1, 'Apple': 1, 'Banana': 1}]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = read_notes(input_data)
                error_msg = (f'Called read_notes({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the notes were read.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_update_recipes(self):
        input_data = [
                        ({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                          'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
                        (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)),

                        ({'Apple Pie': {'Apple': 1, 'Pie Crust': 1, 'Cream Custard': 1},
                          'Blueberry Pie': {'Blueberries': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
                        (('Blueberry Pie', {'Blueberries': 2, 'Pie Crust': 1, 'Cream Custard': 1}),
                         ('Apple Pie', {'Apple': 1, 'Pie Crust': 1, 'Cream Custard': 1}))),

                        ({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                          'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
                          'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
                        (('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
                         ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
                         ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})))
                     ]

        output_data = [
                        {'Banana Bread': {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
                         'Raspberry Pie': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
                        {'Apple Pie': {'Apple': 1, 'Pie Crust': 1, 'Cream Custard': 1},
                        'Blueberry Pie': {'Blueberries': 2, 'Pie Crust': 1, 'Cream Custard': 1}},
                        {'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                        'Raspberry Pie': {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2},
                        'Pasta Primavera': {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1},
                        'Blueberry Crumble': {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}}
                     ]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_recipes(input_data[0], input_data[1])
                error_msg = (f'Called update_recipes({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the recipes were updated.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_sort_entries(self):
        input_data = [
                      {'Banana': 4, 'Apple': 2, 'Orange': 1, 'Pear': 12},
                      {'Apple': 3, 'Orange': 5, 'Banana': 1, 'Avocado': 2},
                      {'Orange': 3, 'Banana': 2, 'Apple': 1},
                      {'Apple': 2, 'Raspberry': 2, 'Blueberries': 5, 'Broccoli' : 2, 'Kiwi': 1, 'Melon': 4}
                     ]

        output_data = [
                        {'Apple': 2, 'Banana': 4, 'Orange': 1, 'Pear': 12},
                        {'Apple': 3, 'Avocado': 2, 'Banana': 1, 'Orange': 5},
                        {'Apple': 1, 'Banana': 2, 'Orange': 3},
                        {'Apple' : 2, 'Blueberries': 5, 'Broccoli': 2, 'Kiwi': 1, 'Melon': 4, 'Raspberry': 2}
                      ]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expecred=expected):
                actual_result = sort_entries(input_data)
                error_msg = (f'Called sort_entries({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} for the sorted entries.')

                # Because we are asserting equal, we need to convert to an OrderedDict.
                # Regular dictionaries will compare equal even when they are ordered
                # differently from one another. See https://stackoverflow.com/a/58961124
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_send_to_store(self):
        input_data = [
                        ({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                         {'Banana': ['Isle 5', False], 'Apple': ['Isle 4', False],
                          'Orange': ['Isle 4', False], 'Milk': ['Isle 2', True]}),

                        ({'Kiwi': 3, 'Juice': 5, 'Yoghurt': 2, 'Milk': 5},
                         {'Kiwi': ['Isle 6', False], 'Juice': ['Isle 5', False],
                          'Yoghurt': ['Isle 2', True], 'Milk': ['Isle 2', True]}),

                        ({'Apple': 2, 'Raspberry': 2, 'Blueberries': 5,
                          'Broccoli' : 2, 'Kiwi': 1, 'Melon': 4},

                         {'Apple': ['Isle 1', False], 'Raspberry': ['Isle 6', False],
                          'Blueberries': ['Isle 6', False], 'Broccoli': ['Isle 3', False],
                          'Kiwi': ['Isle 6', False], 'Melon': ['Isle 6', False]})
                      ]

        output_data = [
                        {'Orange': [1, 'Isle 4', False], 'Milk': [2, 'Isle 2', True],
                         'Banana': [3, 'Isle 5', False], 'Apple': [2, 'Isle 4', False]},

                        {'Yoghurt': [2, 'Isle 2', True], 'Milk': [5, 'Isle 2', True],
                         'Kiwi': [3, 'Isle 6', False], 'Juice': [5, 'Isle 5', False]},

                        {'Raspberry': [2, 'Isle 6', False], 'Melon': [4, 'Isle 6', False],
                         'Kiwi': [1, 'Isle 6', False], 'Broccoli': [2, 'Isle 3', False],
                         'Blueberries': [5, 'Isle 6', False], 'Apple': [2, 'Isle 1', False]}
                      ]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = send_to_store(input_data[0], input_data[1])
                error_msg = (f'Called send_to_store({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the fulfillment cart.')

                # Because we are asserting equal, we need to convert to an OrderedDict.
                # Regular dictionaries will compare equal even when they are ordered
                # differently from one another. See https://stackoverflow.com/a/58961124
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=6)
    def test_update_store_inventory(self):
        input_data = [
                        ({'Orange': [1, 'Isle 4', False], 'Milk': [2, 'Isle 2', True],
                          'Banana': [3, 'Isle 5', False], 'Apple': [2, 'Isle 4', False]},
                         {'Banana': [15, 'Isle 5', False], 'Apple': [12, 'Isle 4', False],
                          'Orange': [1, 'Isle 4', False], 'Milk': [4, 'Isle 2', True]}),

                        ({'Kiwi': [3, 'Isle 6', False]},{'Kiwi': [3, 'Isle 6', False], 'Juice': [5, 'Isle 5', False],
                          'Yoghurt': [2, 'Isle 2', True], 'Milk': [5, 'Isle 2', True]}),

                        ({'Kiwi': [1, 'Isle 6', False], 'Melon': [4, 'Isle 6', False], 'Apple': [2, 'Isle 1', False],
                          'Raspberry': [2, 'Isle 6', False], 'Blueberries': [5, 'Isle 6', False],
                          'Broccoli': [1, 'Isle 3', False]},
                         {'Apple': [2, 'Isle 1', False], 'Raspberry': [5, 'Isle 6', False],
                          'Blueberries': [10, 'Isle 6', False], 'Broccoli': [4, 'Isle 3', False],
                          'Kiwi': [1, 'Isle 6', False], 'Melon': [8, 'Isle 6', False]})
                      ]

        output_data = [
                        {'Banana': [12, 'Isle 5', False], 'Apple': [10, 'Isle 4', False],
                         'Orange': ['Out of Stock', 'Isle 4', False], 'Milk': [2, 'Isle 2', True]},

                        {'Juice': [5, 'Isle 5', False], 'Yoghurt': [2, 'Isle 2', True],
                         'Milk': [5, 'Isle 2', True], 'Kiwi': ["Out of Stock", 'Isle 6', False]},

                        {'Kiwi': ['Out of Stock', 'Isle 6', False], 'Melon': [4, 'Isle 6', False],
                         'Apple': ['Out of Stock', 'Isle 1', False], 'Raspberry': [3, 'Isle 6', False],
                         'Blueberries': [5, 'Isle 6', False], 'Broccoli': [3, 'Isle 3', False]}
                      ]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_store_inventory(input_data[0], input_data[1])
                error_msg = (f'Called update_store_inventory({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the store inventory.')

                self.assertEqual(actual_result, expected, msg=error_msg)
