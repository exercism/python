# Instructions

In this exercise, you've been tasked with writing the software for an encryption device that works by performing transformations on data. You need a way to flexibly create complicated functions by combining simpler functions together.

For each task, return a function (using a `lambda`).


## 1. Create an adder

Implement `secret_add`. It should return a function which takes one argument and adds to it the argument passed in to `secret_add`.

```python
>>> adder = secret_add(2)
>>> adder(2)
4
```

## 2. Create a multiplier

Implement `secret_multiply`. It should return a function which takes one argument and multiplies it by the secret passed in to `secret_multiply`.

```python
>>> multiplier = secret_multiply(7)
>>> multiplier(3)
21
```

## 3. Create a "max"-er

Implement `secret_max`. It should return a function which takes one argument (a list of exactly two numbers) and returns either the secret passed into `secret_max`, or the argument passed into the function that `secret_max` returns, whichever one's **product** is bigger.

```python
>>> maxer = secret_max([7, 3])
>>> maxer([2, 11])
[2, 11]
```

## 4. Create a sorter

Implement `secret_sort`. It should take a number, `secret_index`, and return a lambda which takes one argument, a list of lists of an unknown amount of numbers. The lambda should return the list of lists, but sorted by `sublist[secret_index]`.

```python
>>> sorter = secret_sort(0)
>>> sorter([[3, 120, 5], [1, 5, 2], [8, 2, 23]])
[[1, 5, 2], [3, 120, 5], [8, 2, 23]]
```

## 5. Create a function combiner

Implement `secret_combine`. It should return a function which takes one argument and applies to it the two functions passed in to `secret_combine` in order.

```python
>>> multiply = secret_multiply(7)
>>> divide = secret_add(3)
>>> combined = secret_combine(multiply, add)

>>> combined(6)
25
```
