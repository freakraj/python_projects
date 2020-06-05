
age=input("Please Enter Your are :")

age=int(age)

if age==0 or age<0:
    print("You can not Watch..")

elif age>0 and age<=3:
         print("Ticket Price : Free .")
elif age>3 and age<=10:
         print("Ticket Price :150 .")
elif age>10 and age<=60:
         print("Ticket Price : 250 ..")
else :
         print("Ticket Price :200")

# ======================================
name="Harshit"
name=input("Please Enter Your Name ")

if "a" in name :
     print("Present IN name ")
else:
     print("Not Present ")
             
