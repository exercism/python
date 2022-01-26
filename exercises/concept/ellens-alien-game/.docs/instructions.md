# Instructions

Ellen is making a game where the player has to fight aliens.
She has just learned about Object Oriented Programming (OOP) and is eager to take advantage of what this paradigm has to offer.

To Ellen's delight, you have offered to help and she has given you the task of programming the aliens that the player has to fight.

## 1. Create the Alien Class

Define the Alien class so that it accepts an x and a y position, and puts them into `x` and `y` variables.
Every alien starts off with a health of 3, so initialize the `health` variable too.

```python
>>> alien = Alien(2, 0)
>>> alien.x
2
>>> alien.y
0
>>> alien.health
3
```

Now, each alien should be able to keep track of it's own position and health.

## 2. The `hit` Method

Ellen would like the Alien class to have a `hit` method that decrements the health of an alien object when it is called.
This way, she can simply call the `hit` method instead of having to manually change an alien's health.

For example:

```python
>>> alien = Alien(0, 0)
>>> alien.health
3 # same as before
>>> alien.hit()
>>> alien.health
2
```

## 3. The `is_alive` Method

You realize that if the health keeps decreasing, at some point it will probably hit 0 (or even less!).
It would be a good idea to add an `is_alive` method that Ellen can quickly call to check if the alien is... well... alive.

```python
>>> alien.health
1
>>> alien.is_alive()
True
>>> alien.hit()
>>> alien.health
0
>>> alien.is_alive()
False
```

## 4. The `teleport` Method

In Ellen's game, the aliens have the ability to teleport! 
You will need to write a `teleport` function that takes new x and y positions, and changes the alien's position accordingly.

```python
>>> alien.teleport(5, -4)
>>> alien.x
5
>>> alien.y
-4
```

## 5. The `collision_detection` Method

Obviously, if the aliens can be hit by something, then they need to be able to detect when such a collision has occurred.
However, collision detection algorithms can be tricky, and you do not yet know how to implement one.
Ellen has said that she will do it later, but she would still like the method to appear in the class.
It will need to take a variable of some kind (probably another object), but that's really all you know:

```python
>>> alien.collision_detection(other_object)
>>> 
```

## 6. Alien Counter

Ellen has come back with a new request for you.
She wants to keep track of how many aliens have been created over the game's lifetime.
She says that it's got something to do with the scoring system.

For example:

```python
>>> alien_one = Alien(5, 1)
>>> alien_one.total_aliens_created
1
>>> alien_two = ALien(3, 0)
>>> alien_two.total_aliens_created
2
>>> alien_one.total_aliens_created
2
```

## 7. Object Creation

Ellen loves what you've done so far, but she has a favor to ask.
She would like a standalone function that will create a list of alien objects, given a list of positions (as tuples).

For example:

```python
>>> alien_start_positions = [(4, 7), (-1, 0)]
>>> alien_list = new_alien_list(alien_start_positions)
>>> for alien in alien_list:
    	print(alien.x, alien.y)
4 7
-1 0
```
