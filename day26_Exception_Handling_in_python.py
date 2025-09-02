# a=input("Enter a number: ")
# i=0
# try:
#  for i in range(1,11):
#    print(f"{int(a)} X {i} = {int(a)*i} ")

# except ValueError as k:
#   print(k)
# #  print("Enter an integer")
# # except Exception as e:
# #   print(e)

try:
    num=(int(input("enter an integer:  ")))
    a=[6,3]
    print(a[num])
except ValueError:
    print("enter an integer")
except IndexError:
    print("Index Error")