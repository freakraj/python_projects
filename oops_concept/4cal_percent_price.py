class Laptop(object):
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + ' '+ model_name


    def cal_price(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

        
l1 = Laptop('Hp','Aute243hjd',1000)
print(l1.cal_price(10))