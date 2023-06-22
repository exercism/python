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
    def add_item(self):
        self.assertEqual()

    @pytest.mark.task(taskno=2)
    def read_notes(self):
        self.assertEqual()

    @pytest.mark.task(taskno=3)
    def sort_entries(self):
        self.assertEqual()

    @pytest.mark.task(taskno=4)
    def add_recipe(self):
        self.assertEqual()

    @pytest.mark.task(taskno=5)
    def send_to_store(self):
        self.assertEqual()

    @pytest.mark.task(taskno=6)
    def update_store_inventory(self):
        self.assertEqual()
