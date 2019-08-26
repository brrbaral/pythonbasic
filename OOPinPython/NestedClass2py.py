class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno


    def show(self):
        print(self.name,self.rollno)


    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('Aakash',20)
s1.show()
l1=Student.Laptop()
l1.show()