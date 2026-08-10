# Instructions

In this exercise, you will simulate a game very similar to the classic card game **Camicia**.
Your program will receive the initial configuration of two players' decks and must simulate the game until it ends (or detect that it will never end).

## Rules

- The deck is split between **two players**.
  The player's cards are read from left to right, where the leftmost card is the top of the deck.
- A round consists of both players playing at least one card.
- Players take turns placing the **top card** of their deck onto a central pile.
- If the card is a **number card** (2-10), play simply passes to the other player.
- If the card is a **payment card**, a penalty must be paid:
  - **J** → opponent must pay 1 card
  - **Q** → opponent must pay 2 cards
  - **K** → opponent must pay 3 cards
  - **A** → opponent must pay 4 cards
- If the player paying a penalty reveals another payment card, that player stops paying the penalty.
  The other player must then pay a penalty based on the new payment card.
- If the penalty is fully paid without interruption, the player who placed the **last payment card** collects the central pile and places it at the bottom of their deck.
  That player then starts the next round.
- If a player runs out of cards and is unable to play a card (either while paying a penalty or when it is their turn), the other player collects the central pile.
- The moment when a player collects cards from the central pile is called a **trick**.
- If a player has all the cards in their possession after a trick, the game **ends**.
- The game **enters a loop** as soon as the decks are identical to what they were earlier during the game, **not** counting number cards!

## Examples

A small example of a match that ends.

| Round | Player A     | Player B                   | Pile                       | Penalty Due |
| :---- | :----------- | :------------------------- | :------------------------- | :---------- |
| 1     | 2 A 7 8 Q 10 | 3 4 5 6 K 9 J              |                            | -           |
| 1     | A 7 8 Q 10   | 3 4 5 6 K 9 J              | 2                          | -           |
| 1     | A 7 8 Q 10   | 4 5 6 K 9 J                | 2 3                        | -           |
| 1     | 7 8 Q 10     | 4 5 6 K 9 J                | 2 3 A                      | Player B: 4 |
| 1     | 7 8 Q 10     | 5 6 K 9 J                  | 2 3 A 4                    | Player B: 3 |
| 1     | 7 8 Q 10     | 6 K 9 J                    | 2 3 A 4 5                  | Player B: 2 |
| 1     | 7 8 Q 10     | K 9 J                      | 2 3 A 4 5 6                | Player B: 1 |
| 1     | 7 8 Q 10     | 9 J                        | 2 3 A 4 5 6 K              | Player A: 3 |
| 1     | 8 Q 10       | 9 J                        | 2 3 A 4 5 6 K 7            | Player A: 2 |
| 1     | Q 10         | 9 J                        | 2 3 A 4 5 6 K 7 8          | Player A: 1 |
| 1     | 10           | 9 J                        | 2 3 A 4 5 6 K 7 8 Q        | Player B: 2 |
| 1     | 10           | J                          | 2 3 A 4 5 6 K 7 8 Q 9      | Player B: 1 |
| 1     | 10           | -                          | 2 3 A 4 5 6 K 7 8 Q 9 J    | Player A: 1 |
| 1     | -            | -                          | 2 3 A 4 5 6 K 7 8 Q 9 J 10 | -           |
| 2     | -            | 2 3 A 4 5 6 K 7 8 Q 9 J 10 | -                          | -           |

status: `"finished"`, cards: 13, tricks: 1

This is a small example of a match that loops.

| Round | Player A | Player B | Pile  | Penalty Due |
| :---- | :------- | :------- | :---- | :---------- |
| 1     | J 2 3    | 4 J 5    | -     | -           |
| 1     | 2 3      | 4 J 5    | J     | Player B: 1 |
| 1     | 2 3      | J 5      | J 4   | -           |
| 2     | 2 3 J 4  | J 5      | -     | -           |
| 2     | 3 J 4    | J 5      | 2     | -           |
| 2     | 3 J 4    | 5        | 2 J   | Player A: 1 |
| 2     | J 4      | 5        | 2 J 3 | -           |
| 3     | J 4      | 5 2 J 3  | -     | -           |
| 3     | J 4      | 2 J 3    | 5     | -           |
| 3     | 4        | 2 J 3    | 5 J   | Player B: 1 |
| 3     | 4        | J 3      | 5 J 2 | -           |
| 4     | 4 5 J 2  | J 3      | -     | -           |

The start of round 4 matches the start of round 2.
Recall, the value of the number cards does not matter.

status: `"loop"`, cards: 8, tricks: 3

## Your Task

- Using the input, simulate the game following the rules above.
- Determine the following information regarding the game:
  - **Status**: `"finished"` or `"loop"`
  - **Cards**: total number of cards played throughout the game
  - **Tricks**: number of times the central pile was collected

~~~~exercism/advanced
For those who want to take on a more exciting challenge, the hunt for other records for the longest game with an end is still open.
There are 653,534,134,886,878,245,000 (approximately 654 quintillion) possibilities, and we haven't calculated them all yet!
~~~~
