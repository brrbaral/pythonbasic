class Employee:
    def __init__(self, first, last):
        self.fname=first
        self.lname=last

    def email(self):
        return (self.fname +'.'+ self.lname +'@email.com')

    def fullName(self):
        return '{1} {0}'.format(self.fname,self.lname)

emp1=Employee('anil','Bhandari')

emp1.fname="shree"
print(emp1.fname)
print(emp1.email())
print(emp1.fullName())
