def outer():
    x=3
    
    def inner():
        y=4
        result=x+y
        return result
    print(inner())

outer()
print(outer)
print(outer())