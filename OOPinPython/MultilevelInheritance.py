class Student:
    def getStudentData(self):
        self.name=input("Enter name:\n")
        self.age=input("Enter age:\n")
        self.gender=input("Enter gender:\n")

class Test(Student):
    def getMarks(self):
        self.Class=input("Enter Class:")
        print("Enter the marks of the sutends:")
        self.physics=int(input("physics:"))
        self.mathts= int(input("maths:"))
        self.biology = int(input("Biology:"))

class Marks(Test):
    def display(self):
        print("\n Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Study in class:",self.Class)
        print("Total marks:",self.mathts+self.biology+self.physics)

m=Marks()
m.getStudentData()
m.getMarks()
m.display()