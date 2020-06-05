
# List Squre number 

def negative_sqaure(l):
    negative =[]
    for i in l :
        negative.append(i**2)
    return negative

number = list(range(1,11))    
print(negative_sqaure(number))