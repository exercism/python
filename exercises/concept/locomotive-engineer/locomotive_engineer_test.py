import unittest
import pytest
from locomotive_engineer import get_list_of_wagons, fix_list_of_wagons, add_missing_stops, extend_route_information #, something

class InventoryTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_list_of_wagons(self):
        input_data = [(1,5,2,7,4), (1,5), (1,), (1,9,3), (1,10,6,3,9,8,4,14,24,7)]
        output_data = [[1,5,2,7,4], [1,5], [1], [1,9,3], [1,10,6,3,9,8,4,14,24,7]]

        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(get_list_of_wagons(*input_data), output_data)

    @pytest.mark.task(taskno=2)
    def test_fix_list_of_wagons(self): # One extra case needed at first
        input_data = [([3, 27, 1, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19], [8, 10, 5, 9, 36, 7, 20]),
                     ([4, 2, 1], [8, 6, 15]), 
                     ([3, 14, 1, 25, 7, 19, 10], [8, 6, 4, 5, 9, 21, 2, 13])
                     ]
        output_data = [[1, 8, 10, 5, 9, 36, 7, 20, 14, 10, 4, 12, 6, 23, 17, 13, 22, 28, 19, 3, 27], 
                        [1, 8, 6, 15, 4, 2], 
                        [1, 8, 6, 4, 5, 9, 21, 2, 13, 25, 7, 19, 10, 3, 14]
                    ]
        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(fix_list_of_wagons(input_data[0], input_data[1]), output_data)

    @pytest.mark.task(taskno=3)
    def test_add_missing_stops(self): 
        input_data = [{"stop_1": "Hamburg", "stop_2": "Hannover", "stop_3": "Frankfurt"}, 
                        {"stop_1": "Paris"}, 
                        {"stop_1": "London", "stop_2": "Manchester", "stop_3": "Liverpool", "stop_4": "Birmingham", "stop_5": "Bristol", "stop_6": "Cardiff", "stop_7": "Swansea"}
                    ]
        output_data = [{"stop_1": "Hamburg", "stop_2": "Hannover", "stop_3": "Frankfurt"}, 
                        {"stop_1": "Paris"}, 
                        {"stop_1": "London", "stop_2": "Manchester", "stop_3": "Liverpool", "stop_4": "Birmingham", "stop_5": "Bristol", "stop_6": "Cardiff", "stop_7": "Swansea"}
                    ]
        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(add_missing_stops(**input_data), output_data)

    @pytest.mark.task(taskno=4)
    def test_extend_route_information(self): 
        input_data = [({"from": "Berlin", "to": "Hamburg"}, {"timeOfArrival": "12:00", "precipitation": "10", "temperature": "5"}), 
                        ({"from": "Paris", "to": "London"}, {"timeOfArrival": "10:30", "temperature": "20"}), 
                        ({"from": "Gothenburg", "to": "Copenhagen"}, {"precipitation": "1", "timeOfArrival": "21:20", "temperature": "-6"})]
        output_data = [{"from": "Berlin", "to": "Hamburg", "timeOfArrival": "12:00", "precipitation": "10", "temperature": "5"},
                        {"from": "Paris", "to": "London", "timeOfArrival": "10:30", "temperature": "20"},
                        {"from": "Gothenburg", "to": "Copenhagen", "precipitation": "1", "timeOfArrival": "21:20", "temperature": "-6"}
                    ]
        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(extend_route_information(input_data[0], input_data[1]), output_data)