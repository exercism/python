# Introduction

In Python, `None` is frequently used to represent the absence of a value -- a placeholder to define a `null` (empty) variable, object, or argument.

If you've heard about or used a `NULL` or `nil` type in another programming language, then this usage of `None` in Python will be familiar to you. `None` helps you to declare variables or function arguments that you don't yet have values for. These can then be re-assigned to specific values later as needed.

```python
a = None
print(a)
#=> None
type(a)
#=> <class 'NoneType'>

# Adding a Default Argument with `None`
def add_to_todos(new_task, todo_list=None):
  if todo_list is None:
    todo_list = []
    todo_list.append(new_task)
  return todo_list

```

`None` will evaluate to `False` when used in a conditional check, so it is useful for validating the "presence of" or "absence of" a value - _any_ value -- a pattern frequently used when a function or process might hand back an error object or message.

```python
a = None
if a: #=> a will be evaluated to False when its used in a conditional check.
    print("This will not be printed")
```
