my_list=[1,2,3,4,5]
#GET IN ITERATOR USING ITER()
my_iter=iter(my_list)

print("______________________")
try:
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
except StopIteration as e:
    print(e)
