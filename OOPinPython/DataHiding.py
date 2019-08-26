#AN OBJECT ATTRIBUTES MAY OR MAY NOE BE VISIBLE TO OUTSIDE
class JustCounter:
    __secretCount=0

    def Count(self):
        self.__secretCount+=1
        print(self.__secretCount)

c1=JustCounter()
c1.Count()
c1.Count()

#THIS WILL NOT GIVE THE OUTPUT
#print(c1.__secretCount)

#THIS WILL GIVE THE OUTPUT
print(c1._JustCounter__secretCount)
