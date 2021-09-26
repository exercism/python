import unittest
import pytest
from string_formatting import (capitalize_header,
                               format_date,
                               display_icons,
                               print_leaflet)


class PrettyLeafletTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_header(self):
        self.assertEqual(capitalize_header(""), "",
                         msg="Expected an empty header, "
                         "but the header wasn't empty.")

    @pytest.mark.task(taskno=1)
    def test_header_event(self):
        self.assertEqual(capitalize_header('Event'), 'Event',
                         msg="Expected: 'Event' for header.")

    @pytest.mark.task(taskno=1)
    def test_header_event_capitalized(self):
        self.assertEqual(capitalize_header('evENt'), 'Event',
                         msg="Expected: 'Event' for a capitalized header.")

    @pytest.mark.task(taskno=2)
    def test_leaflet_date_day_month_year(self):
        self.assertEqual(format_date([21, 2, 2021]), 'February 21, 2021',
                         msg="Expected 'February 21, 2021' for date.")

    @pytest.mark.task(taskno=3)
    def test_leaflet_method_get_icons_fox_clover_fish(self):
        self.assertEqual(
            display_icons(['\U0001F98A', '\U0001F340', '\U0001F420']),
            ['🦊', '🍀', '🐠'],
            msg="Expected an array of three unicode icons: "
            "[Fox, Clover, Fish] for the method display_icons().")

    @pytest.mark.task(taskno=4)
    def test_print_leaflet_concert(self):
        handbill = ("""********************
*                  *
*    'Concert'     *
*                  *
*  April 30, 2021  *
*                  *
* John         🎸  *
* Benjamin     🎤  *
* Max          🎹  *
*                  *
********************""")
        self.assertEqual(
            print_leaflet("Concert", 
                          ['\U0001F3B8', '\U0001F3A4', '\U0001F3B9'],
                          ['John', 'Benjamin', 'Max'],
                          [30, 4, 2021]
            ),
            handbill,
            msg="Expected a leaflet for Concert "
            "with a partial date, three artists and three icons.")

    @pytest.mark.task(taskno=4)
    def test_print_leaflet_teather_empty_date_and_missing_icon(self):
        handbill = ("""********************
*                  *
*    'Macbeth'     *
*                  *
*                  *
*                  *
* Fleance      🌘  *
* Seyton           *
*                  *
********************""")
        self.assertEqual(print_leaflet("macbeth",
                                       ['\U0001F318'],
                                       ['Fleance', 'Seyton']
        ),
        handbill,
        msg="Expected a leaflet for Macbeth "
        "with two artists and one icon but without date.")

    @pytest.mark.task(taskno=4)
    def test_print_leaflet_webinar(self):
        handbill = ("""********************
*                  *
*    'Webinar'     *
*                  *
* January 29, 2020 *
*                  *
* Vince        📚  *
* Chris        💻  *
* Leo          🎯  *
*                  *
********************""")
        self.assertEqual(print_leaflet("webinar",
                                       ['\U0001F4DA', '\U0001F4BB', '\U0001F3AF'],
                                       ['Vince', 'Chris', 'Leo'],
                                       [29, 1, 2020]
        ),
        handbill,
        msg="Expected a leaflet for Webinar "
        "with a complete date, with three artists and icons.")
