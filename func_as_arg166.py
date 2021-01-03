# map 
l = [1,2,3,4]

def square(a):
    return a**2 

# print(list(map(square,num)))

def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

print(my_map(lambda a: a**3,l))
