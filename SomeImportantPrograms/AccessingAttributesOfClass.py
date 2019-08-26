class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("The number of employee:", Employee.empCount)

    def displayEmployee(self):
        print("name:"+self.name,"salary:",self.salary)

emp1=Employee("Jolly",35000)
emp2=Employee("Abhiyan",10000)
emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()
#print("the total no of employee is :",str(Employee.empCount))

#Built in attributes of class
print("Employee doc:",Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)