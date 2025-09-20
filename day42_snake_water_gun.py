import random
to_win={"snake":"gun",
        "water":"snake",
        "gun":"water"}
user_input=(input("Enter your choice: ")).lower()
computer_choice=random.choice(list(to_win.keys()))
print("Computer chose:",computer_choice)

if user_input==computer_choice:
    print("Draw")

else:
    print("LOOSER")
