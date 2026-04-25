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

