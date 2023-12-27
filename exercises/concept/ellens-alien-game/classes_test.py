import unittest
import pytest


try:
    from classes import Alien
except ImportError as import_fail:
    # pylint: disable=raise-missing-from
    raise ImportError("\n\nMISSING CLASS --> We tried to import the 'Alien' class from "
                      "your classes.py file, but could not find it." 
                      "Did you misname or forget to create it?") from None

try:
    from classes import new_aliens_collection
except ImportError as err:
    raise ImportError("\n\nMISSING FUNCTION --> We tried to import the "
                      "new_aliens_collection() function "
                      "from your classes.py file, but could not find it. "
                      "Did you misname or forget to create it?") from None


class ClassesTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_alien_has_correct_initial_coordinates(self):
        """Test that the Alien class gets correctly initialised."""

        alien = Alien(2, -1)
        error_message = (f'Created a new Alien by calling Alien(2, -1). '
                         f'The Alien was initialized to position '
                         f'{(alien.x_coordinate, alien.y_coordinate)}, but the tests expected '
                         f'the object to be at position (2, -1)')

        self.assertEqual((2, -1), (alien.x_coordinate, alien.y_coordinate), msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_alien_has_health(self):
        alien = Alien(0, 0)
        error_message = (f'Created a new Alien by calling Alien(0, 0). '
                         f'The new Alien has a health of {alien.health}, '
                         f'but the tests expect health = 3')

        self.assertEqual(3, alien.health, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_alien_instance_variables(self):
        """Test instance variables are unique to specific instances."""

        alien_one = Alien(-8, -1)
        alien_two = Alien(2, 5)

        coord_x_error = (f'Created two new Aliens by assigning '
                         f'alien_one = Alien(-8, -1) and alien_two = Alien(2, 5). '
                         f'Both Aliens x coordinates were {alien_two.x_coordinate}, '
                         f'but the tests expect alien_one and alien_two to have '
                         f'different x positions.')

        coord_y_error = (f'Created two new Aliens by assigning '
                         f'alien_one = Alien(-8, -1) and alien_two = Alien(2, 5). '
                         f'Both Aliens y coordinates were {alien_two.y_coordinate}, '
                         f'but the tests expect alien_one and alien_two to have '
                         f'different y positions.')

        self.assertFalse(alien_one.x_coordinate == alien_two.x_coordinate, msg=coord_x_error)
        self.assertFalse(alien_one.y_coordinate == alien_two.y_coordinate, msg=coord_y_error)


    @pytest.mark.task(taskno=2)
    def test_alien_hit_method(self):
        """Test class methods work as specified.

        There are two valid interpretations for this method/task.
        `self.health -= 1` and `self.health = max(0, self.health - 1)`
        The tests for this task reflect this ambiguity.

        """

        test_data = [1, 2, 3, 4, 5, 6]
        result_data = [(2,), (1,), (0,), (0, -1), (0, -2), (0, -3)]

        for variant, (iterations, expected) in enumerate(zip(test_data, result_data), start=1):
            alien = Alien(2, 2)

            with self.subTest(f'variation #{variant}',
                              iterations=iterations,
                              expected=expected):

                for _ in range(iterations):
                    alien.hit()

                error_message = (f'Called hit() {iterations} time(s) '
                                 f'on a newly created Alien. The Aliens health '
                                 f'is now {alien.health}, but the tests expected '
                                 f'it to be in {expected} after decrementing 1 health '
                                 f'point {iterations} time(s).')

                self.assertIn(alien.health, expected, msg=error_message)


    @pytest.mark.task(taskno=3)
    def test_alien_is_alive_method(self):
        alien = Alien(0, 1)

        alive_error = ('Created a new Alien and called hit(). '
                       'The function is_alive() is returning False (dead) '
                       'while alien.health is greater than 0.')

        dead_error = ('Created a new Alien and called hit(). '
                       'The function is_alive() is returning True (alive) '
                       'while alien.health is less than or equal to 0.')

        for _ in range(5):
            alien.hit()
            if alien.health > 0:
                self.assertTrue(alien.is_alive(), msg=alive_error)
            else:
                self.assertFalse(alien.is_alive(), msg=dead_error)

    @pytest.mark.task(taskno=4)
    def test_alien_teleport_method(self):
        alien = Alien(0, 0)
        alien.teleport(-1, -4)

        error_message = ('Called alien.teleport(-1,-4) on a newly created Alien. '
                         'The Alien was found at position '
                         f'{(alien.x_coordinate, alien.y_coordinate)}, but the '
                         'tests expected it at position (-1, -4).')

        self.assertEqual((-1, -4), (alien.x_coordinate, alien.y_coordinate), msg=error_message)

    @pytest.mark.task(taskno=5)
    def test_alien_collision_detection_method(self):
        alien = Alien(7, 3)
        error_message = ('Created a new Alien at (7,3) and called '
                         'alien.collision_detection(Alien(7, 2)). '
                         f'The method returned {alien.collision_detection(Alien(7, 2))}, '
                         'but the tests expected None. ')

        self.assertIsNone(alien.collision_detection(Alien(7, 2)), msg=error_message)


    @pytest.mark.task(taskno=6)
    def test_alien_class_variable(self):
        """Test class attribute/variables are identical across instances."""

        alien_one, alien_two = Alien(0, 2), Alien(-6, -1)
        Alien.health = 6

        created_error_message = ('Created two new Aliens and requested the '
                                 'total_aliens_created attribute for each one. '
                                 f'Received {alien_one.total_aliens_created, alien_two.total_aliens_created} '
                                 f'for total_aliens_created, but the tests expect '
                                 f'the class attributes for each newly created Alien to be identical. ')

        health_error_message = ('Created two new Aliens and requested the '
                                f'health attribute for each one. Received {alien_one.health, alien_two.health} '
                                'for health, but the tests expect the class '
                                'attributes for each newly created Alien to be identical. ')

        self.assertEqual(alien_two.total_aliens_created,
                         alien_one.total_aliens_created,
                         msg=created_error_message)

        self.assertEqual(alien_two.health,
                         alien_one.health,
                         msg=health_error_message)

    @pytest.mark.task(taskno=6)
    def test_alien_total_aliens_created(self):
        """Test total_aliens_created class variable increments upon object instantiation."""

        Alien.total_aliens_created = 0
        aliens = [Alien(-2, 6)]

        error_message = ('Created a new Alien and called total_aliens_created for it. '
                         f'{aliens[0].total_aliens_created} was returned, but '
                         'the tests expected that total_aliens_created would equal 1.')

        self.assertEqual(1, aliens[0].total_aliens_created, msg=error_message)

        aliens.append(Alien(3, 5))
        aliens.append(Alien(-5, -5))

        def error_text(alien, variable):
            return ('Created two additional Aliens for the session.'
                    f"Alien number {alien}'s total_aliens_created variable "
                    f"is equal to {variable}, but the tests expected all "
                    'total_aliens_created variables for all instances to be '
                    'equal to number of alien instances created (i.e. 3).')

        self.assertEqual(3, aliens[0].total_aliens_created, msg=error_text(1, aliens[0]))
        self.assertEqual(3, aliens[1].total_aliens_created, msg=error_text(2, aliens[1]))
        self.assertEqual(3, aliens[2].total_aliens_created, msg=error_text(3, aliens[2]))

    @pytest.mark.task(taskno=7)
    def test_new_aliens_collection(self):
        """Test that the user knows how to create objects themselves."""

        test_data = [(-2, 6), (1, 5), (-4, -3)]
        actual_result = new_aliens_collection(test_data)

        error_message = "new_aliens_collection() must return a list of Alien objects."

        for obj in actual_result:
            self.assertIsInstance(obj, Alien, msg=error_message)

        for position, obj in zip(test_data, actual_result):
            position_error = (f'After calling new_aliens_collection({test_data}), '
                              f'found {obj} initialized to position {(obj.x_coordinate, obj.y_coordinate)}, '
                              f'but the tests expected {obj} to be at position {position} instead.')

            self.assertEqual(position, (obj.x_coordinate, obj.y_coordinate), msg=position_error)
