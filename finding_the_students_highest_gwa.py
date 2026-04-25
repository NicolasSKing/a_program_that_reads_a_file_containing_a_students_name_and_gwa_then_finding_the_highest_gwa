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

    def find_highest_gwa(self):
        highest_student = self.students[0]

        for student in self.students:
            if student.gwa > highest_student.gwa:
                highest_student = student

        return highest_student

    def run(self):
        print("Reading data from file:", self.filename)

        self.load_students()

        highest = self.find_highest_gwa()

        print("\nStudent with the highest GWA:")
        print("Name:", highest.name)
        print("GWA:", highest.gwa)
        



