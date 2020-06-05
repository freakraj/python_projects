list comprehencen 
with help of list comprehencen  we can create list in one line 

create a list squre from 1 to 10
squre = []
for i in range(1,11):
     squre.append(i**2)
print(squre)

create list for squre 1 to 10 using comprehencen 

squre = [i**2 for i in range(1,11)]
print(squre)

create a list for 1 to 10 nagetive number 

nagetive = []
for i in range(1,11):
     nagetive.append(-i)
print(nagetive)

create a list from 1 to 10 using comprehencen 

nagetive = [-i for i in range(1,11)]
print(nagetive)

given a list to print the first charecter 

new_list = ['raj','honny','deepak','Harish']
 
new_list2 = []
for new1 in new_list :
    new_list2.append(new1[0])
print(new_list2)


using for list comprehencen 
names_of_std = ['raj','honny','deepak','Harish','Pankaj']
new_list2 = [name[0] for name in names_of_std]
print(new_list2)

 




