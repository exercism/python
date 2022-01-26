import unittest

from alien_class import (
    Alien,
    new_alien_list
)

class ClassesTest(unittest.TestCase):
    # Test Alien class exists and correctly initialised
    def test_can_create_one_alien_instance(self):
        Alien(1, 5)
        
    def test_alien_has_correct_initial_x_and_y(self):
        alien = Alien(2, -1)
        error = (
            "Expected object to be at position (2, -1) but instead "
            f"found it initialized to position {(alien.x, alien.y)}.")
        
        self.assertEqual((2, -1), (alien.x, alien.y), msg=error)
        
    def test_alien_has_health(self):
        alien = Alien(0, 0)
        error = (
            "Expected object's health to be 3 but instead found "
            f"it had a health of {alien.health}.")
        
        self.assertEqual(3, alien.health, msg=error)
        
    # Test class variables are identical across instances
    def test_alien_class_variable(self):
        alien_one = Alien(0, 2)
        alien_two = Alien(-6, -1)
        Alien.total_aliens_created = -2
        
        error_one = "Expected the total_aliens_created variable to be identical."
        error_two = "Expected the health variable to be identical."
        
        self.assertEqual(alien_two.total_aliens_created,
                         alien_one.total_aliens_created,
                         msg=error_one)
        self.assertEqual(alien_two.health, alien_one.health, msg=error_two)
        
    # Test instance variables are unique to specific instances
    def test_alien_instance_variables(self):
        alien_one = Alien(-8, -1)
        alien_two = Alien(2, 5)
        
        pos_x_error = (
            "Expected alien_one and alien_two to have different x "
            f"positions. Instead both x's were: {alien_two.x}")
        pos_y_error = (
            "Expected alien_one and alien_two to have different y "
            f"positions. Instead both y's were: {alien_two.y}")
        
        self.assertFalse(alien_one.x == alien_two.x, msg=pos_x_error)
        self.assertFalse(alien_one.y == alien_two.y, msg=pos_y_error)
    
    # Test total_aliens_created increments upon object instantiation
    def test_alien_total_aliens_created(self):
        Alien.total_aliens_created = 0
        alien_one = Alien(-2, 6)
        error = (
            "Expected total_aliens_created to equal 1. Instead "
            f"it equals: {alien_one.total_aliens_created}.")
        
        self.assertEqual(1, alien_one.total_aliens_created, msg=error)
        
        alien_two = Alien(3, 5)
        alien_three = Alien(-5, -5)
        
        def error_text(alien, variable):
            return (
                "Expected all total_aliens_created variables to be "
                "equal to number of alien instances (i.e. 3).  Alien "
                f"number {alien}'s total_aliens_created variable "
                f"is equal to {variable}")
        
        tec_one = alien_one.total_aliens_created
        tec_two = alien_two.total_aliens_created
        tec_three = alien_three.total_aliens_created
        
        self.assertEqual(3, tec_one, msg=error_text(1, tec_one))
        self.assertEqual(3, tec_two, msg=error_text(2, tec_two))
        self.assertEqual(3, tec_three, msg=error_text(3, tec_three))
    
    # Test class methods work as specified
    def test_alien_hit_method(self):
        alien = Alien(2, 2)
        
        for i in range(3, -3, -1):
            error = (
                "Expected hit method to decrement health by 1. "
                f"Health is {alien.health} when it should be {i}")
            
            self.assertEqual(i, alien.health, msg=error)
            alien.hit()
        
    def test_alien_is_alive_method(self):
        alien = Alien(0, 1)
        alive_error = "Alien is dead while health is greater than 0"
        dead_error = "Alien is alive while health is less than or equal to 0"
            
        for _ in range(6):
            if alien.health > 0:
                self.assertTrue(alien.is_alive(), msg=alive_error)
            else:
                self.assertFalse(alien.is_alive(), msg=dead_error)
            alien.health -= 1
    
    def test_alien_teleport_method(self):
        alien = Alien(0, 0)
        alien.teleport(-1, -4)
            
        error = (
            "Expected alien to be at position (-1, -4) but "
            f"instead found it in position {(alien.x, alien.y)}.")
        
        self.assertEqual((-1, -4), (alien.x, alien.y), msg=error)
        
    def test_alien_collision_detection_method(self):
        alien = Alien(7, 3)
        error = "Expected collision_detection method to not be implemented"
        
        self.assertIsNone(alien.collision_detection(Alien(7, 2)), msg=error)
        
    # Test that the user knows how to create objects themselves
    def test_new_alien_list_function(self):
         position_data = [(-2,  6),
                          ( 1,  5),
                          (-4, -3)]
         obj_list = new_alien_list(position_data)
         obj_error = "new_alien_list must return a list of Alien objects."
         
         for obj, position in zip(obj_list, position_data):
             self.assertIsInstance(obj, Alien, msg=obj_error)
             
             pos_error = (
                 f"Expected object to be at position {position} but "
                 f"instead found it initialized to position {(obj.x, obj.y)}.")
             
             self.assertEqual(position, (obj.x, obj.y), msg=pos_error)
