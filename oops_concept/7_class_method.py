# Instance Method
class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    # instance method    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    # instance method   
    def is_valid(self):
        return self.age>18 
    # class method
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"
p1 = Person('raj','gautam',17)
p3 = Person('Disha','gautam',17)
print(p3.full_name())
print(p1.is_valid())
print(Person.count_instances())