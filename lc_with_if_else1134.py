
# list comprehension with if else statement 
num_list = range(1,11)

# num_list_empty = []
# for i in num_list :
#     if i%2 == 0:
#         num_list_empty.append(i*2)
#     else:
#         num_list_empty.append(-i)
# print(num_list_empty)

num_list_empty2 =[ i*2 if (i%2==0) else -i for i in num_list]
print(num_list_empty2)

