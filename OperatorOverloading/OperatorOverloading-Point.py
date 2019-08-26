
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({},{})".format(self.x,self.y)

    #HERE IF {1}{0} THEN GIVES (Y,X) IF {}{} THEN ALSO GIVES (X,Y)



p1=Point(1,2)
p2=Point(3,4)
p3=Point(5,6)
p4=Point(7,8)
print(p1)
print(p2)
print(p3)
print(p4)