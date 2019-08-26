class Super1():
    def __init__(self):
        print("this is first class")

class Super2():
    def __init__(self):
        print("this is superclass 2")

class base(Super1,Super2):
    def __init__(self):
        super().__init__()
        print("this is third class")
b1=base()