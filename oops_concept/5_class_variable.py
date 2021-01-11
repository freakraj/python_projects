# Class Vriable 
class Circle:
    pi = 3.14 # class Variable
    def __init__(self,radius):
        self.radius = radius  

    def calu_circumference(self):
        return 2*Circle.pi*self.radius

c1 = Circle(4)

print(c1.calu_circumference())

