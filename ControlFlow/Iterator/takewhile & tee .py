import itertools
list1=[2,4,6,7,8,10,20]
iti=iter(list1)

#USING THE TAKEWHILE()
print(list(itertools.takewhile(lambda x: x%2==0,list1)))

it=itertools.tee(iti,3)
for i in range(0,3):
    print(list(it[i]))
