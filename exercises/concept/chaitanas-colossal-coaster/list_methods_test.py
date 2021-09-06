import unittest
import pytest

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

    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue_set_normal_queue(self):
        params = (["Tony", "Bruce"], ["RobotGuy", "WW"], 0, "HawkEye")
        result = ["RobotGuy", "WW", "HawkEye"]

        self.assertListEqual(
            add_me_to_the_queue(*params), result,
            msg="The person was not added to the queue correctly"
        )

    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue_express_queue(self):
        params = (["Tony", "Bruce"], ["RobotGuy", "WW"], 1, "RichieRich")
        result = ["Tony", "Bruce", "RichieRich"]

        self.assertListEqual(
            add_me_to_the_queue(*params), result,
            msg="The person was not added to the queue correctly"
        )

    @pytest.mark.task(taskno=2)
    def test_find_my_friend_start_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Natasha")
        result = 0
        self.assertEqual(
            find_my_friend(*params), result,
            msg="The index of the friend to find is incorrect."
        )

    @pytest.mark.task(taskno=2)
    def test_find_my_friend_middle_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Steve")
        result = 1

        self.assertIs(
            find_my_friend(*params), result,
            msg="The index of the friend to find is incorrect"
        )

    @pytest.mark.task(taskno=2)
    def test_find_my_friend_end_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], "Rocket")
        result = 4

        self.assertIs(
            find_my_friend(*params), result,
            msg="The index of the friend to find is incorrect"
        )

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends_start_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 0, "Bucky")
        result = ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]

        self.assertListEqual(
            add_me_with_my_friends(*params), result,
            msg="The person was added to the wrong location in the queue or was not added at all",
        )

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends_middle_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 1, "Bucky")
        result = ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"]

        self.assertListEqual(
            add_me_with_my_friends(*params), result,
            msg="The person was added to the wrong location in the queue or was not added at all"
        )

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends_end_of_queue(self):
        params = (["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"], 5, "Bucky")
        result = ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket", "Bucky"]

        self.assertListEqual(add_me_with_my_friends(*params), result,
              msg="The person was added to the wrong location in the queue or was not added at all"
                             )

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person_middle_of_queue(self):
        params = (["Natasha", "Steve", "Ultron", "Wanda", "Rocket"], "Ultron")
        result = ["Natasha", "Steve", "Wanda", "Rocket"]

        self.assertListEqual(
            remove_the_mean_person(*params), result,
            msg="The mean person was not removed properly"
        )

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person_end_of_queue(self):
        params = (["Natasha", "Steve", "Wanda", "Rocket", "Ultron"], "Ultron")
        result = ["Natasha", "Steve", "Wanda", "Rocket"]

        self.assertListEqual(
            remove_the_mean_person(*params), result,
            msg="The mean person was not removed properly"
        )

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person_start_of_queue(self):
        params = (["Ultron", "Natasha", "Steve", "Wanda", "Rocket"], "Ultron")
        result = ["Natasha", "Steve", "Wanda", "Rocket"]

        self.assertListEqual(
            remove_the_mean_person(*params), result,
            msg="The mean person was not removed properly"
        )

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows_person_not_in_queue(self):
        params = (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Bucky")
        result = 0

        self.assertIs(
            how_many_namefellows(*params), result,
            msg="The namefellow count is incorrect"
        )

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows_only_one(self):
        params = (["Natasha", "Steve", "Ultron", "Rocket"], "Natasha")
        result = 1
        self.assertIs(
            how_many_namefellows(*params), result,
            msg="The namefellow count is incorrect"
        )

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows_more_than_one(self):
        params = (["Natasha", "Steve", "Ultron", "Natasha", "Rocket"], "Natasha")
        result = 2

        self.assertIs(
            how_many_namefellows(*params), result,
            msg="The namefellow count is incorrect"
        )

    @pytest.mark.task(taskno=6)
    def test_remove_the_last_person(self):
        params = ["Natasha", "Steve", "Ultron", "Natasha", "Rocket"]
        result = "Rocket"

        self.assertIs(
            remove_the_last_person(params), result,
            msg="The last person was not removed properly"
        )

    @pytest.mark.task(taskno=7)
    def test_sorted_names(self):
        params = ["Steve", "Ultron", "Natasha", "Rocket"]
        result = ["Natasha", "Rocket", "Steve", "Ultron"]

        self.assertListEqual(sorted_names(params), result,
                             msg="The queue was not properly sorted"
                             )
