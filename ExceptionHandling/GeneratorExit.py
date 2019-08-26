def my_generator():
    try:
        for i in range(5):
            print('yeilding',i)
            yield i

    except GeneratorExit:
        print('exiting eraly')
g=my_generator()
print( g.next())
g.close()