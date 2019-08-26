s="hi"
def func():
    global s
    s=50
    print(s)

func()
print(s)