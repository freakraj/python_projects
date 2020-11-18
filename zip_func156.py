# zip function 
user_id = ['user1','user2','user3'] 
name = ['harshit','mohit','rohit']
last_name = ['sharma','gupta','gautam']

# Applying for zip function to give o/p is tuple -(eterable value)

# print(zip(user_id,name))
# output - <zip object at 0x01823F88>
print(list(zip(user_id,name,last_name)))
#output for the tuple pair ->  [('user1', 'harshit'), ('user2', 'mohit'), ('user3', 'rohit')]

example  = [('a',1),('b',2)]
print(dict(example))