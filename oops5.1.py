# Static methods

from datetime import datetime


class Student:

    numberOfStudent = 0
    coursePrice = 0

    def __init__(self, name, age, course, price):

        self.name = name
        self.age = age
        self.course = course
        Student.numberOfStudent += 1
        self.rollNo = Student.numberOfStudent
        Student.coursePrice = price

    def displayStudentInfo(self):
        print("Roll Number", self.rollNo)
        print("Student Name", self.name)
        print("Age", self.age)
        print("Course", self.course)
        print("---------------")

    @classmethod
    def discountedCoursePrice(cls, discount):
        print(discount)
        cls.coursePrice = cls.coursePrice - ((cls.coursePrice * discount) / 100)


    @staticmethod
    def isvalidStudent(doj):

        doj = datetime.strptime(doj, "%d/%m/%Y")
        present = datetime.now()

        if (present - doj).days > 365:
            return False
        return True


stud1 = Student('Stud1', 25, 'PYTHON', 15000)
stud2 = Student('Stud2', 26, 'PYTHON', 15000)
stud1.displayStudentInfo()
stud2.displayStudentInfo()
print(Student.isvalidStudent("28/07/2018"))