class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __lt__(self, other):
        first=self.x+self.y
        second=other.x+other.y
        return first<second

print(Point(2,1)<Point(1,1))