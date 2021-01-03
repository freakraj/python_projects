# fucntion returning function (closure) practice 
# first classv function 

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(3))
