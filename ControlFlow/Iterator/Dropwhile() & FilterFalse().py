import itertools
import operator

list1=[2,4,5,6,7,8,9,10,11,12,13,14]

print(list(itertools.dropwhile(lambda x: x%2==0, list1)))
print(list(itertools.filterfalse(lambda x: x%2==0, list1)))
