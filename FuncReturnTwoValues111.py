
# function returning two values 

def func(int1,int2):
    add=int1+int2 
    multiply = int1 * int2
    return add , multiply

# print(func(2,3)) # out put is tuple value is not to proper way 
adding ,multi =func(25,3.5)
print(adding)
print(multi)