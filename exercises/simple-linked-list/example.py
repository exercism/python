class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def push(self, new_element):
        new_e = Element(new_element)

        if self.empty():
            self.head = new_e
        else:
            new_e.next = self.head
            self.head = new_e
        self.size += 1

    def pop(self):
        if self.empty():
            return None
        else:
            e = self.head
            self.head = self.head.next
            self.size -= 1
            return e.value

    def empty(self):
        return self.size == 0

    def get_peek(self):
        if self.empty():
            return None
        else:
            return self.head.value

    def reverse(self):
        new_list = LinkedList()
        if self.size > 0:
            current = self.head
            while current.next:
                new_list.push(current.value)
                current = current.next
            new_list.push(current.value)
        return new_list

    def to_array(self):
        arr = []
        if self.empty():
            return []
        current = self.head
        while current.next:
            arr.append(current.value)
            current = current.next
        arr.append(current.value)
        return arr

    def from_array(self, arr=[]):
        if len(arr) == 0:
            return self
        else:
            for i in arr:
                self.push(i)
        return self
