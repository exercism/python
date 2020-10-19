import unittest
from list_methods import *


class TestListMethods(unittest.TestCase):
    def test_add_me_to_the_queue_set_1(self):
        self.assertListEqual(
            add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"),
            ["Tony", "Bruce", "RichieRich"],
            msg="The person was not added to the queue correctly"
        )

    def test_add_me_to_the_queue_set_2(self):
        self.assertListEqual(
            add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"),
            ["RobotGuy", "WW", "HawkEye"],
            msg="The person was not added to the queue correctly"
        )

    def test_find_his_friend_set_1(self):
        self.assertIs(
            find_his_friend(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], friend_name="Steve"),
            1,
            msg="The Index of the friend to find is incorrect"
        )

    def test_find_his_friend_set_2(self):
        self.assertIs(
            find_his_friend(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], friend_name="Rocket"),
            4,
            msg="The Index of the friend to find is incorrect"
        )

    def test_add_person_with_his_friends_set_1(self):
        self.assertListEqual(
            add_person_with_his_friends(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], index=1, person_name="Bucky"),
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
            msg="The People added location were incorrect"
        )

    def test_add_person_with_his_friends_set_2(self):
        self.assertListEqual(
            add_person_with_his_friends(queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], index=0, person_name="Bucky"),
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            msg="The People added location were incorrect"
        )

    def test_remove_the_mean_person_set_1(self):
        self.assertListEqual(
            remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"),
            ["Natasha", "Steve", "Wanda", "Rocket"],
            msg="The mean person was not removed properly"
        )

    def test_remove_the_mean_person_set_2(self):
        self.assertListEqual(
            remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Eltran", "Rocket"], person_name="Eltran"),
            ["Natasha", "Steve", "Wanda", "Eltran", "Rocket"],
            msg="The mean person was not removed properly"
        )

    def test_how_many_dopplegangers_set_1(self):
        self.assertIs(
            how_many_dopplegangers(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Bucky"),
            0,
            msg="The Doppleganger count is incorrect"
        )

    def test_how_many_dopplegangers_set_2(self):
        self.assertIs(
            how_many_dopplegangers(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"),
            2,
            msg="The Doppleganger count is incorrect"
        )

    def test_remove_the_last_person(self):
        self.assertIs(
            remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]),
            "Rocket",
            msg="The last person is not removed properly"
        )

    def test_sorted_names(self):
        self.assertListEqual(
            sorted_names(queue=["Steve", "Eltran", "Natasha", "Rocket"]),
            ['Eltran', 'Natasha', 'Rocket', 'Steve'],
            msg="The Queue is not properly sorted"
        )
