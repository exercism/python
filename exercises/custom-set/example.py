class CustomSet(object):
    def __init__(self, *numbers):
        self.size = 0
        self.capacity = 100
        num_buckets = int(self.capacity / 10)
        self.data = [[] for x in range(num_buckets)]
        for number in numbers:
            self.add(number)                                                                                                                                                                                                                                                                                                                                                                              

    def empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

    def expand(self):
        new_capacity = self.capacity * 2
        num_buckets = int(new_capacity / 10)
        new_data = [[] for x in range(num_buckets)]
        for bucket in self.data:
            for element in bucket:
                new_index = hash(element) % num_buckets
                new_data[new_index].append(element)
        self.data = new_data
        self.capacity = new_capacity

    def add(self, n):
        if n in self:
            return

        if self.size > (2/3) * self.capacity:
            self.expand()
        index = hash(n) % len(self.data)
        self.data[index].append(n)
        self.size += 1
        
    def __contains__(self, n):
        return n in self.data[hash(n) % len(self.data)]

    def subset(self, other):
        for bucket in other.data:
            for element in bucket:
                if element not in self:
                    return False
        return True

    def disjoint(self, other):
        disj = CustomSet()
        for bucket in other.data:
            for element in bucket:
                if element in self:
                    return False
        return True

    #this def follows from the mathematical definition of equality for sets as
    #two sets are equal when both sets of subsets of each other
    def __eq__(self, other):
        return self.subset(other) and other.subset(self)

    def intersection(self, other):
        inter = CustomSet()
        for bucket in other.data:
            for element in bucket:
                if element in self:
                    inter.add(element)
        return inter

    def __sub__(self, other):
        result = CustomSet()
        for bucket in self.data:
            for element in bucket:
                if element not in other:
                    result.add(element)
        return result

    def __add__(self, other):
        result = CustomSet()
        for bucket in self.data:
            for element in bucket:
                result.add(element)
        
        for bucket in other.data:
            for element in bucket:
                result.add(element)
        
        return result

    def __iter__(self):
        result = []
        for bucket in self.data:
            for element in bucket:
                result.append(element)
        return iter(result)