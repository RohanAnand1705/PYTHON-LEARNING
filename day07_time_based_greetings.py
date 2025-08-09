import time
m=time.strftime("%I:%M:%S %p")
print(m)
t=time.strftime("%I")
print(t)
# if(int(t)<12):
#     print("GOOD MORNING")
# elif(int(t)>=12):
#     print("GOOD AFTERNOON")
k=time.strftime("%p")
# # print(k)
# if(k=="AM"):
#     print("GOOD MORNING")
# if(k=="PM"):
#     print("GOOD AFTERNOON")
if(k=="PM") and 1<= int(t) <=3:
    print("GOOD AFTERNOON")
elif(k=="PM") and int(t) ==12:
    print("GOOD AFTERNOON")
elif(k=="PM") and 4<= int(t) <=9:
    print("GOOD EVENING")
elif(k=="AM") and 6<= int(t) <=11:
    print("GOOD MORNING")
else:
    print("GOOD NIGHT")
    
