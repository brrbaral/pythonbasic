import operator
a=[2,3,4,5,6]
b=operator.add(a,[1,8,9])
print(b)
print(a)
c=operator.iadd(a,[1,8,9])
print(c)
print(a)