a=input("Enter number between 1 and 9: ")
try:
 if  a.lower()=="quit":
   print("Good Job") 
 else:
  if int(a)<1 or int(a)>9 :
   raise ValueError("Between 1 and 9 😠😠😠")

except ValueError as e:
 print(e)