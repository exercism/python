import unittest
import pytest
from locomotive_engineer import get_list_of_wagons, fix_list_of_wagons, add_missing_stops, extend_route_information, fix_wagon_depot

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
    @pytest.mark.task(taskno=5)
    def test_fix_wagon_depot(self):
        input_data = [[(2,5,3), (4,9,7), (8,13,11)], 
                        [(13, 4, 3, 8, 9), (5, 6, 7, 10, 11), (19, 2, 12, 14, 15)],
                        [(14, 9, 3, 7, 10, 11, 5), (2, 4, 6, 8, 12, 13, 15), (19, 1, 16, 17, 18, 20, 21)]
                    ]
        output_data = [[(3,5,2), (7,9,4), (11,13,8)], 
                        [(9, 4, 3, 8, 13), (11, 6, 7, 10, 5), (15, 2, 12, 14, 19)],
                        [(5, 9, 3, 7, 10, 11, 14), (15, 4, 6, 8, 12, 13, 2), (21, 1, 16, 17, 18, 20, 19)]
                    ]


        for variant, (input_data, output_data) in enumerate(zip(input_data, output_data), start=1):
            with self.subTest(f"variation #{variant}", input_data=input_data, output_data=output_data):
                self.assertEqual(fix_wagon_depot(input_data), output_data)