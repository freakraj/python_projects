
class Laptop:
    def __init__(self,brand_name,model_name,price):
        # instane variable 
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        # ak aur variable bna skte hai 
        self.laptop_name = brand_name +' '+ model_name

obj = Laptop('dell','I7',25458)
print(obj.brand_name)
print(obj.laptop_name)
