from collections import defaultdict


class School:
    def __init__(self):
        self.db = {}
        self.add = []

    def added(self):
        result = self.add[:]
        self.add = []
        return result

    def add_student(self, name, grade):

        if not self.db.get(name, 0):
            self.db[name] = grade
            self.add.append(True)
        else:
            self.add.append(False)


    def roster(self, grade=0):
        grades_roster = defaultdict(list)

        for key, value in self.db.items():
            grades_roster[value].append(key)

        if grade:
            return sorted(grades_roster[grade])
        else:
            working_list = (sorted(grades_roster[key]) for key in sorted(grades_roster.keys()))
            return [element for item in working_list for element in item]

    def grade(self, grade_number):
        return sorted(self.roster(grade_number))
