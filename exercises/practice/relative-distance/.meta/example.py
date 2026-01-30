import collections
import itertools

class RelativeDistance:
    def __init__(self, family_tree):
        self.neighbors = collections.defaultdict(set)
        for parent, children in family_tree.items():
            for child in children:
                self.neighbors[parent].add(child)
                self.neighbors[child].add(parent)
            
            for child1, child2 in itertools.combinations(children, 2):
                self.neighbors[child1].add(child2)
                self.neighbors[child2].add(child1)

    def degree_of_separation(self, person_a, person_b):
        if person_a not in self.neighbors:
            raise ValueError("Person A not in family tree.")
        if person_b not in self.neighbors:
            raise ValueError("Person B not in family tree.")

        queue = collections.deque([(person_a, 0)])
        visited = {person_a}

        while queue:
            current, degree = queue.popleft()

            if current == person_b:
                return degree

            for neighbor in self.neighbors.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, degree + 1))
        
        raise ValueError("No connection between person A and person B.")
