def function():
    print(s)
    #THIS WILL NOT WORK BECAUSE LOCAL VAIRABLE REFERENCED BERFORE ASSIGNMENT
    s="Hello world"
    print(s)
s="hello world"
function()