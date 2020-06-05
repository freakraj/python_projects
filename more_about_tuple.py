
# loopint in tuples 
# TUPLE WITH ONE ELEMNT 
# tuple withouth parenthisis 
# tuple unpacking 
# list inside tuple 
# some function that you can use with tuple 

mixed = (1,2,3,4.0)

# for looping and tuple 
for i in mixed :
    print(i)

# Tuple with one element 
num = (1)
print(type(num)) # this is type of int 

st = ('raj gautam',)
print(type(st)) # this is type of tuple

num1 = (1,)
print(type(num1))


# tuple withouth parenthesis 
guitar = 'yamah','batoh rouge','taylor'
print(type(guitar))

# tuple unpacking - same no of items and same number of variable 

guitarist = ('manali jamal','Eddie van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3=(guitarist)
print(guitarist1)
print(guitarist3)
# -------------------------

# List inside tuple 
favorites = ('southen mangolia',['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
print(favorites)
favorites[1].append("raj gautam")
print(favorites)
