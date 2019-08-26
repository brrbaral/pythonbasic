def check(func):#HERE WE ARE PASSING FUNC TO CHECK WHICH IS ALSO A FUNCTION
    def inside(a,b):
        if b==0:
            print("cannot divide by 0")
        
        func(a,b)
    return inside

def div(a,b):
    return a/b

div1=check(div)
print(div1(10,0))

