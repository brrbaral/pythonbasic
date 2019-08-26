'''def get_age(age):
    print("you are :",age,"years old")

get_age(20)'''


def get_agewith_assert(age):
    assert (age>0), "Age cannot be negative"
    print("you are", age, "years old")

get_agewith_assert(25)
get_agewith_assert(-3)
