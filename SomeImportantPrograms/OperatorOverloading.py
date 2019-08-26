class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self, other):
        self.x=self.x+other.x
        self.y=self.y+other.y
        return Point(self.x,self.y)

p1=Point(1,2)
p2=Point(3,4)
print(p1)
print(p2)
p3=p1+p2
print(p3)
