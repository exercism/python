import unittest
import pytest
from locomotive_engineer import (get_list_of_wagons,
                                 fix_list_of_wagons,
                                 add_missing_stops,
                                 extend_route_information,
                                 fix_wagon_depot)


class LocomotiveEngineerTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_list_of_wagons(self):
        input_data = [(1,5,2,7,4), (1,5), (1,), (1,9,3), (1,10,6,3,9,8,4,14,24,7)]
        output_data = [[1,5,2,7,4], [1,5], [1], [1,9,3], [1,10,6,3,9,8,4,14,24,7]]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):

                actual_result = get_list_of_wagons(*input_data)
                error_msg= (f'Called get_list_of_wagons{input_data}. '
                            f'The function returned {actual_result}, but the '
                            f'tests expected: {expected} as the wagon list instead.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_fix_list_of_wagons(self):
        input_data = [([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]),
                     ([3, 27, 1, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19], [8, 10, 5, 9, 36, 7, 20]),
                     ([4, 2, 1], [8, 6, 15]), 
                     ([3, 14, 1, 25, 7, 19, 10], [8, 6, 4, 5, 9, 21, 2, 13])
                     ]
        output_data = [[1, 3, 17, 6, 15, 7, 4,  12, 6, 3, 13, 2, 5],
                        [1, 8, 10, 5, 9, 36, 7, 20, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19, 3, 27], 
                        [1, 8, 6, 15, 4, 2], 
                        [1, 8, 6, 4, 5, 9, 21, 2, 13, 25, 7, 19, 10, 3, 14]
                    ]
        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):

                actual_result = fix_list_of_wagons(input_data[0], input_data[1])
                error_msg= (f'Called fix_list_of_wagons({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the '
                            f'tests expected: {expected} as the wagon list instead.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_add_missing_stops(self): 
        input_data = (({'from': 'Berlin', 'to': 'Hamburg'}, {'stop_1': 'Lepzig', 'stop_2': 'Hannover', 'stop_3': 'Frankfurt'}), 
                        ({'from': 'Paris', 'to': 'London'}, {'stop_1': 'Lille'}),
                      ({'from': 'New York', 'to': 'Philadelphia'},{}),
                        ({'from': 'Gothenburg', 'to': 'Copenhagen'}, {'stop_1': 'Kungsbacka', 'stop_2': 'Varberg', 'stop_3': 'Halmstad', 'stop_4': 'Angelholm', 'stop_5': 'Lund', 'stop_6': 'Malmo'})
                    )
        output_data = [{'from': 'Berlin', 'to': 'Hamburg', 'stops': ['Lepzig', 'Hannover', 'Frankfurt']}, 
                        {'from': 'Paris', 'to': 'London', 'stops': ['Lille']},
                        {'from': 'New York', 'to': 'Philadelphia', 'stops': []},
                        {'from': 'Gothenburg', 'to': 'Copenhagen', 'stops': ['Kungsbacka', 'Varberg', 'Halmstad', 'Angelholm', 'Lund', 'Malmo']}
                    ]
        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):

                actual_result = add_missing_stops(input_data[0], **input_data[1])
                error_msg= (f'Called add_missing_stops({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the '
                            f'tests expected: {expected} as the set of stops.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_extend_route_information(self): 
        input_data = [({'from': 'Berlin', 'to': 'Hamburg'}, {'timeOfArrival': '12:00', 'precipitation': '10', 'temperature': '5', 'caboose': 'yes'}),
                        ({'from': 'Paris', 'to': 'London'}, {'timeOfArrival': '10:30', 'temperature': '20', 'length': '15'}),
                        ({'from': 'Gothenburg', 'to': 'Copenhagen'}, {'precipitation': '1', 'timeOfArrival': '21:20', 'temperature': '-6'})]
        output_data = [{'from': 'Berlin', 'to': 'Hamburg', 'timeOfArrival': '12:00', 'precipitation': '10', 'temperature': '5', 'caboose': 'yes'},
                        {'from': 'Paris', 'to': 'London', 'timeOfArrival': '10:30', 'temperature': '20', 'length': '15'},
                        {'from': 'Gothenburg', 'to': 'Copenhagen', 'precipitation': '1', 'timeOfArrival': '21:20', 'temperature': '-6'}
                    ]

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):

                actual_result = extend_route_information(input_data[0], input_data[1])
                error_msg= (f'Called extend_route_information({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the '
                            f'tests expected: {expected} as the route dictionary.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_fix_wagon_depot(self):
        input_data = (
            [[(2, 'red'), (4, 'red'), (8, 'red')], [(5, 'blue'), (9, 'blue'), (13, 'blue')], [(3, 'orange'), (7, 'orange'), (11, 'orange')]],
            [[(6, 'blue'), (10, 'blue'), (14, 'blue')], [(7, 'red'), (4, 'red'), (2, 'red')], [(3, 'orange'), (11, 'orange'), (15, 'orange')]],
            [[(7, 'pink'), (4, 'pink'), (2, 'pink')], [(10, 'green'), (6, 'green'), (14, 'green')], [(9, 'yellow'), (5, 'yellow'), (13, 'yellow')]],
            [[(3, 'purple'), (11, 'purple'), (15, 'purple')], [(20, 'black'), (16, 'black'), (12, 'black')], [(19, 'white'), (17, 'white'), (18, 'white')]]
        )

        output_data = (
            [[(2, 'red'), (5, 'blue'), (3, 'orange')], [(4, 'red'), (9, 'blue'), (7, 'orange')], [(8, 'red'), (13, 'blue'), (11, 'orange')]],
            [[(6, 'blue'), (7, 'red'), (3, 'orange')], [(10, 'blue'), (4, 'red'), (11, 'orange')], [(14, 'blue'), (2, 'red'), (15, 'orange')]],
            [[(7, 'pink'), (10, 'green'), (9, 'yellow')], [(4, 'pink'), (6, 'green'), (5, 'yellow')], [(2, 'pink'), (14, 'green'), (13, 'yellow')]],
            [[(3, 'purple'), (20, 'black'), (19, 'white')], [(11, 'purple'), (16, 'black'), (17, 'white')], [(15, 'purple'), (12, 'black'), (18, 'white')]]
        )

        for variant, (input_data, expected) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):

                actual_result = fix_wagon_depot(input_data)
                error_msg= (f'Called fix_wagon_depot({input_data}). '
                            f'The function returned {actual_result}, but the '
                            f'tests expected: {expected} as the wagon depot list.')

                self.assertEqual(actual_result, expected, msg=error_msg)
