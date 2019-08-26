class Enemy:
    def __init__(self,x):
        self.energy=x

    def get_energy(self):
        print(self.energy)

e1=Enemy(5)
e2=Enemy(50)
e1.get_energy()