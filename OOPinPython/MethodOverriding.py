class Parent:
    def MyMethod(self):
        print("calling parent myMethod")

class Child(Parent):
    def MyMethod(self):
        print("Calling Child method")

c1=Child()
c1.MyMethod()

#NEED TO CALL EXPLICITLY PARENT METHOD ALSO

p1=Parent()
p1.MyMethod()