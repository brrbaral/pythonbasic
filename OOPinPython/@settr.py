class Employee:
    def __init__(self, first, last):
        self.first=first
        self.last=last

    @property
    def fullName(self):
        return '{1} {0}'.format(self.first,self.last)

    @fullName.setter
    def fullName(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

emp1=Employee('anil','Bhandari')
emp1.fullName="Shree Raj" #THIS IS NOT ALLOWED SO HERE COMES @setter
print(emp1.first)
print(emp1.last)
print(emp1.fullName)
