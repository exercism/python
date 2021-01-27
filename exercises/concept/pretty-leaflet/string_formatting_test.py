import unittest
from string_formatting import Leaflet


class test_string_formatting(unittest.TestCase):
    def test_header(self):
        self.assertEqual(Leaflet('', [], []).header, '',
                         msg="Expected an empty header, "
                         "but the header instance attribute wasn't empty.")

    def test_header_event(self):
        self.assertEqual(Leaflet('Event', [], []).header, 'Event',
                         msg="Expected: 'Event' for header.")

    def test_header_event_capitalized(self):
        self.assertEqual(Leaflet('evENt', [], []).header, 'Event',
                         msg="Expected: 'Event' for a capitalized header.")

    def test_leaflet_date(self):
        self.assertEqual(Leaflet('', [], []).date, '',
                         msg="Expected an empty date.")

    def test_leaflet_date_day_month(self):
        leaflet = Leaflet('Event', [], [])
        leaflet.set_date(15, 12)
        self.assertEqual(leaflet.date, 'December 15',
                         msg="Expected 'December 15' for date.")

    def test_leaflet_date_day_month_year(self):
        leaflet = Leaflet('Event', [], [])
        leaflet.set_date(21, 2, 2021)
        self.assertEqual(leaflet.date, 'February 21, 2021',
                         msg="Expected 'February 21, 2021' for date.")

    def test_leaflet_method_get_icons(self):
        self.assertEqual(Leaflet('', [], []).get_icons(), [],
                         msg="Expected an empty array for get_icons().")

    def test_leaflet_method_get_icons_fox_clover_fish(self):
        leaflet = Leaflet('', [], ['\U0001F98A', '\U0001F340', '\U0001F420'])
        self.assertEqual(
            leaflet.get_icons(),
            ['🦊', '🍀', '🐠'],
            msg="Expected an array of three unicode icons: "
            "[Fox, Clover, Fish] for the method get_icons().")

    def test_print_leaflet_concert(self):
        leaflet = Leaflet('Concert',
                          ['John', 'Benjamin', 'Max'],
                          ['\U0001F3B8', '\U0001F3A4', '\U0001F3B9'])
        leaflet.set_date(30, 4)
        handbill = ("""********************
*                  *
*    'Concert'     *
*                  *
*     April 30     *
*                  *
* John         🎸  *
* Benjamin     🎤  *
* Max          🎹  *
*                  *
********************""")
        self.assertEqual(leaflet.print_leaflet(), handbill,
                         msg="Expected a leaflet for Concert "
                         "with a partial date, three artists and three icons.")

    def test_print_leaflet_teather_empty_date_and_missing_icon(self):
        leaflet = Leaflet('Macbeth', ['Fleance', 'Seyton'], ['\U0001F318'])
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
        self.assertEqual(leaflet.print_leaflet(), handbill,
                         msg="Expected a leaflet for Macbeth "
                         "with two artists and one icon but without date.")

    def test_print_leaflet_webinar(self):
        leaflet = Leaflet('Webinar',
                          ['Vince', 'Chris', 'Leo'],
                          ['\U0001F4DA', '\U0001F4BB', '\U0001F3AF'])
        leaflet.set_date(29, 1, 2020)
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
        self.assertEqual(leaflet.print_leaflet(), handbill,
                         msg="Expected a leaflet for Webinar "
                         "with a complete date, with three artists and icons.")
