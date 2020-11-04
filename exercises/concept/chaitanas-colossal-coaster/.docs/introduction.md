## list-methods

Python allows you to manipulate `list` in a lot of ways. A `list` is simple a collection of objects. They are mutable, ordered and indexed. Let's look at the methods that are available to manipulate a `list` object.

When you manipulate a list with a list-method, you are changing the properties of the list you pass. That is, **you will alter the list** object that is being used with the list-method. If you do not want to change the original list, you need to copy the list and then work on the copied list.

To begin, you first need a `list` object to use the functions.

```python
ex_list = list() # (or)  ex_list = []
print(ex_list)
#=> []
```

## Add an Item to the List

Topics to discuss:

1. `append`
2. `insert`
3. `extend`

If you want to add an item to an existing list, you use the list-method `append()` for it. As the name represent, it appends the item to the **end** of the list.

```python
ex_list = [1, 2, 3]
ex_list.append(9)
print(ex_list)
#=> [1, 2, 3, 9]
```

There is another way to add an item to the list. `insert()` method also gives you the ability to add the item to a particular index in the list.

`insert` takes 2 parameters.

1. index at which you want to add the item
2. item

Note: if the index is 0, the item will be added to the first of the list. if the index is more than or equal to the length of the list, then item will be added to the last of the list (like the append function)

```python
ex_list = [1, 2, 3]
ex_list.insert(0, -2)
print(ex_list)
#=> [-2, 1, 2, 3]
ex_list.insert(1, 0)
print(ex_list)
#=> [-2, 0, 1, 2, 3]
```

If you have another list object who's content you need to be copied to your list, then you can use the `extend` function.
The extend function takes an iterable as its parameter.

```python
ex_list = [1, 2, 3]
extend_list = [5, 6, 7]

ex_list.extend(extend_list)
print(ex_list)
#=> [1, 2, 3, 5, 6, 7]

ex_list.extend([8, 9])
print(ex_list)
#=> [1, 2, 3, 5, 6, 7, 8, 9]
```

# Removing Items from the list

Topics to discuss:

1. `remove`
2. `pop`
3. `clear`

If you want to remove an item from a list, you can use the `remove` function which takes one parameter. Feed the function with the item you want to remove from the list. the `remove` function will throw a `ValueError` if the item does not exist in the loop.

```python
ex_list = [1, 2, 3]
ex_list.remove(2)
print(ex_list)
#=> [1, 3]
ex_list.remove(0)
#=> ValueError: list.remove(x): x not in list
```

There is another way to remove an item from the list. If you know the index of the item which you want to remove, you can use `pop` function. Pop takes 1 parameter, the index of the item you need to remove, and return it to you. If you specify an index more than the length of the list, you will get an `IndexError`. If you dont specify an index, the function will remove the last element and return it to you.

```python
ex_list = [1, 2, 3]
ex_list.pop(0)
#=> 1
print(ex_list)
#=> [2, 3]
ex_list.pop()
#=> [2]
```

If you want to clear the list (ie: all the items in the list), then you can use the `clear` function. It does not take any parameter as input but will remove all the elements in the list.

```python
ex_list = [1, 2, 3]
ex_list.clear()
print(ex_list)
#=> []
```

## Reverse the list

The items in the list can be reordered in the reverse order with the `reverse` function.

```python
ex_list = [1, 2, 3]
ex_list.reverse()
print(ex_list)
#=> [3, 2, 1]
```

## Sort the list

When you have an random ordered list of items, you can sort them with the help of `sort` function. If you have items that are alphanumerical, you dont have to provide any inputs to sort.

ex: you have list of numbers, or you have a list of names and you want to sort them

```python
ex_list = ["Tony", "Natasha", "Thor", "Bruce"]
ex_list.sort()
print(ex_list)
#=> ["Bruce", "Natasha", "Thor", "Tony"]
```

If you want the sort to be in descending order, you can use the reverse parameter.

```python
ex_list = ["Tony", "Natasha", "Thor", "Bruce"]
ex_list.sort(reverse=True)
print(ex_list)
#=> ["Tony", "Thor", "Natasha", "Bruce"]
```

If you have a list of items that are complex, you can use the key parameter in the sort. Lets see more about this later.

Internally, python uses `Timsort` to sort the list.

## Occurances of an item in the list.

You can find the occurances of an element in the list with the help of the `count` function. It takes one parameter which will be the item, for which you need to find the number of occurances.

```python
ex_list = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
ex_list.count(1)
#=> 3
```

## Find the Index of the Item.

If you want to find the index of an item you want in the list, you can use the `index` function. If you have multiple occurances of the same item, it will provide you the index of the first occurance. If you do not have any occurances of the item, then you will have a `ValueError` raised.

Index starts with 0.

```python
ex_list = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
ex_list.index(4)
#=> 1
ex_list.index(10)
#=>ValueError: 10 is not in list
```

You can also provide a start (and an end) to the index from where you need the search has to happen for the item.

```python
ex_list = [1, 4, 7, 8, 2, 9, 2, 1, 1, 0, 4, 3]
ex_list.index(4, 2, 12)
#=> 10
```

## Copy a List.

Lists are a collection of items which are referenced to an index, Hence if you do an assignment of a list object to another variable. Any change you make to the assigned variable will also have an impact on the original variable.

```python
ex_list = ["Tony", "Natasha", "Thor", "Bruce"]
new_list = ex_list
new_list.append("Clarke")
print(new_list)
#=> ["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
print(ex_list)
#=> ["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
```

You need to use the `copy` function in order to do a `shallow_copy` of the list. ( More about `shallow_copy` and `deep_copy` later.)

```python
ex_list = ["Tony", "Natasha", "Thor", "Bruce"]
new_list = ex_list.copy()
new_list.append("Clarke")
print(new_list)
#=> ["Tony", "Natasha", "Thor", "Bruce", "Clarke"]
print(ex_list)
#=> ["Tony", "Natasha", "Thor", "Bruce"]
```
