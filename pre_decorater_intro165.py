
# you have complete understanding for the functions ,
# first class functon / closeres 
# then finaly we will learn about decoraters 

def square(a):
    return a**2

s = square
print(s.__name__)
print(square.__name__)
print(s)
print(square)
# print(s(5))