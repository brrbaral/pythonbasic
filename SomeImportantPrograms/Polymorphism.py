class Shark():
    def swim(self):
        print("shark is swimming")
    def backward_swimming(self):
        print("shark cannot swim backward")
    def skeleton(self):
        print("shark skeleton is made up of cartilage")

class Clownfish():
    def swim(self):
        print("clown fish is swimming")
    def backward_swimming(self):
        print("clown fish can swim backward")
    def skeleton(self):
        print("clownfish skeleton is made up of bone")

sh1=Shark()
'''
sh1.swim()
sh1.backward_swimming()
sh1.skeleton()
'''
cl1=Clownfish()
'''cl1.swim()
cl1.backward_swimming()
cl1.skeleton()
'''
for fish in (sh1,cl1):
    fish.swim()
    fish.backward_swimming()
    fish.skeleton()