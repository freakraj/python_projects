# OBJECTIVE 
# WHAT IS CLASS 
# HOW TO CREATE AN CLASS 
# WHAT IS INIT METHOD ,CONSTRUCTOR 
# WHAT ARE ATTRIBUTES ,INSTANCE VARIABLE 
# HOW TO CREATE OUR OBJECT 

class Person:
    def __init__(self,first_name,last_name,age): 
            # Instance variables initialized
        print('init method called')
             #instance variable
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 

  
# Creating object for this class -->jitne bar object bnega utne bar init func call hoga
p1 = Person('raj','gutam',24)
p2 = Person('mohit','chauhan',25)
p3 = Person('mojs','akdjas',23)

print(p1.first_name)
print(p2.last_name)


    