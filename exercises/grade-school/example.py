from collections import defaultdict


class School:
    def __init__(self,):
        self.db = defaultdict(set)

    def add_student(self, name, grade):
        self.db[grade].add(name)

    def roster(self):
        return [
            name
            for grade, names in sorted(self.db.items())
            for name in sorted(names)
        ]

    def grade(self, grade_number):
        return sorted(self.db[grade_number])
