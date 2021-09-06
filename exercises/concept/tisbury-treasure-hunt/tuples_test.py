import unittest
import pytest
from tuples import get_coordinate, convert_coordinate, compare_records, create_record, clean_up


class TuplesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_get_coordinate(self):
        input_data = [("Scrimshaw Whale's Tooth", '2A'),
                      ('Brass Spyglass', '4B'),
                      ('Robot Parrot', '1C'),
                      ('Glass Starfish', '6D'),
                      ('Vintage Pirate Hat', '7E'),
                      ('Pirate Flag', '7F'),
                      ('Crystal Crab', '6A'),
                      ('Model Ship in Large Bottle', '8A'),
                      ('Angry Monkey Figurine', '5B'),
                      ('Carved Wooden Elephant', '8C'),
                      ('Amethyst  Octopus', '1F'),
                      ('Antique Glass Fishnet Float', '3D'),
                      ('Silver Seahorse', '4E')]

        result_data = ['2A', '4B', '1C', '6D', '7E', '7F', '6A', '8A', '5B', '8C', '1F', '3D', '4E']
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(get_coordinate(item), result)

    @pytest.mark.task(taskno=2)
    def test_convert_coordinate(self):
        input_data = ['2A', '4B', '1C', '6D', '7E', '7F', '6A', '8A', '5B', '8C', '1F', '3D', '4E']
        result_data = [('2', 'A'),
                       ('4', 'B'),
                       ('1', 'C'),
                       ('6', 'D'),
                       ('7', 'E'),
                       ('7', 'F'),
                       ('6', 'A'),
                       ('8', 'A'),
                       ('5', 'B'),
                       ('8', 'C'),
                       ('1', 'F'),
                       ('3', 'D'),
                       ('4', 'E')]

        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(convert_coordinate(item), result)

    @pytest.mark.task(taskno=3)
    def test_compare_records(self):
        input_data = [
            (("Scrimshaw Whale's Tooth", '2A'), ('Deserted Docks', ('2', 'A'), 'Blue')),
            (('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')),
            (('Robot Parrot', '1C'), ('Seaside Cottages', ('1', 'C'), 'Blue')),
            (('Glass Starfish', '6D'), ('Tangled Seaweed Patch', ('6', 'D'), 'Orange')),
            (('Vintage Pirate Hat', '7E'), ('Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')),
            (('Amethyst  Octopus', '1F'), ('Seaside Cottages', ('1', 'C'), 'Blue')),
            (('Angry Monkey Figurine', '5B'), ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')),
            (('Antique Glass Fishnet Float', '3D'), ('Deserted Docks', ('2', 'A'), 'Blue')),
            (('Brass Spyglass', '4B'), ('Spiky Rocks', ('3', 'D'), 'Yellow')),
            (('Carved Wooden Elephant', '8C'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
        ]
        result_data = [True, True, True, True, True, False, False, False, False, False]
        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(compare_records(item[0], item[1]), result)

    @pytest.mark.task(taskno=4)
    def test_create_record(self):
        input_data = [
            (('Angry Monkey Figurine', '5B'), ('Stormy Breakwater', ('5', 'B'), 'Purple')),
            (('Carved Wooden Elephant', '8C'), ('Foggy Seacave', ('8', 'C'), 'Purple')),
            (('Amethyst  Octopus', '1F'), ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')),
            (('Antique Glass Fishnet Float', '3D'), ('Spiky Rocks', ('3', 'D'), 'Yellow')),
            (('Silver Seahorse', '4E'), ('Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')),
            (('Amethyst  Octopus', '1F'), ('Seaside Cottages', ('1', 'C'), 'Blue')),
            (('Angry Monkey Figurine', '5B'), ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')),
            (('Antique Glass Fishnet Float', '3D'), ('Deserted Docks', ('2', 'A'), 'Blue')),
            (('Brass Spyglass', '4B'), ('Spiky Rocks', ('3', 'D'), 'Yellow')),
            (('Carved Wooden Elephant', '8C'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
        ]
        result_data = [
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow'),
            'not a match',
            'not a match',
            'not a match',
            'not a match',
            'not a match'
        ]

        number_of_variants = range(1, len(input_data) + 1)

        for variant, item, result in zip(number_of_variants, input_data, result_data):
            with self.subTest(f"variation #{variant}", item=item, result=result):
                self.assertEqual(create_record(item[0], item[1]), result)

    @pytest.mark.task(taskno=5)
    def test_clean_up(self):
        input_data = (
            ("Scrimshaw Whale's Tooth", '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
            ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
            ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
            ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
            ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
            ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
            ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
            ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
        )

        result_data = """(\"Scrimshaw Whale's Tooth\", 'Deserted Docks', ('2', 'A'), 'Blue')\n\
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n\
('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')\n\
('Glass Starfish', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange')\n\
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n\
('Pirate Flag', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange')\n\
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n\
('Model Ship in Large Bottle', 'Harbor Managers Office', ('8', 'A'), 'Purple')\n\
('Angry Monkey Figurine', 'Stormy Breakwater', ('5', 'B'), 'Purple')\n\
('Carved Wooden Elephant', 'Foggy Seacave', ('8', 'C'), 'Purple')\n\
('Amethyst  Octopus', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')\n\
('Antique Glass Fishnet Float', 'Spiky Rocks', ('3', 'D'), 'Yellow')\n\
('Silver Seahorse', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"""

        self.assertEqual(clean_up(input_data), result_data)
