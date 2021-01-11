class Laptop:
    def __init__(self,brand_name,model_name,price):
        # Instance Variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name


laptopObj = Laptop('HP','auteh36kg3',23423)

print(f"Laptop Detail :\n {laptopObj.brand_name} \n {laptopObj.model_name} \n {laptopObj.price} \n {laptopObj.laptop_name}")
    