class Outer:
    def __init__(self):
        print("this is outer class")

    class Inner:
        def __init__(self):
            print("this is inner class")

c1=Outer()
c2=Outer.Inner()