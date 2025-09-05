marks=[23,34,45,56,67,89]
# index=0
# for i in marks:
#     print(i)
#     if index==3:
#      print("Good Job")
#     index+=1 

for index, i in enumerate(marks):  #in enumerate, index starts by default from 0
    print(index,i)
    if index==3:
     print("Good Job")

# basically it writes SNo. with output