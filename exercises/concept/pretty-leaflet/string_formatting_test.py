import unittest
import pytest
from string_formatting import (capitalize_header,
                               format_date,
                               display_icons,
                               print_leaflet)


class PrettyLeafletTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_header(self):
        failure_msg = 'Expected an empty header, but the header was not empty.'
        self.assertEqual(capitalize_header(''), '', msg=failure_msg)

    @pytest.mark.task(taskno=1)
    def test_header_event(self):
        self.assertEqual(capitalize_header('Event'), 'Event', msg='Expected: "Event" for header.')

    @pytest.mark.task(taskno=1)
    def test_header_event_capitalized(self):
        self.assertEqual(capitalize_header('evENt'), 'Event', msg='Expected: "Event" for a capitalized header.')

    @pytest.mark.task(taskno=2)
    def test_leaflet_date_day_month_year(self):
        self.assertEqual(format_date([21, 2, 2021]), 'February 21, 2021', msg='Expected "February 21, 2021" for date.')

    @pytest.mark.task(taskno=3)
    def test_leaflet_method_get_icons_fox_clover_fish(self):
        failure_msg = 'Expected an array of three unicode icons: [Fox, Clover, Fish] for the method display_icons().'
        self.assertEqual(display_icons(['\U0001F98A', '\U0001F340', '\U0001F420']), ['🦊', '🍀', '🐠'], msg=failure_msg)


    @pytest.mark.task(taskno=4)
    def test_print_leaflet_concert(self):
        handbill = ('''********************
*                  *
*    'Concert'     *
*                  *
*  April 30, 2021  *
*                  *
* John         🎸  *
* Benjamin     🎤  *
* Max          🎹  *
*                  *
********************''')

        event_info =  ('Concert', ['\U0001F3B8', '\U0001F3A4', '\U0001F3B9'], ['John', 'Benjamin', 'Max'],[30, 4, 2021])
        failure_msg = 'Expected a leaflet for Concert with a partial date, three artists and three icons.'
        self.assertEqual(print_leaflet(*event_info), handbill, msg=failure_msg)

    @pytest.mark.task(taskno=4)
    def test_print_leaflet_teather_empty_date_and_missing_icon(self):
        handbill = ('''********************
*                  *
*    'Macbeth'     *
*                  *
*                  *
*                  *
* Fleance      🌘  *
* Seyton           *
*                  *
********************''')

        event_info = ('macbeth',['\U0001F318'],['Fleance', 'Seyton'])
        failure_msg = 'Expected a leaflet for Macbeth with two artists and one icon but without date.'
        self.assertEqual(print_leaflet(*event_info), handbill,msg=failure_msg)

    @pytest.mark.task(taskno=4)
    def test_print_leaflet_webinar(self):
        handbill = ('''********************
*                  *
*    'Webinar'     *
*                  *
* January 29, 2020 *
*                  *
* Vince        📚  *
* Chris        💻  *
* Leo          🎯  *
*                  *
********************''')

        event_info = ('webinar',['\U0001F4DA', '\U0001F4BB', '\U0001F3AF'],['Vince', 'Chris', 'Leo'],[29, 1, 2020])
        failure_msg = 'Expected a leaflet for Webinar with a complete date, with three artists and icons.'
        self.assertEqual(print_leaflet(*event_info), handbill, msg=failure_msg)
