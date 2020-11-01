import unittest
from enums import *
from enum import Enum


class TestEnums(unittest.TestCase):

    def test_parse_log_level_set1(self):
        self.assertIs(
            parse_log_level("[INF]: File deleted"),
            LogLevel.Info,
            msg="The Log level returned is incorrect"
        )

    def test_parse_log_level_set2(self):
        self.assertIs(
            parse_log_level("[WRN]: File is being overwrited"),
            LogLevel.Warning,
            msg="The Log level returned is incorrect"
        )
    
    def test_parse_log_level_set3(self):
        self.assertIs(
            parse_log_level("[XYZ]: Some Random Log"),
            LogLevel.Unknown,
            msg="The Log level returned is incorrect"
        )
    
    def test_parse_log_level_set4(self):
        self.assertIs(
            parse_log_level("[ERR]: Some Random Log"),
            LogLevel.Error,
            msg="The Log level returned is incorrect"
        )

    def test_convert_to_short_log_set1(self):
        self.assertEqual(
            convert_to_short_log(LogLevel.Error, "Stack overflow"),
            "6:Stack overflow",
            msg="Incorrect Short String returned"
        )

    def test_convert_to_short_log_set2(self):
        self.assertEqual(
            convert_to_short_log(LogLevel.Warning, "This is a warning"),
            "5:This is a warning",
            msg="Incorrect Short String returned"
        )

    def test_return_alias(self):
        self.assertIs(
            return_alias(),
            LogLevel.Warn,
            msg="The alias returned is incorrect"
        )

    def test_return_members_set1(self):
        class Color(Enum):
            RED = 'red'
            GREEN = 'green'
        
        self.assertListEqual(
            return_members(Color),
            [('RED', 'red'), ('GREEN', 'green')],
            msg="The Members list containing enums is incorrect"
        )

    def test_return_members_set2(self):
        class Shapes(Enum):
            CIRCLE = 1
            SQUARE = 2
            OVAL = 3

        self.assertListEqual(
            return_members(Shapes),
            [('CIRCLE', 1), ('SQUARE', 2), ('OVAL', 3)],
            msg="The Members list containing enums is incorrect"
        )
