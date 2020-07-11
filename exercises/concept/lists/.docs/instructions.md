## Instructions

As a magician-to-be, Elyse needs to practice some basics. She has a stack of cards that she wants to manipulate. In this exercise we'll use lists to help Elyse perform her card tricks.

[//]: # 'Creating Lists'

## 1. Creating a List

Some magic tricks involve forming a [hand](https://en.wikipedia.org/wiki/Glossary_of_card_game_terms#hand) as in a regular card game, e.g. forming a single hand from five individual cards.

Implement a function `to_list` that takes five arguments and returns a single list with those arguments as its elements:

```python
>>> to_list('10H', 'JH', 'QH', 'KH', 'AH')
['10H', 'JH', 'QH', 'KH', 'AH']
```

[//]: # 'Create Lists Using the `list` Type'

## 2. Creating a copy of a List

In a traditional deck of cards, each card is unique and only occurs once. But for some magic tricks, Elyse needs to sneak in duplicate copies of some cards.

Implement a function `list_twice` that takes a single list as its only argument, and returns a list which consists of two copies of the input list:

```python
>>> list_twice(['AC', 'AD', 'AH', 'AS'])
[['AC', 'AD', 'AH', 'AS'], ['AC', 'AD', 'AH', 'AS']]
```

[//]: # 'Concatenating Lists Using the `+` Operator'

## 3. Concatenating Lists

For some tricks, Elyse needs to take two stacks of cards and put one on top of the other

Implement a function `concatenate_lists` that takes two lists and returns a single list consisting of all the elements in the first list, followed by all the elements in the second list:

```python
>>> concatenate_lists(['2C', '2H', '2D'], ['KC', 'KD'])
['2C', '2H', '2D', 'KC', 'KD']
```

[//]: # 'Checking for List Membership using the `in` keyword'

## 4. Testing List Membership

Elyse is practicing one particular trick in which she has a volunteer select a set of cards from the deck, and she has to guess whether a certain card is in their hand.

Implement a function `list_contains_object` that takes two arguments, an arbitrary object and a list, and returns `True` if the object is an element of the list:

```python
>>> list_contains_object(['AC', 'AD', 'AH', 'AS'], 'AC')
True

>>> list_contains_object(['AC', 'AD', 'AH', 'AS'], '10C')
False
```

[//]: # 'Accessing List Elements by Index'

## 5. Accessing List Elements by Index

For some tricks, Elyse needs to be able to take cards from the top and bottom of the deck through slight-of-hand.

Implement a function `first_and_last` that returns the first and last elements from a list:

```python
>>> first_and_last(['2C', '2H', '2D', 'KC', 'KD'])
['2C', 'KD']
```

[//]: # 'Accessing Sublists by Slicing'

## 6. Accessing Sublists by Slicing

For other tricks, Elyse needs to be able to take some cards from inbetween other cards through slight-of-hand.

Implement a function `interior_of_list` that returns all elements of a list _except_ for the first and last elements:

```python
>>> interior_of_list(['2C', '2H', '2D', 'KC', 'KD'])
['2H', '2D', 'KC']
```

One of Elyse's most amazing tricks to reorder a shuffled deck.

Implement a function `even_elements` that returns every element of even index from a list:

```python
>>> even_elements(['2C', '2H', '2D', 'KC', 'KD'])
['2C', '2D', 'KD']
```

Implement a function `odd_elements` that returns every element of odd index from a list:

```python
>>> odd_elements(['2C', '2H', '2D', 'KC', 'KD'])
['2H', 'KC']
```

Implement a function `unshuffle` that "unshuffles" a set of cards by appending the elements of odd index to the elements of even index:

```python
>>> unshuffle(['2C', '2H', '2D', 'KC', 'KD'])
['2C', '2D', 'KD', '2H', 'KC']
```

## 7. Iterating Over List Items

For some tricks, Elyse guesses all the cards in a volunteers hands and names them out loud.

Implement a function `print_list` that prints each element of a list on a separate line:

```python
>>> print_list(['2C', '2H', '2D', 'KC', 'KD'])
2C
2H
2D
KC
KD
```

## 8. Creating Lists with Mixed Data Types

For some tricks, Elyse sneaks in objects that aren't even playing cards!

Suppose that you're given a function `count_types` that returns a count of the number of distinct types that occur in a given list:

```python
>>> count_types(['2C', '2H', '2D', 'KC', 'KD'])
1
>>> count_types([1, 2, 3])
1
>>> count_types(['2C', '2H', '2D', 'KC', 'KD', 1, 2, 3])
2
```

Write a function `multitype_list` that returns a list of elements of at least three different types:

```python
>>> count_types(multitype_list()) > 2
True
```

## 9. Modifying Values in Lists

For some tricks, Elyse needs to use sleight-of-hand to swap cards without anyone noticing.

Implement a function `swap_first_and_last` that takes a list and swaps the positions of the first and last elements in the list:

```python
>>> _list = ['2C', '2H', '2D', 'KC', 'KD']
>>> swap_first_and_last(_list)
>>> _list
['KD', '2H', '2D', 'KC', '2C']
```
