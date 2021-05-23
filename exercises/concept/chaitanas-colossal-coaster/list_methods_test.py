import unittest

from list_methods import (
    add_me_to_the_queue,
    find_my_friend,
    add_me_with_my_friends,
    remove_the_mean_person,
    how_many_namefellows,
    remove_the_last_person,
    sorted_names,
)


class TestListMethods(unittest.TestCase):
    def test_add_me_to_the_queue_set_normal_queue(self):
        self.assertListEqual(
            add_me_to_the_queue(
                express_queue=["Tony", "Bruce"],
                normal_queue=["RobotGuy", "WW"],
                ticket_type=0,
                person_name="HawkEye",
            ),
            ["RobotGuy", "WW", "HawkEye"],
            msg="The person was not added to the queue correctly",
        )

    def test_add_me_to_the_queue_express_queue(self):
        self.assertListEqual(
            add_me_to_the_queue(
                express_queue=["Tony", "Bruce"],
                normal_queue=["RobotGuy", "WW"],
                ticket_type=1,
                person_name="RichieRich",
            ),
            ["Tony", "Bruce", "RichieRich"],
            msg="The person was not added to the queue correctly",
        )

    def test_find_my_friend_start_of_queue(self):
        self.assertEqual(
            find_my_friend(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                friend_name="Natasha",
            ),
            0,
            msg="The Index of the friend to find is incorrect",
        )

    def test_find_my_friend_middle_of_queue(self):
        self.assertIs(
            find_my_friend(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                friend_name="Steve",
            ),
            1,
            msg="The Index of the friend to find is incorrect",
        )

    def test_find_my_friend_end_of_queue(self):
        self.assertIs(
            find_my_friend(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                friend_name="Rocket",
            ),
            4,
            msg="The Index of the friend to find is incorrect",
        )

    def test_add_me_with_my_friends_start_of_queue(self):
        self.assertListEqual(
            add_me_with_my_friends(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                index=0,
                person_name="Bucky",
            ),
            ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
            msg="The People added location were incorrect",
        )

    def test_add_me_with_my_friends_middle_of_queue(self):
        self.assertListEqual(
            add_me_with_my_friends(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                index=1,
                person_name="Bucky",
            ),
            ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"],
            msg="The People added location were incorrect",
        )

    def test_add_me_with_my_friends_end_of_queue(self):
        self.assertListEqual(
            add_me_with_my_friends(
                queue=["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"],
                index=4,
                person_name="Bucky",
            ),
            ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"],
            msg="The People added location were incorrect",
        )

    def test_remove_the_mean_person_middle_of_queue(self):
        self.assertListEqual(
            remove_the_mean_person(
                queue=["Natasha", "Steve", "Ultron", "Wanda", "Rocket"],
                person_name="Ultron",
            ),
            ["Natasha", "Steve", "Wanda", "Rocket"],
            msg="The mean person was not removed properly",
        )

    def test_remove_the_mean_person_end_of_queue(self):
        self.assertListEqual(
            remove_the_mean_person(
                queue=["Natasha", "Steve", "Wanda", "Rocket", "Ultron"],
                person_name="Ultron",
            ),
            ["Natasha", "Steve", "Wanda", "Rocket"],
            msg="The mean person was not removed properly",
        )

    def test_remove_the_mean_person_start_of_queue(self):
        self.assertListEqual(
            remove_the_mean_person(
                queue=["Ultron", "Natasha", "Steve", "Wanda", "Rocket"],
                person_name="Ultron",
            ),
            ["Natasha", "Steve", "Wanda", "Rocket"],
            msg="The mean person was not removed properly",
        )

    def test_how_many_namefellows_person_not_in_queue(self):
        self.assertIs(
            how_many_namefellows(
                queue=["Natasha", "Steve", "Ultron", "Natasha", "Rocket"],
                person_name="Bucky",
            ),
            0,
            msg="The namefellow count is incorrect",
        )

    def test_how_many_namefellows_only_one(self):
        self.assertIs(
            how_many_namefellows(
                queue=["Natasha", "Steve", "Ultron", "Rocket"], person_name="Natasha"
            ),
            2,
            msg="The namefellow count is incorrect",
        )

    def test_how_many_namefellows_more_than_one(self):
        self.assertIs(
            how_many_namefellows(
                queue=["Natasha", "Steve", "Ultron", "Natasha", "Rocket"],
                person_name="Natasha",
            ),
            2,
            msg="The namefellow count is incorrect",
        )

    def test_remove_the_last_person(self):
        self.assertIs(
            remove_the_last_person(
                queue=["Natasha", "Steve", "Ultron", "Natasha", "Rocket"]
            ),
            "Rocket",
            msg="The last person is not removed properly",
        )

    def test_sorted_names(self):
        self.assertListEqual(
            sorted_names(queue=["Steve", "Ultron", "Natasha", "Rocket"]),
            ["Natasha", "Rocket", "Steve", "Ultron"],
            msg="The Queue is not properly sorted",
        )
