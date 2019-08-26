class Employee:
    def __init__(self, first, last):
        self.fname=first
        self.lname=last
        self.email=self.fname+ '.'+self.lname+'@email.com'

    def fullName(self):
        return '{}{}'.format(self.fname,self.lname)

emp1=Employee('anil','Bhandari')
print(emp1.fname)
print(emp1.email)
print(emp1.fullName())
