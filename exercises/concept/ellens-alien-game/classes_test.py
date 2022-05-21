import unittest
import pytest


try:
    from classes import new_aliens_collection
except ImportError as err:
    raise ImportError("We tried to import the new_aliens_collection() function, "
                      "but could not find it. Did you remember to create it?") from err

try:
    from classes import Alien
except ImportError as err:
    raise ImportError("We tried to import the 'Alien' class from the classes.py file, but could not find it. "
                      "Did you remember to create it?") from err


class ClassesTest(unittest.TestCase):
    # Test Alien class exists and correctly initialised.
    @pytest.mark.task(taskno=1)
    def test_alien_has_correct_initial_coordinates(self):
        alien = Alien(2, -1)
        error = ("Expected object to be at position (2, -1) but instead "
                 f"found it initialized to position {(alien.x_coordinate, alien.y_coordinate)}.")

        self.assertEqual((2, -1), (alien.x_coordinate, alien.y_coordinate), msg=error)

    @pytest.mark.task(taskno=1)
    def test_alien_has_health(self):
        alien = Alien(0, 0)
        error = ("Expected object's health to be 3 but instead found "
                 f"it had a health of {alien.health}.")

        self.assertEqual(3, alien.health, msg=error)

    # Test instance variables are unique to specific instances.
    @pytest.mark.task(taskno=1)
    def test_alien_instance_variables(self):
        alien_one = Alien(-8, -1)
        alien_two = Alien(2, 5)

        coord_x_error = ("Expected alien_one and alien_two to have different x "
                         f"positions. Instead both x's were: {alien_two.x_coordinate}.")
        coord_y_error = ("Expected alien_one and alien_two to have different y "
                         f"positions. Instead both y's were: {alien_two.y_coordinate}.")

        self.assertFalse(alien_one.x_coordinate == alien_two.x_coordinate, msg=coord_x_error)
        self.assertFalse(alien_one.y_coordinate == alien_two.y_coordinate, msg=coord_y_error)

    # Test class methods work as specified.
    @pytest.mark.task(taskno=2)
    def test_alien_hit_method(self):
        #There are two valid interpretations for this method/task.
        #`self.health -= 1` and `self.health = max(0, self.health - 1)`
        #The tests for this task reflect this ambiguity.

        data = [(1, (2,)), (2, (1,)), (3, (0,)), (4, (0, -1)), (5, (0, -2)), (6, (0, -3))]
        for variant, (iterations, result) in enumerate(data, 1):
            alien = Alien(2, 2)
            with self.subTest(f'variation #{variant}', input=iterations, output=result):
                error = ("Expected hit method to decrement health by 1. "
                         f"Health is {alien.health} when it should be {result}.")
                for _ in range(iterations):
                    alien.hit()
                self.assertIn(alien.health, result, msg=error)


    @pytest.mark.task(taskno=3)
    def test_alien_is_alive_method(self):
        alien = Alien(0, 1)
        alive_error = "Alien is dead while health is greater than 0."
        dead_error = "Alien is alive while health is less than or equal to 0."

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

        error = (
            "Expected alien to be at position (-1, -4) but "
            f"instead found it in position {(alien.x_coordinate, alien.y_coordinate)}.")

        self.assertEqual((-1, -4), (alien.x_coordinate, alien.y_coordinate), msg=error)

    @pytest.mark.task(taskno=5)
    def test_alien_collision_detection_method(self):
        alien = Alien(7, 3)
        error = "Expected collision_detection method to not be implemented."

        self.assertIsNone(alien.collision_detection(Alien(7, 2)), msg=error)

    # Test class variables are identical across instances
    @pytest.mark.task(taskno=6)
    def test_alien_class_variable(self):
        alien_one = Alien(0, 2)
        alien_two = Alien(-6, -1)
        Alien.total_aliens_created = -2

        error_one = "Expected the total_aliens_created variable to be identical."
        error_two = "Expected the health variable to be identical."

        self.assertEqual(alien_two.total_aliens_created, alien_one.total_aliens_created, msg=error_one)
        self.assertEqual(alien_two.health, alien_one.health, msg=error_two)

    # Test total_aliens_created increments upon object instantiation
    @pytest.mark.task(taskno=6)
    def test_alien_total_aliens_created(self):
        Alien.total_aliens_created = 0
        aliens = [Alien(-2, 6)]
        error = ("Expected total_aliens_created to equal 1. Instead "
                 f"it equals: {aliens[0].total_aliens_created}.")

        self.assertEqual(1, aliens[0].total_aliens_created, msg=error)

        aliens.append(Alien(3, 5))
        aliens.append(Alien(-5, -5))

        def error_text(alien, variable):
            return (
                "Expected all total_aliens_created variables to be "
                "equal to number of alien instances (i.e. 3).  Alien "
                f"number {alien}'s total_aliens_created variable "
                f"is equal to {variable}.")

        tac_list = [alien.total_aliens_created for alien in aliens]

        self.assertEqual(3, tac_list[0], msg=error_text(1, tac_list[0]))
        self.assertEqual(3, tac_list[1], msg=error_text(2, tac_list[1]))
        self.assertEqual(3, tac_list[2], msg=error_text(3, tac_list[2]))

    # Test that the user knows how to create objects themselves
    @pytest.mark.task(taskno=7)
    def test_new_aliens_collection(self):
        position_data = [(-2, 6), (1, 5), (-4, -3)]
        obj_list = new_aliens_collection(position_data)
        obj_error = "new_aliens_collection must return a list of Alien objects."

        for obj, position in zip(obj_list, position_data):
            self.assertIsInstance(obj, Alien, msg=obj_error)

            pos_error = (
                f"Expected object to be at position {position} but "
                f"instead found it initialized to position {(obj.x_coordinate, obj.y_coordinate)}.")

            self.assertEqual(position, (obj.x_coordinate, obj.y_coordinate), msg=pos_error)
