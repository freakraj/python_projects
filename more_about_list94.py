
# Genererate list with range funtion 
# Somthing more about pop method 
# Index method 
# pass list to a function 

# number=list(range(1,11))
# poped = number.pop())  # isme pop function return kr rha hai 10 .
# print(number)

# index Method --ager apko perticular list me find krna hai ki element kha pr hai

# num=number.index(1,5)
# print(num)

# Pass list to a function 
number =[1, 2, 3, 4, 5, 6,1, 7, 8, 9,10]


def negative_list(l):
    negative=[]

    for i in l:
        negative.append(-i)
    return negative

print(negative_list(number))