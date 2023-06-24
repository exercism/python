import unittest
import pytest
from dict_methods import (add_item,
                          read_notes,
                          sort_entries,
                          add_recipe,
                          send_to_store,
                          update_store_inventory)


class MechaMunchManagementTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_add_item(self):
        input_data = [({'Apple': 1, 'Banana': 4 }, ('Raspberry', 4)), 
                        ({'Orange': 1, 'Raspberry': 1, 'Blueberries': 1}, ('Blueberries', 1)), 
                        ({'Broccoli': 1, 'Kiwi': 1, 'Melon': 1, 'Apple': 1, 'Banana': 1}, ('Pineapple', 1))
                    ]
        output_data = [{'Apple': 1, 'Banana': 4, 'Raspberry': 4}, 
                        {'Orange': 1, 'Raspberry': 1, 'Blueberries': 2}, 
                        {'Broccoli': 1, 'Kiwi': 1, 'Melon': 1, 'Apple': 1, 'Banana': 1, 'Pineapple': 1}
                    ]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different shopping cart.'
                self.assertEqual(add_item(input_data[0], input_data[1]), output_data, msg=error_msg)
        

    @pytest.mark.task(taskno=2)
    def test_read_notes(self):
        input_data = [('Apple', "Banana"), 
                    ('Orange', 'Raspberry', 'Blueberries'), 
                    ('Broccoli', 'Kiwi', 'Melon', 'Apple', 'Banana')]
        output_data = [{'Apple': 1, 'Banana': 1}, 
                        {'Orange': 1, 'Raspberry': 1, 'Blueberries': 1},
                        {'Broccoli': 1, 'Kiwi': 1, 'Melon': 1, 'Apple': 1, 'Banana': 1}]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different shopping cart.'
                self.assertEqual(read_notes(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_sort_entries(self):
        input_data = [{'Banana': 4, 'Apple': 2, 'Orange': 1}, 
                        {'Apple': 3, 'Orange': 2, 'Banana': 1}, 
                        {'Orange': 3, 'Banana': 2, 'Apple': 1}, 
                        {'Apple': 2, 'Raspberry': 2, 'Blueberries': 5, 'Broccoli' : 2, 'Kiwi': 1, 'Melon': 4}
                    ]
        output_data = [['Apple', 'Banana', 'Orange'], 
                            ['Apple', 'Banana', 'Orange'], 
                            ['Apple', 'Banana', 'Orange'], 
                            ['Apple', 'Blueberries', 'Broccoli', 'Kiwi', 'Melon', 'Raspberry']
                        ]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got a different sorted list instead.'
                self.assertEqual(sort_entries(input_data), output_data, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def add_recipe(self):
        self.assertEqual()

    @pytest.mark.task(taskno=5)
    def send_to_store(self):
        self.assertEqual()

    @pytest.mark.task(taskno=6)
    def update_store_inventory(self):
        self.assertEqual()
