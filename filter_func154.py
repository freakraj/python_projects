
# Filter function 

def is_even(a):
    return a%2==0 

number = [2,3,4,5,10,9,7,12]

even = tuple(filter(lambda a : a % 2 == 0,number))
print(even)

# using list comprehension 

new_even = [i for i in number if i%2==0]
print(new_even)