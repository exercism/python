import unittest
from copy import deepcopy
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
        test_data = [
        ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'), ['RobotGuy', 'WW', 'HawkEye']),
        ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'), ['Tony', 'Bruce', 'RichieRich']),
        ((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 1, 'Okoye'), ['Agatha', 'Pepper', 'Valkyrie', 'Okoye']),
        ((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 0, 'Gamora'), ['Drax', 'Nebula', 'Gamora']),
        ]

        for variant, (params, expected) in enumerate(test_data, start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            express_queue, normal_queue, ticket_type, person_name = deepcopy(params)

            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = add_me_to_the_queue(*params)

                error_message = (
                    f'\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n'
                    f'The function returned {actual_result},\n'
                    f' but the tests expected {expected} after {person_name} was added.')

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_add_me_to_the_queue_validate_queue(self):
        test_data = [
        ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye'), ['RobotGuy', 'WW', 'HawkEye']),
        ((['Tony', 'Bruce'], ['RobotGuy', 'WW'], 1, 'RichieRich'), ['Tony', 'Bruce', 'RichieRich']),
        ((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 1, 'Okoye'), ['Agatha', 'Pepper', 'Valkyrie', 'Okoye']),
        ((['Agatha', 'Pepper', 'Valkyrie'], ['Drax', 'Nebula'], 0, 'Gamora'), ['Drax', 'Nebula', 'Gamora']),
        ]

        for variant, (params, expected) in enumerate(test_data, start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            express_queue, normal_queue, ticket_type, person_name = deepcopy(params)
            express, normal, ticket, name = params

            with self.subTest(f'variation #{variant}',
                              express=express, normal=normal,
                              ticket=ticket, name=name, expected=expected):

                actual_result = add_me_to_the_queue(express, normal, ticket, name)

                if type == 1:
                    error_message = (
                            f'\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n'
                            f'The queue == {express}, but the tests expected\n'
                            f'queue == {expected} after {person_name} was added.'
                    )

                    self.assertIs(actual_result, express, msg=error_message)

                if type == 0:
                    error_message = (
                            f'\nCalled add_me_to_the_queue{express_queue, normal_queue, ticket_type, person_name}.\n'
                            f'The queue == {normal}, but the tests expected \n'
                            f'queue == {expected} after {person_name} was added.'
                    )

                    self.assertIs(actual_result, normal, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_find_my_friend(self):
        test_data = [
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Natasha'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Steve'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Rocket'),
        ]

        result_data = (0,1,4)

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = find_my_friend(*params)
                error_message = (
                        f'\nCalled find_my_friend{params}.\n'
                        f'The function returned {actual_result}, but\n'
                        f'the tests expected {expected} when looking for\n'
                        f'{params[-1]} in the queue.'
                )

                self.assertIs(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends(self):
        test_data = [
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 1, 'Bucky'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 5, 'Bucky'),
        ]

        result_data = [
                ['Bucky', 'Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'],
                ['Natasha', 'Bucky', 'Steve', 'Tchalla', 'Wanda', 'Rocket'],
                ['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket', 'Bucky'],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            queue, index, person_name = deepcopy(params)

            with self.subTest(f'variation #{variant}', params=params, expected=expected):

                actual_result = add_me_with_my_friends(*params)
                error_message = (
                        f'\nCalled add_me_with_my_friends{queue, index, person_name}.\n'
                        f'The function returned {actual_result}, but\n'
                        f'the tests expected {expected} when adding\n'
                        f'{person_name} to position {index} in the queue.'
                )

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_add_me_with_my_friends_validate_queue(self):
        test_data = [
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 1, 'Bucky'),
                (['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 5, 'Bucky'),
        ]

        result_data = [
                ['Bucky', 'Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'],
                ['Natasha', 'Bucky', 'Steve', 'Tchalla', 'Wanda', 'Rocket'],
                ['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket', 'Bucky'],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, add_index, person_name = deepcopy(params)
            queue, _, _ = params

            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = add_me_with_my_friends(*params)
                error_message = (
                        f'\nCalled add_me_with_my_friends{start_queue, add_index, person_name}.\n'
                        f'The function returned {actual_result},\n'
                        'but the original queue was unmodified. The tests expected the \n'
                        f'*original* queue to be modified by adding "{person_name}".'
                )

                self.assertIs(actual_result, queue, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person(self):
        test_data = [
                (['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'], 'Ultron'),
                (['Natasha', 'Steve', 'Wanda', 'Rocket', 'Ultron'], 'Rocket'),
                (['Ultron', 'Natasha', 'Steve', 'Wanda', 'Rocket'], 'Steve'),
        ]

        result_data = [
                ['Natasha', 'Steve', 'Wanda', 'Rocket'],
                ['Natasha', 'Steve', 'Wanda', 'Ultron'],
                ['Ultron', 'Natasha', 'Wanda', 'Rocket'],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):

            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, person_name = deepcopy(params)

            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = remove_the_mean_person(*params)
                error_message = (
                        f'\nCalled remove_the_mean_person{start_queue, person_name}.\n'
                        f'The function returned {actual_result}, but\n'
                        f'the tests expected {expected} when removing\n'
                        f'{person_name} from the queue.'
                )

                self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_remove_the_mean_person_validate_queue(self):
        test_data = [
                (['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'], 'Ultron'),
                (['Natasha', 'Steve', 'Wanda', 'Rocket', 'Ultron'], 'Rocket'),
                (['Ultron', 'Natasha', 'Steve', 'Wanda', 'Rocket'], 'Steve'),
        ]

        result_data = [
                ['Natasha', 'Steve', 'Wanda', 'Rocket'],
                ['Natasha', 'Steve', 'Wanda', 'Ultron'],
                ['Ultron', 'Natasha', 'Wanda', 'Rocket'],
        ]


        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):

            # Deepcopy() is needed here because the task expects the input lists to be mutated.
            # That mutation wrecks havoc with the verification and error messaging.
            start_queue, person_name = deepcopy(params)
            queue, _ = params

            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = remove_the_mean_person(*params)
                error_message = (
                        f'\nCalled remove_the_mean_person{start_queue, person_name}.\n'
                        f'The function returned {actual_result}, queue == {queue}.\n'
                        f'But the tests expected queue == {expected} when removing\n'
                        f'{person_name}.'
                )

                self.assertIs(actual_result, queue, msg=error_message)


    @pytest.mark.task(taskno=5)
    def test_how_many_namefellows(self):
        test_data = [(['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Bucky'),
                     (['Natasha', 'Steve', 'Ultron', 'Rocket'], 'Natasha'),
                     (['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Natasha')]

        result_data = (0,1,2)

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', params=params, expected=expected):
                actual_result = how_many_namefellows(*params)

                error_message = (f'Called how_many_namefellows{params}. '
                                 f'The function returned {actual_result}, but '
                                 f'The tests expected {expected} when counting '
                                 f'namefellows in the queue for {params[-1]}.')

                self.assertIs(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_remove_the_last_person(self):
        test_data = [
            (['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], ['Natasha', 'Steve', 'Ultron', 'Natasha'], 'Rocket'),
            (['Wanda', 'Natasha', 'Steve', 'Rocket', 'Ultron'], ['Wanda', 'Natasha', 'Steve', 'Rocket'], 'Ultron'),
            (['Steve', 'Wanda', 'Rocket', 'Ultron', 'Natasha'], ['Steve', 'Wanda', 'Rocket', 'Ultron'], 'Natasha')
        ]
        for variant, (queue, modified, expected) in enumerate(test_data, start=1):
            with self.subTest(f'variation #{variant}', queue=queue, modified=modified, expected=expected):

                # Deepcopy() is needed here because the task expects the input lists to be mutated.
                # That mutation wrecks havoc with the verification and error messaging.
                unmodified_queue = deepcopy(queue)
                expected_result = expected
                actual_result = remove_the_last_person(queue)
                expected_queue = modified

                error_message = (f'\nCalled remove_the_last_person({unmodified_queue}).\n'
                                 f'The function was expected to remove and return the name "{expected_result}" '
                                 f'and change the queue to {expected_queue},\n'
                                 f'but the name "{actual_result}" was returned and the queue == {queue}.')

                self.assertEqual((actual_result, queue), (expected_result, expected_queue), msg=error_message)


    @pytest.mark.task(taskno=7)
    def test_sorted_names(self):
        test_data =(
        (['Steve', 'Ultron', 'Natasha', 'Rocket'], ['Natasha', 'Rocket', 'Steve', 'Ultron']),
        (['Agatha', 'Pepper', 'Valkyrie', 'Drax', 'Nebula'], ['Agatha', 'Drax', 'Nebula', 'Pepper', 'Valkyrie']),
        (['Gamora', 'Loki', 'Tony', 'Peggy', 'Okoye'], ['Gamora', 'Loki', 'Okoye', 'Peggy', 'Tony']),
        )

        for variant, (queue, expected) in enumerate(test_data, start=1):
            with self.subTest(f'variation #{variant}', queue=queue, expected=expected):
                actual_result = sorted_names(queue)
                expected_result = expected

            error_message = (f'\nCalled sorted_names({queue}).\n'
                             f'The function returned {actual_result}, but \n'
                             f'the tests expect {expected_result}.')

            self.assertEqual(actual_result, expected_result, msg=error_message)

    @pytest.mark.task(taskno=7)
    def test_sorted_names_validate_queue(self):
        test_data = (
        (['Steve', 'Ultron', 'Natasha', 'Rocket'], ['Natasha', 'Rocket', 'Steve', 'Ultron']),
        (['Agatha', 'Pepper', 'Valkyrie', 'Drax', 'Nebula'], ['Agatha', 'Drax', 'Nebula', 'Pepper', 'Valkyrie']),
        (['Gamora', 'Loki', 'Tony', 'Peggy', 'Okoye'], ['Gamora', 'Loki', 'Okoye', 'Peggy', 'Tony']),
        )

        for variant, (queue, expected) in enumerate(test_data, start=1):
            with self.subTest(f'variation #{variant}', queue=queue, expected=expected):

                # Deepcopy() is needed here because the input lists might be mutated.
                # That mutation wrecks havoc with the verification and error messaging.
                original_queue = deepcopy(queue)
                actual_result = sorted_names(queue)
                expected_result = expected

            error_message = (f'\nCalled sorted_names({original_queue}).\n'
                             f'The function returned {actual_result}, \n'
                             f'with a queue == {queue}.\n'
                             f'The tests expect {expected_result}, \n'
                             f'with a queue == {original_queue}.')

            self.assertIsNot(actual_result, queue, msg=error_message)
