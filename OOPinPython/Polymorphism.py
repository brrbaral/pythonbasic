class Nepal:
    def Capital(self):
        print("the capital of nepal is Kathmandu")
    def language(self):
        print("Nepali is the official language of Nepal")

    def Type(self):
        print("Nepal is underdeveloped country")

class India:
    def Capital(self):
        print("the capital of nepal is New Delhi")
    def language(self):
        print("Hindi is the official language of India")

    def Type(self):
        print("Nepal is developing country")

c1=Nepal()
c2=India()

for country in(c1,c2):
    country.Capital()
    country.language()
    country.Type()