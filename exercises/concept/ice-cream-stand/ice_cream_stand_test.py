import unittest
import pytest
from ice_cream_stand import (ice_cream_combinations, sprinkles, fill_out_ice_cream_menu)


class IceCreamStandTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_ice_cream_combinations(self):
        input_data = [(['vanilla', 'chocolate', 'strawberry'], 2),
         (['vanilla', 'chocolate', 'strawberry'], 1),
         (['vanilla', 'chocolate', 'strawberry'], 3),
         (['vanilla', 'chocolate', 'strawberry', 'mint'], 2),
         (['vanilla', 'chocolate', 'strawberry', 'mint', 'raspberry', 'blueberry'], 4)
         ]
        output_data = [(('vanilla', 'chocolate'), ('vanilla', 'strawberry'), ('chocolate', 'strawberry')),
         (('vanilla',), ('chocolate',), ('strawberry',)),
         (('vanilla', 'chocolate', 'strawberry'),),
         (('vanilla', 'chocolate'), ('vanilla', 'strawberry'), ('vanilla', 'mint'), ('chocolate', 'strawberry'), ('chocolate', 'mint'), ('strawberry', 'mint')),
        (
            ('vanilla', 'chocolate', 'strawberry', 'mint'),
            ('vanilla', 'chocolate', 'strawberry', 'raspberry'),
            ('vanilla', 'chocolate', 'strawberry', 'blueberry'),
            ('vanilla', 'chocolate', 'mint', 'raspberry'),
            ('vanilla', 'chocolate', 'mint', 'blueberry'),
            ('vanilla', 'chocolate', 'raspberry', 'blueberry'),
            ('vanilla', 'strawberry', 'mint', 'raspberry'),
            ('vanilla', 'strawberry', 'mint', 'blueberry'),
            ('vanilla', 'strawberry', 'raspberry', 'blueberry'),
            ('vanilla', 'mint', 'raspberry', 'blueberry'),
            ('chocolate', 'strawberry', 'mint', 'raspberry'),
            ('chocolate', 'strawberry', 'mint', 'blueberry'),
            ('chocolate', 'strawberry', 'raspberry', 'blueberry'),
            ('chocolate', 'mint', 'raspberry', 'blueberry'),
            ('strawberry', 'mint', 'raspberry', 'blueberry')
        )]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got different result'
                self.assertEqual(ice_cream_combinations(input_data[0], input_data[1]), output_data, msg=error_msg)


    @pytest.mark.task(taskno=2)
    def test_sprinkles(self):
        input_data = [(['ice_cream_1', 'ice_cream_2', 'ice_cream_3'], [0, 1, 0]),
        (['ice_cream_1', 'ice_cream_2', 'ice_cream_3'], [1, 0, 1]),
        (['ice_cream_1', 'ice_cream_2', 'ice_cream_3', 'ice_cream_4', 'ice_cream_5'], [1, 1, 0, 0, 1]),
        (['ice_cream_1', 'ice_cream_2', 'ice_cream_3', 'ice_cream_4', 'ice_cream_5'], [0, 0, 0, 0, 0]),
        (['ice_cream_1', 'ice_cream_2', 'ice_cream_3', 'ice_cream_4', 'ice_cream_5', 'ice_cream_6', 'ice_cream_7'], [1, 1, 1, 1, 1, 0, 0]),
         ]
        output_data = [['ice_cream_2'],
            ['ice_cream_1', 'ice_cream_3'],
            ['ice_cream_1', 'ice_cream_2', 'ice_cream_5'],
            [],
            ['ice_cream_1', 'ice_cream_2', 'ice_cream_3', 'ice_cream_4', 'ice_cream_5']
        ]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got different result'
                self.assertEqual(sprinkles(input_data[0], input_data[1]), output_data, msg=error_msg)


    @pytest.mark.task(taskno=3)
    def test_fill_out_ice_cream_menu(self):
        input_data = ((('vanilla', 'chocolate', 'strawberry'), ('cherry', 'raspberry'), ('licorice',)),
                        (('strawberry', 'chocolate', 'vanilla'), ('cherry',), ('licorice', 'caramel')),
                        (('chocolate', 'vanilla', 'strawberry'), ('cherry', 'raspberry', 'blueberry'), ('licorice', 'caramel', 'chocolate')),
                        (('chocolate', 'vanilla', 'strawberry'), (), ()),
                        (('strawberry', 'choclate', 'mint', 'vanilla'),('cherry', 'raspberry', 'blueberry'), ('licorice', 'caramel')))
        output_data = [[('vanilla', 'cherry', 'licorice'), ('chocolate', 'raspberry', 'None'), ('strawberry', 'None', 'None')],
            [('strawberry', 'cherry', 'licorice'), ('chocolate', 'None', 'caramel'), ('vanilla', 'None', 'None')],
            [('chocolate', 'cherry', 'licorice'), ('vanilla', 'raspberry', 'caramel'), ('strawberry', 'blueberry', 'chocolate')], 
            [('chocolate', 'None', 'None'), ('vanilla', 'None', 'None'), ('strawberry', 'None', 'None')],
            [('strawberry', 'cherry', 'licorice'), ('choclate', 'raspberry', 'caramel'), ('mint', 'blueberry', 'None'), ('vanilla', 'None', 'None')]
        ]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, output_data=output_data):
                error_msg=f'Expected: {output_data} but got different result'
                self.assertEqual(fill_out_ice_cream_menu(input_data[0], input_data[1], input_data[2]), output_data, msg=error_msg)
