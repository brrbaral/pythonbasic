class Employee:
    def __init__(self, first, last):
        self.fname=first
        self.lname=last



    @property
    def fullName(self):
        return '{1} {0}'.format(self.fname,self.lname)

emp1=Employee('anil','Bhandari')
emp1.fullName="Shree Raj" #THIS IS NOT ALLOWED SO HERE COMES @setter
