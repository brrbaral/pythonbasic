def outerFucntion(text):
    text=text

    def innerFunction():
        print(text)

    innerFunction()

#if __name__ == '__main__':
outerFucntion("Hey Python")