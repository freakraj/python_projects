class Laptop:
    discount_percent = 10
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand+ ' '+model

    def apply_discount(self):
        off_price=(self.discount_percent/100)*self.price
        return self.price - off_price

# Laptop.discount_percent = 0
lap_obj = Laptop('Lenovo','Ideapad 145',100)
lap_obj2 = Laptop('Dell','Risen x34',60000)
print(lap_obj.__dict__) 
lap_obj2.discount_percent = 50

print(f"Discount:{lap_obj.apply_discount()}\nYour Laptop Detail:\nBrand Name:{lap_obj.brand}\nModel Name:{lap_obj.model}\nReal Price:{lap_obj.price}\nLaptop Name:{lap_obj.laptop_name}")
print(lap_obj2.apply_discount())