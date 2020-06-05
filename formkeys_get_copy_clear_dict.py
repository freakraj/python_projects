# fromkeys uses
# d = {'name':'unknown','age':'unknown' }

# Passing list in fromkeys
# d= dict.fromkeys(['name','age','address','city'],'unknown')
# print(d)
#------------------------------------
# passing tuple in fromkeys 
# d = dict.fromkeys(('name','age','address','city'),'Unknown')
# print(d)
#--------------------------------------
# passing string in fromkeys
d = dict.fromkeys('abc','unknown')
print(d)
#------------------------------------
# range function in fromkeys 
# d= dict.fromkeys(range(1,11),'KNOWN VALUE')
# print(d)
#--------------------------------------
# get() method is usefull 

d={
    'name': 'raj gautam',
    'age' : 24,
    'address' : "kanpur"
}

# print(d['names'])

# print(d.get('names')) # Better use according to above
#--------------------------------------------
# if "name" in d:
#     print("Present")
# else :
#         print("Not Present")
#-------------------------------------------------
# if d.get('names'):  # Better way of condition
#     print("Present")
# else : 
#     print("Not Present")

    # if None -------false ,else ------true 

# d.clear()
# print(d)

d1 = d.copy()
# d1 = d
print(d1.popitem())
print(d)


print(d1 is d)