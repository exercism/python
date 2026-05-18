# List manipulation

The direct approach would be to manipulate and check the given lists to solve this.
This solution uses a helper function, which simplifies things, but the approach can be implemented without it.

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_sub_sequences(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)
    return any(list_b[i : i + len_a] == list_a for i in range(len_b - len_a + 1))

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequences(list_one, list_two):
        return SUBLIST
    if check_sub_sequences(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
```

~~~~exercism/note
You might wonder why the lists in the helper function are named `list_a` and `list_b` instead of `list_one` and `list_two`.
This is because if the parameters have the same name, Pylint thinks the parameters are being passed in incorrectly when we call `check_sub_sequences(list_two, list_one)`.
(The exact warning generated is [`W1114 arguments-out-of-order`][w1114].)

[w1114]: https://pylint.readthedocs.io/en/stable/user_guide/messages/warning/arguments-out-of-order.html
~~~~

In this approach, we first check for equality using the `==` operator, and if the lists are equal, then we return `EQUAL`.
After that, we call `check_sub_sequences()`, passing in `list_one` and `list_two` for the parameters `list_a` and `list_b`.

In the helper function, we check if `any` of the possible sub-sequences in `list_b` of length `len_a` (the length of `list_a`) are equal to `list_a`.
If so, then we conclude that `list_a` is a `SUBLIST` of `list_b`.

To find whether `list_one` is a `SUPERLIST` of `list_two`, we just reverse this process — pass in the lists in the opposite order.
Thus, we check if `any` of the possible sub-sequences in `list_one` of the length of `list_two` are equal to `list_two`.

If none of the above conditions are true, we conclude that the two lists are `UNEQUAL`.
