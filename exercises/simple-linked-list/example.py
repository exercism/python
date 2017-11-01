class Node(object):
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList(object):
    def __init__(self, values=[]):
        self._head = None
        self._len = 0
        [self.add(v) for v in values]

    def __len__(self):
        return self._len

    def head(self):
        if self._head is None:
            raise EmptyListException()
        return self._head

    def add(self, value):
        newNode = Node(value)
        if self._head is None:
            self._head = newNode
        else:
            current = self._head
            while current.next() is not None:
                current = current.next()
            current._next = newNode
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException()
        self._len -= 1
        ret = self._head.value()
        self._head = self._head.next()
        return ret


class EmptyListException(Exception):
    pass
