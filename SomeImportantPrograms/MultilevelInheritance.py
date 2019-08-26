class Student:
    def getStudent(self):
        self.name=input("enter name:")
        self.age=input("enter age:")
        self.gender=input("enter gender:")

class Test(Student):
    def getMarks(self):
        self.grade=input("enter your class:")
        print("Enter the marks of the respective subjects")
        self.literature=int(input("literature:"))
        self.maths=int(input("maths:"))
        self.physics=int(input("physics:"))

class Marks(Test):
    def display(self):
        print("\n\nName:",self.name)
        print("age:",self.age)
        print("Gender:",self.gender)
        print("study in:class-",self.grade)
        print("Total marks=",self.literature+self.maths+self.physics)

m1=Marks()
m1.getStudent()
m1.getMarks()
m1.display()