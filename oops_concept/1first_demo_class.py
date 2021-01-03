# OBJECTIVES 
# WHAT IS CLASS
# HOW TO CREATE AN CLASS 
# WHATS IS INIT METHOS
# WHATS ARE ATTRIBUTES , INSTACE VARIABLE
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        # instace variable
        print("init method are construnction are called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','vashistha',24)
p2 = Person('mohit','gautam',25)
print(p1.first_name)
print(p2.first_name)