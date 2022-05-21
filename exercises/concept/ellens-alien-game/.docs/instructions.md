# Instructions

Ellen is making a game where the player has to fight aliens.
She has just learned about Object Oriented Programming (OOP) and is eager to take advantage of what using `classes` could offer her program.

To Ellen's delight, you have offered to help and she has given you the task of programming the aliens that the player has to fight.


## 1. Create the Alien Class

Define the Alien class with a constructor that accepts two parameters `<x_coordinate>` and `<y_coordinate>`, putting them into `x_coordinate` and `y_coordinate` instance variables.
Every alien will also start off with a health level of 3, so the `health` variable should be initialized as well.

```python
>>> alien = Alien(2, 0)
>>> alien.x_coordinate
2
>>> alien.y_coordinate
0
>>> alien.health
3
```

Now, each alien should be able to internally track its own position and health.

## 2. The `hit` Method

Ellen would like the Alien `class` to have a `hit` method that decrements the health of an alien object by 1 when called.
This way, she can simply call `<alien>.hit()` instead of having to manually change an alien's health.
It is up to you if `hit()` takes healths points _to_ or _below_ zero.

```python
>>> alien = Alien(0, 0)
>>> alien.health

# Initialized health value.
3

# Decrements health by 1 point.
>>> alien.hit()
>>> alien.health
2
```

## 3. The `is_alive` Method

You realize that if the health keeps decreasing, at some point it will probably hit 0 (_or even less!_).
It would be a good idea to add an `is_alive` method that Ellen can quickly call to check if the alien is... well... alive. 😉
`<alien>.is_alive()` should return a boolean.

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
You will need to write a `teleport` method that takes new `x_coordinate` and `y_coordinate` values, and changes the alien's coordinates accordingly.

```python
>>> alien.teleport(5, -4)
>>> alien.x_coordinate
5
>>> alien.y_coordinate
-4
```

## 5. The `collision_detection` Method

Obviously, if the aliens can be hit by something, then they need to be able to detect when such a collision has occurred.
However, collision detection algorithms can be tricky, and you do not yet know how to implement one.
Ellen has said that she will do it later, but she would still like the `collision_detection` method to appear in the class as a reminder to build out the functionality.
It will need to take a variable of some kind (probably another object), but that's really all you know.
You will need to make sure that putting the method definition into the class doesn't cause any errors when called:

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
>>> alien_two = Alien(3, 0)
>>> alien_two.total_aliens_created
2
>>> alien_one.total_aliens_created
2
>>> Alien.total_aliens_created
# Accessing the variable from the class directly
2
```

## 7. Creating a List of Aliens

Ellen loves what you've done so far, but she has one more favor to ask.
She would like a standalone (_outside the `Alien()` class_) function that creates a `list` of `Alien()` objects, given a list of positions (as `tuples`).

For example:

```python
>>> alien_start_positions = [(4, 7), (-1, 0)]
>>> aliens = new_aliens_collection(alien_start_positions)
...
>>> for alien in aliens:
    	print(alien.x_coordinate, alien.y_coordinate)
(4, 7)
(-1, 0)
```
