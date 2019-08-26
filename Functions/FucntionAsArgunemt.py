def hello():
    return "Hi Bishow"

def other(func):
    print("Hello")
    print(func())

other(hello)