import unittest
import pytest
from locomotive_engineer import get_list_of_wagons #, fix_list_of_wagons, add_missing_stops, extend_route_information, something

class InventoryTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_returning_list(self):
        self.assertEqual(get_list_of_wagons(1,5,2,7,4), [1,5,2,7,4])
    
    @pytest.mark.task(taskno=2)
    def test_works_with_two_wagon(self):
        self.assertEqual(get_list_of_wagons(1,5), [1,5])
    
    @pytest.mark.task(taskno=3)
    def test_works_with_one_wagon(self):
        self.assertEqual(get_list_of_wagons(1), [1])

    @pytest.mark.task(taskno=4)
    def test_works_with_many_wagons(self):
        self.assertEqual(get_list_of_wagons(1,5,6,3,9,8,4,14,24,7), 
                        [1,5,6,3,9,8,4,14,24,7])

    """Should we have this one?
    @pytest.mark.task(taskno=5)
    def test_works_with_no_items(self):
        self.assertEqual(get_list_of_wagons(), [])
    """
    