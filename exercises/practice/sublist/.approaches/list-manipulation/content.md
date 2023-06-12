# List manipulation
The direct approach would be to manipulate and check the given lists to solve this.
This solution uses a helper function, which simplifies things, but the approach can be implemented without it.

```python
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def check_sub_sequences(list_one, list_two):
    n1 = len(list_one)
    n2 = len(list_two)
    return any(list_two[i:i+n1] == list_one for i in range(n2 - n1 + 1))
    
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if check_sub_sequences(list_one, list_two):
        return SUBLIST
    if check_sub_sequences(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
```

We first check for equality using the `==` operator, if so, then we return `EQUAL`. 
A common way to do this differently would be to return `1` directly, but this is better practice as we  [remove magic values][magic values].

After that we call `check_sub_sequences` passing in `list_one` and `list_two`.
In the helper function, we check if `any` of the possible sub-sequences in `list_two` of length `n1` (the length of the first list) are equal to the first list.
If so, then we conclude that `list_one` is a `SUBLIST` of `list_two`. 

To find whether `list_one` is a `SUPERLIST` of `list_two`, we just reverse this process - pass in the lists in the opposite order.
Thus, we check if `any` of the possible sub-sequences in `list_one` of length `n2` (the length of the second list) are equal to the second list.

If none of the above conditions are true, we conclude that the two lists are unequal.

[magic values]: https://stackoverflow.com/questions/47882/what-is-a-magic-number-and-why-is-it-bad