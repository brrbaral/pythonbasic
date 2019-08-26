import itertools
list1=[1,2,3,4,5,6]
list2=[(1,2,3),(4,5,6),(7,8,9)]

print(list(itertools.islice(list1,1,6,2)))

print(list(itertools.starmap(min,list2)))


