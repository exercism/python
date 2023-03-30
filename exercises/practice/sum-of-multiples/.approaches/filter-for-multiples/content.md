# `filter` for multiples

```python
def sum_of_multiples(limit, factors):
    is_multiple = lambda n: any(n % f == 0 for f in factors if f != 0)
    return sum(filter(is_multiple, range(limit)))
```

Probably the most straightforward way of solving this problem is to

1. look at every individual integer between `0` and `limit`,
2. check that it is a multiple of any of the given `factors`, and
3. add it to the sum when it is.


## Notable language features used in this solution

### Built-in function: `sum`

Adding all the numbers in a collection together is a very common operation.
Therefore, Python provides the built-in function [`sum`][builtin-sum].

`sum` takes one argument, and requires that it be **iterable**.
A value is iterable whenever it makes sense to use it in a `for` loop like this:

```python
for _ in iterable_value:  # 👈
    ...
```

The `list` is the most commonly used iterable data structure.
Many other containers are also iterable, such as `set`s, `tuple`s, `range`s, and even `dict`s and `str`ings.
Still other examples include iterators and generators, which are discuss below.

When given such a collection of numbers, `sum` will look at the elements one by one and add them together.
The result is a single number.

```python
numbers = range(1, 100 + 1)  # 1, 2, …, 100
sum(numbers)
# ⟹ 5050
```

Had the highlighted solution not used `sum`, it might have looked like this:

```python
def sum_of_multiples(limit, factors):
    is_multiple = lambda n: any(n % f == 0 for f in factors if f != 0)
    total = 0
    for multiple in filter(is_multiple, range(limit)):
        total += total
    return total
```


### Built-in function: `filter`

Selecting elements of a collection for having a certain property is also a very common operation.
Therefore, Python provides the built-in function [`filter`][builtin-filter].

`filter` takes two arguments.
The first is a **predicate**.
The second is the iterable the elements of which should be filtered.

A predicate is a function that takes one argument (of any particular type) and returns a `bool`.
Such functions are commonly used to encode properties of values.
An example is `str.isupper`, which takes a `str` and returns `True` whenever it is uppercase:

```python
str.isupper("AAAAH! 😱")  # ⟹ True
str.isupper("Eh? 😕")     # ⟹ False
str.isupper("⬆️💼")       # ⟹ False
```

Thus, the function `str.isupper` represents the property of _being an uppercase string_.

Contrary to what you might expect, `filter` does not return a data structure like the one given as an argument:

```python
filter(str.isupper, ["THUNDERBOLTS", "and", "LIGHTNING"])
# ⟹ <filter object at 0x000002F46B107BE0>
```

Instead, it returns an **iterator**.

An iterator is an object whose sole purpose is to guide iteration through some data structure.
In particular, `filter` makes sure that elements that do not satisfy the predicate are skipped.
It is a bit like a cursor that can move only to the right.

The main differences between containers (such as `list`s) and iterators are

- Containers can, depending on their contents, take up a lot of space in memory, but iterators are generally very small (regardless of how many elements they 'contain').
- Containers can be iterated over multiple times, but iterators can be used only once.

To illustrate the latter difference:

```python
is_even = lambda n: n % 2 == 0
numbers = range(20)                      # 0, 1, …, 19
even_numbers = filter(is_even, numbers)  # 0, 2, …, 18
sum(numbers)       # ⟹ 190
sum(numbers)       # ⟹ 190
sum(even_numbers)  # ⟹ 90
sum(even_numbers)  # ⟹ 0
```

Here, `sum` iterates over both `numbers` and `even_numbers` twice.

In the case of `numbers` everything is fine.
Even after looping through the whole of `numbers`, all its elements are still there, and so `sum` can ask to see them again without problem.

The situation with `even_numbers` is move involved.
To use the _cursor_ analogy: after going through all of `even_number`'s 'elements' &ndash; actually elements of `numbers` &ndash; the cursor has moved all the way to the right.
It cannot move backwards, so if you wish to iterate over all even numbers then you need a new cursor.
We say the the `even_numbers` iterator is _exhausted_. When `sum` asks for its elements again, `even_numbers` comes up empty and so `sum` returns `0`.

Had the highlighted solution not used `filter`, it might have looked like this:

```python
def sum_of_multiples(limit, factors):
    is_multiple = lambda n: any(n % f == 0 for f in factors if f != 0)
    multiples = [candidate for candidate in range(limit) if is_multiple(candidate)]
    return sum(multiples)
```

This variant stores all the multiples in a `list` before summing them.
Such a list can potentially be very big.
For example, if `limit = 1_000_000_000` and `factors = [1]` then `multiples` will be a list 8 gigabytes large!
It is to avoid unnecessarily creating such large intermediate data structures that iterators are often used.


### A function expression: `lambda`

...


### Built-in function: `any`

...


### A generator expression

...


## Reflections on this approach

An important advantage of this approach is that it is very easy to understand.
However, it suffers from potentially performing a lot of unnecessary work, for example when all `factors` are large, or when there are no `factors` at all.

<!-- TODO elaborate -->


[builtin-sum]: https://docs.python.org/3/library/functions.html#sum "Built-in Functions: sum"
[builtin-filter]: https://docs.python.org/3/library/functions.html#filter "Built-in Functions: filter"
