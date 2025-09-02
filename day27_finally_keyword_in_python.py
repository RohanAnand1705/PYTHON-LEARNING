def func1():
    try:
     l= [1,3,5,7]
     i=int(input("enter the index: "))
     print(l[i])
     return 2

    except:
     print("error occured")
     return 3
    finally:  # even after function returns finally still executes
     print("I'm always printed")
y=func1()
print(y)