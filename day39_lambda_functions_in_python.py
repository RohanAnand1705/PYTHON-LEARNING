# def double(x):
#     return x * 2
double= lambda x: x*2
cube= lambda x: x*x*x
avg= lambda x,y: (x+y)/2
print(double(5))  
print(cube(5))  
print(avg(4,5))
def apply(fx,value):
    return 6+ fx(value)
print(apply(cube,6))

print(apply(lambda x: x*x*x,2))
