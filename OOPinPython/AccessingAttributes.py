class Employee:
    employeeCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.employeeCount+=1

    def displayCount(self):
        print("no. of Employee:",Employee.employeeCount)

    def displayEmployee(self):
        print("Name:",self.name,"salary->",self.salary)

emp1=Employee("zara", 10000)
emp2=Employee("Maahi",15000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total no. of emp:",str(Employee.employeeCount))

#SETTING ATTRIBUTE
emp1.age=10
setattr(emp1,'age',8)
print(hasattr(emp1, 'age'))
print(getattr(emp1,'age'))

#BUILT IN ATTRIBUTES
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)