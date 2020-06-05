
user_name=input(" Pleae Enter your Name : ")
user_age=input(" Please Enter Your Age : ")

user_age=int(user_age)

if user_age>=15 and (user_name[0]=="a" or user_name[0]=="A"):
     print(f" You are Eligible to Mr :{user_name} \n Required age is Complete : {user_age}\n Keep watching Coco")
else :
    print("You can not coco Movie")
