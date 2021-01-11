class Person:
    count_obj = 0
    def __init__(self,name,age,email):
        Person.count_obj +=1
        #instance Variable

        self.name = name
        self.age = age
        self.email = email


obj1 = Person('raj gautam',24,'raj@gmail.com')
obj2 = Person('divya',20,'raj@gmail.com')
obj2 = Person('divya',20,'raj@gmail.com')

print(f"{obj1.name} {obj1.age} {obj1.email}")
print(obj1.count_obj)


        