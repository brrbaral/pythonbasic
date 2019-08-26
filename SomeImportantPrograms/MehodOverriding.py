class Parent:
    def myMethod(self):
        print("calling parents method")
    def __del__(self):
        print()
class Child(Parent):
    def myMethod(self):
        print("child method is called")

c1=Child()
c1.myMethod()
p1=Parent()
p1.myMethod()
