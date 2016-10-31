<<<<<<< e2f6b831658936e2dcb9623291bc9f56bf5449d6
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def empty(self):
        return self.size == 0

    def peek(self):
        pass
        if self.empty:
            return None
||||||| merged common ancestors
=======
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.peek = head
        self.size = 0

    def push(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Element(new_element)
            self.peek = current.next
        else:
            self.head = Element(new_element)
            self.peek = self.head
        self.size += 1

    def pop(self):
        if self.empty():
            return None
        else:
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            if prev:
                e, prev.next = current.value, None
            else:
                e, prev = current.value, None
            self.peek = prev
            self.size -= 1
            return e

    def empty(self):
        return self.size == 0

    def get_peek(self):
        if self.empty():
            return None
        else:
<<<<<<< 9ca4ff25cf0edc3e68b8b5d4cfca60b0fd88499d
            #iterate
    end
>>>>>>> Adding data structures pop peak empty methods and test class
||||||| merged common ancestors
            #iterate
    end
=======
            return self.peek.value

    def reverse(self):
        new_list = LinkedList()
        while self.size > 0:
            new_list.push(self.pop())
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
>>>>>>> including test cases for simple-linked-list
