def generator():
    t=1
    print("First Result",t)
    yield t

    t+=1
    print("Second Result", t)
    yield t

    t+=1
    print("Third Result is :",t)
    yield t

call=generator()
print(next(call))
print(next(call))
print(next(call))