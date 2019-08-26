class A:
    def __init__(self):
        print("This is first class")

class B:
    def __init__(self):
        print("this is second class")

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("This is third class accessing first and second")
c1=C()
