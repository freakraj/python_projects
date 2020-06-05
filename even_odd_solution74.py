
# def even_odd(a,b):
#     if a > b :
#         return a
#     else:
#         return b

# num1= input("Enter your first Number : ")
# num2 = input("Enter your Second number : ")
 
# bigger=even_odd(num1,num2)
# print(f"{bigger} is greater ")

# def filter_odd_even(l):
#     even_num=[]
#     odd_num =[]
#     for i in l :
#         if i%2==0:
#             even_num.append(i)
#         else :
#                 odd_num.append(i)
#     output = [odd_num,even_num]
#     return output 

# number =[1,2,3,4,5,6,7]
# print(filter_odd_even(number))

def filter_odd_even(l):
    odd_num = []
    even_num = []

    for i in l :
        if i%2==0 : # progam logic 
            odd_num.append(i)
        else:
            even_num.append(i)
    output =[odd_num , even_num]
    return output
number = [1,2,3,4,5,6,7,8]
print(filter_odd_even(number))


     
    
