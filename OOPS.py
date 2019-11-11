'''class Students:

    def __init__(self):
        print('inside')
        self.name = 'rohit'
        self.age = 25
        self.course = 'python'


print('before')
obj1 = Students()
print('after')
print(obj1.name)
print(obj1.age)
print(obj1.course)
print(dir(obj1))
obj2 = Students()'''


'''class Students:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
        
obj1 = Students('vivek', 21, 'python')
obj2 = Students('ranvijay', 23, 'python')
print(obj1.name)
print(obj2.name)'''


'''class Students:

    studentcount=0
    def __init__(self, name, age, course,rollno):
        self.name = name
        self.age = age
        self.course = course
        self.rollno = rollno
        Students.studentcount += rollno
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.course)
        print(self.rollno)

print(Students.studentcount)
obj1 = Students('vivek', 21, 'python', 1)
obj1.print_info()
print(Students.studentcount)
obj2 = Students('shubham', 22, 'python', 1)
obj2.print_info()
print(Students.studentcount)'''


class Student:
    fee = 10000
    noofstd = 0

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

    @classmethod
    def discount(cls, dis):
        return cls.fee-(cls.fee*dis)/100


obj1=Student('vivek')
obj1.print_info()
print(Student.discount(10))

