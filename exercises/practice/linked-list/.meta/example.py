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

    def __len__(self):
        return self.length

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield (current_node.value, current_node.succeeding, current_node.prev)
            current_node = current_node.succeeding

    def delete(self, to_delete):
        if self.length == 0:
            raise ValueError("Value not found")
        found = False
        node = self.head

        for value, succeeding, prev in self:
            if value == to_delete:
                if prev:
                    node.prev.succeeding = succeeding
                else:
                    self.head = succeeding
                if succeeding:
                    node.succeeding.prev = prev
                else:
                    self.tail = prev

                found = True
                self.length -= 1
                break
            node = node.succeeding
        if not found:
            raise ValueError("Value not found")

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

        if self.length == 0:
            raise IndexError("List is empty")
        if node is None or node.prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.succeeding = None
        self.length -= 1

        return node.value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
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
