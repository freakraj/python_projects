import copy as cp 
a = [10,20,30]
b= [40,50,60]
c = [a,b] # Nested list

# this is learning print
# print(id(a),id(c[0]))
# print(id(b),id(c[1]))

d = cp.copy(c)
print(id(c)) # c and d both are id is not same using for the shallow copy 
print(id(d)) # ---
#-----------------
print(id(c[0]))
print(id(d[0]))

c[0][0] = 100
print(c)
print(d)
