
# we use enumerate function with for loop to track  position of our 
# item in iterable 

# how we do can this without enumerate function 

names =['abc','abcds','harshit']

# # 0 --> 'abc'
# # 1 --> 'abcdf' 
# pos = 0
# for name in names :
#      print(f"{pos} -- > {name}")
#      pos +=1

# #out put  is    
# # 0 -- > abc
# # 1 -- > abcds  
# # 2 -- > harshit
# --------------------------------------------


names1 =['abc','raj','harshit']

def find_pos(l,target):
     for pos,name in enumerate(l):
         if name ==target :
             return pos
     return -1 

print(find_pos(names1,'raj'))
        