## Loops in Python

There is always a scenario where you would need to go through a [`list` or `group`] of [`things` or `object` or `values`].
When you have an `array` of objects or values to process, you need to `iterate` on the array and process them. You are going to do a repeated set of instructions on every single object or value in an array.

There are 2 ways to loop through objects.

- `while` loop
- `for` loop

## While loops

While loops are based on `conditional` statement for looping through objects.

```
while expression:
    set_of_statements
```

When the expression evaluates to `True` (truthiness) the loop will execute the set of statements till it reaches the end of the indent block. It will execute the loop again until the expression evaluates to `False`.

```python
i = 0
while i < 3:
    print(i)
# => 0
# => 1
# => 2
```

## For Loops

While loops are based on `Iterational` statement. The Loop will iterate over a `iterable` object.

```
for item in iterable_object:
    set_of_statements
```

```python
list_of_items = [1, 2, 3]
for item in list_of_items:
    print(item)
# => 1
# => 2
# => 3
```

## Breaking from loops

Where you have a large set of objects that you want to loop through and you dont want to go through all the objects in the loop but rather go through a certain number of desired objects and then stop the execution, then `break` comes to the rescue.

When you want to break from an iterable loop on any condition, you can use the `break` statement

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

You will have important objects as well as non important ones. When you want to skip over the objects that you dont need to process you use the continue statement.

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

## Else in Loops

An `else` clause in a loop will get executed when there is no `break` that happebed while you were processing your loop.
This gets useful if you want to go over fail over scenarios.

```python
x = None
for i in list_of_items:
    if i > 10:
        x = i
        break
else:
    x = 10
```

What the above code does is it sets the variable x to 10 if the loop inside was not able to find an item that is more than 10.
