In this exercise, you're going to implement some rules from [Blackjack][blackjack]

You have some rules to implement for judging the result of the game.

**Note** : In this exercise, _A_ means an ace, _J_ means jack, _Q_ means queen, and _K_ means king card.

## 1. Calculate the number of card

Create the `number_of_card()` function with a parameter `card`. The value of _J, Q_ or _K_ is 10. If the `card` is _A_, then just return "ace".

```python
>>> number_of_card('K')
10
>>> number_of_card('A')
ace
```

## 2. Calculate the number of Ace

Create the `number_of_ace()` function with a parameter `hand`.

1. `hand` : the sum of cards in hand with an ace.

Ace is 1 or 11. You have to decide the value of ace without the sum of hand exceeding 21.

```python
>>> number_of_ace(19)
1
>>> number_of_ace(7)
11
```

## 3. Judge Blackjack

Create the `blackjack()` function with a parameter `hand`.

1. `hand` : first two cards in hand.

This function should return if the hand is blackjack. There's must be an ace card in `hand`.

**Note** : If the player has an Ace and a ten-value card, it is called a _Blackjack_. Ten-value cards include _10, J, Q, K_. I think you may have many ways. But if you can, use a way to check if there are an ace and a ten-value in the list.

```python
>>> blackjack(['A', 'K'])
True
>>> blackjack([10, 9])
False
```

[blackjack]: https://en.wikipedia.org/wiki/Blackjack