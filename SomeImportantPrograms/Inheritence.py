class Parent:
    parentAttr=100
    def __init__(self):
        print("calling parents contructors")
    def parentMethod(self):
        print("calling parent method")
    #def setAttr(self,attr):
     #   Parent.parentAttr=attr
    def getAttr(self):
        print("Parent Attribute=",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("calling child consructor")
    def childMethod(self):
        print("calling child method")

c=Child()
c.childMethod()
c.parentMethod()
#c.setAttr(200)
c.getAttr()
print(issubclass(Child,Parent))
print(isinstance(c,Child))