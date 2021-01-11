# class Mthod as a constructor
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        # instance Variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18
    # class Method
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"
    # this is SELF CREATING constructor
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(",")
        return cls(first,last,age)

    @staticmethod
    def Hello_static():
        print('this is a static Method')

p1 = Person('raj','gautam',17)
p2 = Person('vinod','sharma',21)
p3 = Person.from_string('rahul,sharma,35')


print(p1.count_instance)
print(p1.full_name())
print(p1.is_above_18())
print(Person.count_instances())
print(p3.full_name())
Person.Hello_static()