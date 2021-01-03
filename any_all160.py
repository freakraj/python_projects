# any and all function  

number1 = [13,5,9,7,9]  
number2 = [1,2,3,4,5,6]``

even1 = []
for num in number1:
    even1.append(num%2 == 0)
print(even1)
 # -->using for the all function 
# all function for checking the all value are true are not 
# agr sari value true ho gyi to ye  return krega true 

# print(all([True, True, True, False, True]))

# using for the list comprehension 
# print(all([num%2 == 0 for num in number1]))

# using for the any function 
print(any([num%2==0 for num in number1]))