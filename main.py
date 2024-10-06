class Student:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students(self):
        if self.students:
            print("все ученики")
            for student in self.students:
                print(student.name)
        else:
            print("школа пустая")

schol = School()

for _ in range(3):
    student_name = input("Имя учня ")
    student = Student(student_name)
    schol.add_student(student)

schol.print_students()
