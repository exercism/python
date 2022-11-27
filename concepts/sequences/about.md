## Reverse a sequence

Using slicing with steps allows reversing a sequence.
That is because we can use a negative step to start at the end of the sequence and move backwards.
This is a very common operation.

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[::-1]
[5, 4, 3, 2, 1]

>>> name = "Delizald"
>>> name[::-1]
'dlazileD'
```
