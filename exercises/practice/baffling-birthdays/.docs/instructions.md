# Instructions

Your task is to estimate the birthday paradox's probabilities.

To do this, you need to:

- Generate random birthdates.
- Check if a collection of randomly generated birthdates contains at least two with the same birthday.
- Estimate the probability that at least two people in a group share the same birthday for different group sizes.

~~~~exercism/note
A birthdate includes the full date of birth (year, month, and day), whereas a birthday refers only to the month and day, which repeat each year.
Two birthdates with the same month and day correspond to the same birthday.
~~~~

~~~~exercism/caution
The birthday paradox assumes that:

- There are 365 possible birthdays (no leap years).
- Each birthday is equally likely (uniform distribution).

Your implementation must follow these assumptions.
~~~~
