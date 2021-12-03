class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedIterator:
    def __init__(self, linked_list):
        self.current = linked_list._head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value()
        self.current = self.current.next()
        return value

    def next(self):
        return self.__next__()


class LinkedList:
    def __init__(self, values=None):
        values = values if values is not None else []
        self._head = None
        self._len = 0
        for value in values:
            self.push(value)

    def __iter__(self):
        return LinkedIterator(self)

    def __len__(self):
        return self._len

    def head(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')
        return self._head

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException('The list is empty.')
        self._len -= 1
        ret = self._head.value()
        self._head = self._head.next()
        return ret

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message
