
# split method 
# to convert string to list 
name ,age = 'harshit,24'.split(',')
print(name)
print(age)

name,age=input("please enter your name and age : ").split(',')
print(name)
print(age)

# join method 
# convert list to string 
user_info =['harshit','24']
print(','.join(user_info))