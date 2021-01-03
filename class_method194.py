class Person:
    count_instance = 0 # class Variable / class atributes
    def __init__(self,first_name,last_name,age):
        #instance Variable   
        Person.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age= age
    
    # class Methos constructor 
    @classmethod
    def from_string(cls,string):
        first_name,last_name,age = string.split(',')
        return cls(first_name,last_name,age)

    # static Method --> iska connection kisi se nhi hota hai na hi init constructon se na hi class method se
    @staticmethod
    def hello():
        print('Hello Static Method Called')
    

    # using for the class method 
    @classmethod  
    def count_instances(cls):
        return f"You have created {cls.count_instance} instance of {cls.__name__} class"
 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18
    
p1 = Person('raj','gautam',23)
p2 = Person('raj','gautam',23)
p3 = Person('raj','gautam',23)
p4 = Person.from_string('disha,gautam,17')

print(Person.count_instance)
print(p1.full_name())
print(p1.is_above_18())
print(Person.count_instances())
print(p4.full_name())

print(Person.hello())
