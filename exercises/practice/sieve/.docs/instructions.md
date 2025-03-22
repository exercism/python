# Instructions

Your task is to create a program that implements the Sieve of Eratosthenes algorithm to find all prime numbers less than or equal to a given number.

A prime number is a number larger than 1 that is only divisible by 1 and itself.
For example, 2, 3, 5, 7, 11, and 13 are prime numbers.
By contrast, 6 is _not_ a prime number as it not only divisible by 1 and itself, but also by 2 and 3.

To use the Sieve of Eratosthenes, first, write out all the numbers from 2 up to and including your given number.
Then, follow these steps:

1. Find the next unmarked number (skipping over marked numbers).
   This is a prime number.
2. Mark all the multiples of that prime number as **not** prime.

Repeat the steps until you've gone through every number.
At the end, all the unmarked numbers are prime.

~~~~exercism/note
The Sieve of Eratosthenes marks off multiples of each prime using addition (repeatedly adding the prime) or multiplication (directly computing its multiples), rather than checking each number for divisibility.

The tests don't check that you've implemented the algorithm, only that you've come up with the correct primes.
~~~~

## Example

Let's say you're finding the primes less than or equal to 10.

- Write out 2, 3, 4, 5, 6, 7, 8, 9, 10, leaving them all unmarked.

  ```text
  2 3 4 5 6 7 8 9 10
  ```

- 2 is unmarked and is therefore a prime.
  Mark 4, 6, 8 and 10 as "not prime".

  ```text
  2 3 [4] 5 [6] 7 [8] 9 [10]
  ↑
  ```

- 3 is unmarked and is therefore a prime.
  Mark 6 and 9 as not prime _(marking 6 is optional - as it's already been marked)_.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
    ↑
  ```

- 4 is marked as "not prime", so we skip over it.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
       ↑
  ```

- 5 is unmarked and is therefore a prime.
  Mark 10 as not prime _(optional - as it's already been marked)_.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
          ↑
  ```

- 6 is marked as "not prime", so we skip over it.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
             ↑
  ```

- 7 is unmarked and is therefore a prime.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
                ↑
  ```

- 8 is marked as "not prime", so we skip over it.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
                   ↑
  ```

- 9 is marked as "not prime", so we skip over it.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
                       ↑
  ```

- 10 is marked as "not prime", so we stop as there are no more numbers to check.

  ```text
  2 3 [4] 5 [6] 7 [8] [9] [10]
                           ↑
  ```

You've examined all the numbers and found that 2, 3, 5, and 7 are still unmarked, meaning they're the primes less than or equal to 10.
