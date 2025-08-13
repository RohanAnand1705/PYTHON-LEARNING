tup= ( 1,3,2,45,78,90,"rohan",2,3.25)
print(type(tup),tup)
print(tup[3:8])
print(tup[-3:8])
# print(tup[3:8])
# if int(input()) in tup:
enter=input()
try:
    val=int(enter)
except ValueError:
    try:
        val=float(enter)
    except ValueError:
     val=(enter)
if val in tup:
    print("yes")
else:
    print("NO,")
