# Encapsulation -->apne data ko aur uske sath hone functionality ko ak hi jgah pr likhna 
# Abstraction --> user se complexsity ko hide krna hi abstraction khlata hai
# Some special naming convention
# Name mangling , __name (this is not a convention )

class Phone:
    def __init__(self,brand,model_name,price):
        # instance variable
        self.brand = brand
        self.model_name = model_name
        self.__price = price  
        # __price this is special variable python has to be 
        # change this name (_Phone__price)

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

# _name # convention for private name
# __name__ # dunder / magic methods
phone1 = Phone('Nokia','1100',1000)
print(phone1._Phone__price)

print(phone1.__dict__)

# phone1._price = -1000
# print(phone1._price)
