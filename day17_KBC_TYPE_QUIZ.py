l=["delhi","patna","cat","doll","tree"]
print("Enter your name:")
k=input()
print("welcome",k,"let's start the game")
# print("1. What is the capital of india?")
# p =input().lower()
# print("Your answe is",p)
# if p==l[0]:
#   print("You won 10000")
# else:
#   print("LOSER")
#   exit()
# print("2. What is the capital of bihar?")
# q =input().lower()
# print("Your answer is",q)
# if q==l[1]:
#   print("You won 20000")
# else:
#   print("LOSER")
#   exit()
# print("3. Which pet do you have?")
# ko =input().lower()
# print("Your answer is",ko)
# if ko==l[2]:
#   print("You won 30000")
# else:
#   print("LOSER")
#   exit()
# print("4. what do you play with?")
# mn =input().lower()
# print("Your answer is",mn)
# if mn==l[3]:
#   print("You won 40000")
# else:
#   print("LOSER")
#   exit()
# print("5. What is in my lawn?")
# asp =input().lower()
# print("Your answer is",asp)
# if asp==l[4]:
#   print("You won 7000000")
#   print("You won the game")
# else:
#   print("YOU ARE THE BIGGEST LOSER IN THE WORLD")


                          #shorter method

Q=["1. What is the capital of india?","2. What is the capital of bihar?","3. Which pet do you have?","4. what do you play with?","5. What is in my lawn?"]
prize = 0
# for i in range(len(Q)):
#    print(Q[i])
#    if input().lower()==l[i]:
#       print("you won")
#       prize+=10000
#       print("Your prize is",prize)
#       print("You won YAY 🎉🎉🎉🎉🎉")
#    else:
#       print("LOSER BOO")
#       print("You LOST EVERYTHING 🤣🤣🤣🤣🤣")
#       break
# else:
#      print("YOU WON THE GAME")

                     #USING ZIP 
for (y,z) in zip(Q,l):
   print(y)
   if input().lower()==z:
      print("you won")
      prize+=10000
      print("Your prize is",prize)
      print("You won YAY 🎉🎉🎉🎉🎉")
   else:
      print("LOSER BOO")
      print("You LOST EVERYTHING 🤣🤣🤣🤣🤣")
      break
else:
     print("YOU WON THE GAME")