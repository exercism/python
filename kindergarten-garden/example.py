class Garden(object):

    __plant_names = {"C": "Clover", "G": "Grass",
                     "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram,
                 students=("Alice Bob Charlie David "
                           "Eve Fred Ginny Harriet "
                           "Ileana Joseph Kincaid Larry").split()):
        self.plant_rows = diagram.split()
        self.students = sorted(students)

    def plants(self, student):
        slot_start = self.students.index(student) * 2
        slot = slice(slot_start, slot_start + 2)
        return [self.__plant_names[abbrev]
                for abbrev in (self.plant_rows[0][slot] +
                               self.plant_rows[1][slot])]
