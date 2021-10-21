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


class ListMethodsTest(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue(self):
        data = [
            ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'), ['RobotGuy', 'WW', 'HawkEye']),
            ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'), ['Tony', 'Bruce', 'RichieRich']),
        ]

        error_message = 'The person was not added to the queue correctly.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertListEqual(add_me_to_the_queue(*params), result, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_find_my_friend(self):
        data = [
            ((['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Natasha'), 0),
            ((['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Steve'), 1),
            ((['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Rocket'), 4),
        ]

        error_message = 'The index of the friend to find is incorrect.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertIs(find_my_friend(*params), result, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends(self):
        data = [
            (
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'),
                ['Bucky', 'Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket']
            ),
            (
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 1, 'Bucky'),
                ['Natasha', 'Bucky', 'Steve', 'Tchalla', 'Wanda', 'Rocket']
            ),
            (
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 5, 'Bucky'),
                ['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket', 'Bucky']
            ),
        ]

        error_message = 'The person was added to the wrong location in the queue or was not added at all.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertListEqual(add_me_with_my_friends(*params), result, error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person(self):
        data = [
            (
                (['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'], 'Ultron'),
                ['Natasha', 'Steve', 'Wanda', 'Rocket']
            ),
            (
                (['Natasha', 'Steve', 'Wanda', 'Rocket', 'Ultron'], 'Ultron'),
                ['Natasha', 'Steve', 'Wanda', 'Rocket']
            ),
            (
                (['Ultron', 'Natasha', 'Steve', 'Wanda', 'Rocket'], 'Ultron'),
                ['Natasha', 'Steve', 'Wanda', 'Rocket']
            ),
        ]

        error_message = 'The mean person was not removed properly.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertListEqual(remove_the_mean_person(*params), result, msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows(self):
        data = [
            ((['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Bucky'), 0),
            ((['Natasha', 'Steve', 'Ultron', 'Rocket'], 'Natasha'), 1),
            ((['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Natasha'), 2),
        ]

        error_message = 'The namefellow count is incorrect.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertIs(how_many_namefellows(*params), result, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_remove_the_last_person(self):
        data = [
            (['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Rocket'),
        ]

        error_message = 'The last person was not removed properly.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertIs(remove_the_last_person(params), result, msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_sorted_names(self):
        data = [
            (
                ['Steve', 'Ultron', 'Natasha', 'Rocket'],
                ['Natasha', 'Rocket', 'Steve', 'Ultron']
            ),
        ]

        error_message = 'The queue was not properly sorted.'
        for variant, (params, result) in enumerate(data, start=1):
            with self.subTest(f'variation #{variant}', input=params, output=result):
                self.assertListEqual(sorted_names(params), result, msg=error_message)
