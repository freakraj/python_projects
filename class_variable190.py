# class Variable 
#circle
# area 
# circum

# class Circle:
#     def __init__(self,radius,pi):
#         self.radius = radius
#         self.pi = pi 

#     def calc_circumference(self):
#         return 2*self.pi*self.radius

# c = Circle(4,3.14)
# c1 = Circle(5,3.14)
# print(c1.calc_circumference())

# Using for the Class Variable for pie value variable only
class Circle:
    pi = 3.14
    def __init__(self,radius):
        # instance variable
        self.radius = radius

    def calc_circumference(self):
        return 2*Circle.pi*self.radius

p1 = Circle(4)
p2 = Circle(5)
p3 = Circle(6)
print(p3.calc_circumference())




   