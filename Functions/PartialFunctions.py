from functools import partial
def fun1(a,b,c,x):
    return a+b+c+x

fun2=partial(fun1,10,20,30)
print(fun2(40))