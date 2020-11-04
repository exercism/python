## loops

## Loops in Python

There are 2 general ways in Python to loop through objects.

- `while` loop (_indefinite_, or _uncounted_)
- `for` loop (_definite_, or _counted_)

## While loops

While loops are _uncounted_ and based on a `conditional` statement for looping through objects.

```
while expression:
    set_of_statements
```

When the statement evaluates to `True`, the loop advances and executes the code in the indented block - or "body" of the loop. Looping continues in this fashion until the conditional statement evaluates to `False`.

```python
i = 0
while i < 3:
    print(i)
# => 0
# => 1
# => 2
```

## For Loops

Unlike `while` loops, `for` loops are based on a counter. The Loop will execute until the counter/object being counted is exhausted. The counter in this case could be the indexes in a `list`, `string`, or `tuple` -- or the indexes in a `range()` object.

```python
for item in countable_object:
    set_of_statements
```

```python
>>> numbers = [1, 2, 3, 4, 5]

>>> for number in numbers:
         print(number)
#=> 1
#=> 2
#=> 3
#=> 4
#=> 5
```

## Breaking from loops

Where you have a large set of objects that you want to loop through but would like to stop the loop execution when a certain condition is met, the `break` statement comes to the rescue.

```python
list_of_items = [1, 2, 3, 4, 5, 6, 7, 8]
for item in list_of_items:
    if item > 5:
        break
    print(item)
# => 1
# => 2
# => 3
# => 4
# => 5
```

## Continuing in loops

You will have important objects as well as non important ones. When you want to skip over the objects that you don't need to process you use the `continue` statement.

Example: you want to process only odd numbers in a loop and not the event numbers.

```python
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in all_numbers:
    if num % 2 == 0:
        continue
    print(num)
# => 1
# => 3
# => 5
# => 7
```
