import random
print(random.random())
print(random.randrange(0,11,5))

random.seed(7)
print(random.randrange(0,10))
print("##############")

li=[1,2,3,4,5,6,7,8,9]
print(li)
random.shuffle(li)
print(li)