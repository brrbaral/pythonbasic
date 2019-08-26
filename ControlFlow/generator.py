def simpleGeneratorFunn():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFunn():
    print(value)