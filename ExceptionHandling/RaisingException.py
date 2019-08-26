try:
    raise NameError("Hi There ")
except NameError:
    print("An exception")
    raise