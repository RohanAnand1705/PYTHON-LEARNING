x=4
print(x)

def hello():
    x=5
    y=7
    global z 
    z=8
    print(f"The local x is {x}")

print(f"The global x is {x}")
hello()
x=6
print(f"The global x is {x}") 
# print(y) cant print y cause its not defined globally
# if you try to print y it will give an error because y is a local variable and only exists within the function hello()
# local variables are created when the function is called and destroyed when the function exits
print(z) # we can print z because we declared it as a global variable inside the function hello()
