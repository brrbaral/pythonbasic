class Parent:
    parentAttr=100
    def __init__(self):
        print("calling parent constructor")

    def ParentMethod(self):
        print("calling parent method")

    def setAttr(self,attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print("parent Attribure is:",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("calling child constructor")

    def childMethod(self):
        print("calling child method")

C=Child()
C.childMethod()
C.setAttr(150)
C.getAttr()
P=Parent()
P.setAttr(500)
P.getAttr()
print(issubclass(Child,Parent))
print(isinstance(C,Child))
print(isinstance(P,Child))
