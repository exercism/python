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
        if empty:
            return None
        else:
            #iterate
    end
>>>>>>> Adding data structures pop peak empty methods and test class
