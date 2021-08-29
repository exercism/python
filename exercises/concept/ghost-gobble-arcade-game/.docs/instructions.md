# Instructions

In this exercise, you need to implement some rules from [Pac-Man][Pac-Man], the classic 1980s-era arcade-game.

You have four rules to implement, all related to the game states.

> _Do not worry about how the arguments are derived, just focus on combining the arguments to return the intended result._

## 1. Define if Pac-Man eats a ghost

Define the `eat_ghost()` function that takes two parameters (_if Pac-Man has a power pellet active_ and _if Pac-Man is touching a ghost_) and returns a Boolean value if Pac-Man is able to eat the ghost.
 The function should return `True` only if Pac-Man has a power pellet active and is touching a ghost.

```python
>>> eat_ghost(False, True)
...
False
```

## 2. Define if Pac-Man scores

Define the `score()` function that takes two parameters (_if Pac-Man is touching a power pellet_ and _if Pac-Man is touching a dot_) and returns a Boolean value if Pac-Man scored.
 The function should return `True` if Pac-Man is touching a power pellet or a dot.

```python
>>> score(True, True)
...
True
```

## 3. Define if Pac-Man loses

Define the `lose()` function that takes two parameters (_if Pac-Man has a power pellet active_ and _if Pac-Man is touching a ghost_) and returns a Boolean value if Pac-Man loses.
 The function should return `True` if Pac-Man is touching a ghost and does not have a power pellet active.

```python
>>> lose(False, True)
...
True
```

## 4. Define if Pac-Man wins

Define the `win()` function that takes three parameters (_if Pac-Man has eaten all of the dots_, _if Pac-Man has a power pellet active_, and _if Pac-Man is touching a ghost_) and returns a Boolean value if Pac-Man wins.
 The function should return `True` if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.

```python
>>> win(False, True, False)
...
False
```

[Pac-Man]: https://en.wikipedia.org/wiki/Pac-Man
