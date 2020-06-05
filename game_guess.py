
winning_number=45
guess=1
number=int(input("Guess a number b/t 1 to 100 : "))
game_over=False

while not game_over:
    if number==winning_number:
        print(f"You win ,and you guess this number in {guess} times ")
        game_over=True 
    else:
        if number<winning_number:
            print("Too low ")
            # guess +=1
            # number=int(input("Please try again ..."))
        else:
            print("Too high ")
        guess +=1
        number=int(input("Please try again ..."))

        # DRY : DON'T REMOVE YOURSELF
===========================================
NAME ="RAJ"

for i in range(len(NAME)):
    print(NAME[i])

=============================================

Ye the python vala tarika

name ="harshit"
for i in name:
    print(i)
==============================================

num =input("Enter Your number : ")
total=0
for i in num:
    total +=int(i)
    print(total)

==============================================

def add_two(a,b):

    return a+b

a=int(input("Please enter your first number : "))
b=int(input("Please enter your second number : "))

total=add_two(a,b)
print(total)
 
 ==========================================================

def add_name(name1,name2):
    return name1+name2

first_name = input("enter your first name: ")
last_name = input("enter your last name : ")

print(add_name(first_name,last_name))

=====================================================

def last_charecter(name):
    return name[-1]

name1=input("enter name : ")
print(f"This is your name last charecter :{last_charecter(name1)} ")

