
class Laptop:
    discount_percent = 10
    def __init__(self,brand,model_name,price):
        # instance variable 
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' '+ model_name

    def apply_dis(self):
        # self.price
        # off_price = (Laptop.discount_percent/100)*self.price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price
      
# abhi tk sare product pr 10 dicount tha sale finis hone ke bad discount zero kr de
# Laptop.discount_percent = 0
laptop1 = Laptop('hp','au114tx',1000)
laptop2 =   Laptop('mac book', 'f11awde',100)

laptop2.discount_percent = 50
# print(laptop1.apply_dis(10))
print(laptop2.__dict__)
print(laptop2.apply_dis())

# How to check laptop Object variable (Means laptop object me kya hai)



