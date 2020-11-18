
# map function 

numbers = [1,2,3,4,5]
def square(a):
    return a**2
squares = list( map(square,numbers))
print(squares)

# using for lambda expresion 
squares = list( map(lambda a : a**2 ,numbers))
print(squares)

# using for list comprihencen 
square_new = [i**2 for i in numbers]
print(square_new) 

new_list = []
for num in numbers :
    new_list.append(square(num))
print(new_list)

naw_names = ['abc','abcd','abcde']
lenght = list(map(len,naw_names))

# for i in lenght :
#     print(i)

print(lenght)