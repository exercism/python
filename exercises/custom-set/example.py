class CustomSet(object):
    def __init__(self):
        self.contents = [[] for index in range(100)]
        self.size = 100
        self.number_of_elements = 0
    def addSingle(self, obj):
        self.contents[hash(obj) % self.size].append(obj)
        self.number_of_elements += 1
    def add(self, obj):
        #if the number of elements is more than 2/3 of the total size
        #expand the set
        if not self.contains(obj):
            if self.number_of_elements >= 0.66 * self.size:
                self.size *= 2
                new_contents = [[] for index in range(self.size)]
                for element in self.contents:
                    new_index = hash(element) % self.size
                    new_contents[hash(element)].append(element)
                self.contents = new_contents
                self.addSingle(obj)
            else:
                self.addSingle(obj)
    def empty(self):
        return self.number_of_elements == 0
    def contains(self, obj):
        bucket = self.contents[hash(obj) % self.size]
        for element in bucket:
            if element == obj:
                return True
        return False
