class Enemy:
    life=3;

    def attack(self):
        self.life-=1

    def checkLife(self):
        if self.life<0:
            print("you are deade")
        else:
            print(str(self.life)+"life left")
enemy1=Enemy()
enemy2=Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()



