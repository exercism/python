class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        node = self.tail
        if node is None or node.prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.succeeding = None
        self.length -= 1
        return node.value

    def shift(self):
        node = self.head
        if node is None or node.succeeding is None:
            self.head = self.tail = None
        else:
            self.head = self.head.succeeding
            self.head.prev = None
        self.length -= 1
        return node.value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.succeeding
