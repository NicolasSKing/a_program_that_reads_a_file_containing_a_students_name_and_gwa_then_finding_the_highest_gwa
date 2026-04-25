class Students:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = gwa

class StudentProgram:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_students(self):
        file = open(self.filename, "r")

        for line in file:
            name, gwa = line.split()
            student = Students(name, float(gwa))
            self.students.append(student)

        file.close()

