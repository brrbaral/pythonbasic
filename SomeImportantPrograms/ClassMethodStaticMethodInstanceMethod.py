class Myclass:
    def method(self):
        print("This is instance method",self)

    @classmethod
    def classMethod(cls):
        print("class Method called",cls)

    @staticmethod
    def staticMethod():
        print("this is static method")

Myclass.classMethod()
Myclass.staticMethod()
obj1=Myclass()
obj1.method()