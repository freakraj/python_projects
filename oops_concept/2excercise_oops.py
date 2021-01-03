# Create a loptop class with attributes like brand name,model name price 
# create to object /instance of your laptop class 

class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name 
        self.price = price
        self.laptop_name = brand + ' ' + model_name


l1 = Laptop('hp','auxtY23',75000)
l2 = Laptop('Dell','amvdr35sdf',45104)

print(f"this your band name {l1.brand} and model name {l2.model_name}")
print(f"this Your Laptop Name :{l2.laptop_name}")