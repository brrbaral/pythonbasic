def number_to_string(argument):
    switcher={
        0:'Zero',
        1:'One',
        2:'Two',
    }
    return switcher.get(argument,"nothing")
if __name__=="__main__":
    argument=0
    print(number_to_string(argument))