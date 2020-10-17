
# we use enumerate function with for loop to track position of our 
# items in iterable 


# how we can do this without enumerate function 

# names = ['abc','abcdef','rajgautam']
# pos = 0 
# for name in names : 
#     print(f"{pos} ---> {name}")
#     pos +=1

# with enumerate function  

# for pos,name in enumerate(names):
#     print(f"{pos} -- > {name}")

# defined a function that takes to argument 
# 1.) list containing string    
# 2.) string that want to find your list 
# and this fucntion wwill return the index of string in your list and 
# if string is not present then return -1 

name_collection = ['raj','rahul','riya','disha','rohit']

def find_position(l,target):
    for pos,name in enumerate(l):
        if name == target :
            return pos
    return -1
print(find_position(name_collection,"disha"))

        

           


