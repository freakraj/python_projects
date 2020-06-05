# Exercisse 
#Define a function thast takes a number(n)
# return a dict containing cude of number from 1 to n

# example 
# cube_finder(n)
#{1:1,2:8,3:24}

def cube_finder(n):
     cubes = {}

     for i in range(1,n+1):
       cubes[i]=i**3
     return cubes
print(cube_finder(10))

