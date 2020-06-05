
winning_no=27

user_input=input("Guess A number b/w 1 to 100 : ")
user_input=int(user_input)

if winning_no==user_input:
    print("You Win the game !!!")
else: # Nested If Else
    if user_input<winning_no:
         print("To lowww !!")
    else:
         print("To High .......")