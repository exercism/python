# Hints

## General

- This challenge is about creating a [_stack_][Baeldung: The Stack Data Structure] using a [singly linked list][singly linked list].
- Unlike stacks underpinned with `lists`, `collections.deque`, or `queue.LifoQueue`, we ask you create custom `Node` and `LinkedList` [`classes`][classes tutorial] to store and link elements.

![Diagram representing a stack implemented with a linked list. A circle with a dashed border named New_Node is to the far left-hand side, with two dotted arrow lines pointing right-ward.  New_Node reads "(becomes head) - New_Node - next = node_6". The top dotted arrow line is labeled "push" and points to Node_6, above and to the right.  Node_6 reads "(current) head - Node_6 - next = node_5". The bottom dotted arrow line is labeled "pop" and points to a box that reads "gets removed on pop()". Node_6 has a solid arrow that points rightward to Node_5, which reads "Node_5 - next = node_4". Node_5 has a solid arrow pointing rightward to Node_4, which reads "Node_4 - next = node_3". This pattern continues until Node_1, which reads "(current) tail - Node_1 - next = None". Node_1 has a dotted arrow pointing rightward to a node that says "None".](https://assets.exercism.org/images/tracks/python/simple-linked-list/linked-list.svg)

- [Real Python: Linked Lists][Real Python Linked Lists], [Towards Data Science: Demystifying the Linked List][towards data science demystifying the linked list], and [ADS Stack in Python][Koder Dojo Coding an ADS Stack in Python] can be helpful to review for details on implementation.
- Your `LinkedList` should accept a `list` argument to its _constructor_, but should not use a `list` to store nodes or elements.
- `len()` is a built-in function for most Python objects.
In order for _custom objects_ to support `len()`, the special method [`__len__`][__len__] needs to be defined.
- Iteration in Python is supported for most sequence, container, or collection type objects.
In order for a _custom_ object to support looping or re-ordering, the special method `__iter__` needs to be defined.
[Implementing an iterator for a class][implementing iterators] can help show you how.

[Baeldung: The Stack Data Structure]: https://www.baeldung.com/cs/stack-data-structure
[Koder Dojo Coding an ADS Stack in Python]: https://www.koderdojo.com/blog/coding-a-stack-abstract-data-structure-using-linked-list-in-python
[Real Python Linked Lists]: https://realpython.com/linked-lists-python/
[__len__]: https://docs.python.org/3/reference/datamodel.html#object.__len__]
[classes tutorial]: https://docs.python.org/3/tutorial/classes.html#tut-classes
[implementing iterators]: https://docs.python.org/3/tutorial/classes.html#iterators
[singly linked list]: https://towardsdatascience.com/python-linked-lists-c3622205da81
[towards data science demystifying the linked list]: https://towardsdatascience.com/demystifying-linked-list-258dfb9f2176
