# Objectives 
# what is the class 
# How to create a class
#What is init method ,Construction 
# What are attributes ,Instance Variable
# how to create an Object 

class Person:
    def __init__(self,first_name,last_name,age):
        # Instance variable
        print('init methos // Construction')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('raj','gautam',24)
p2 = Person('harshit','mishra',34)

print(p1.first_name)
# print(p2.first_name)

