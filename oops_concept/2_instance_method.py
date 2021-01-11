# Instance Method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_valid(self):
        return self.age>18 

p1 = Person('raj','gautam',17)
p3 = Person('Disha','gautam',17)
print(p3.full_name())
print(p1.is_valid())
