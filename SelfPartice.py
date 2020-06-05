# # # for i in range(1,11):
# # #      print(i,end=" ")

# # def febonacci_series(n):
# #     a=0 #first number   in number ke sath chedchad krenge a = 1
# #     b=1 # second number in number ke sath chedchad krenge  b = 1
# #     if n==1:
# #          print(a)
# #     elif n==2:
# #          print(a,b) # a b ,0 1 
# #     else :
# #          print(a,b , end=" ")
# #          for i in range(n-2):
# #             c = a+b  # c =1 ,2
# #             a = b  # a= 1 ,1 ,2   
# #             b= c  # c  = 1 ,2 ,3
# #             print(b,end=" ")
# # print(febonacci_series(10))

# def febonacci_series(n):
#     a=0 
#     b=1
#     if a==1:
#          print(a)
#     elif b==2:
#          print(a,b)
#     else :
#          print(a,b , end=" ") 
#          for i in range(n-2):
#             c=a+b
#             a=b
#             b=c 
#             print(b ,end = " ")
# print(febonacci_series(10))
        

# def user_info(firstname,lastname="UNKNOWN",age):
#      print(f"your first name is :{firstname}")
#      print(f"Your last name is : {lastname}")
#      print(f"your age is : {age}")

# print(user_info("raj",23))

# def qure_list(l):
# emptylist = []
# for i in range(1,11):
#         emptylist.append(i**2)
# print(emptylist)

# emptylist = [i**2 for i in range(1,11)]
# print(emptylist)

# emptylist = []
# for i in range(1,11):
#     emptylist.append(-i)
# print(emptylist)

# emptylist = [-i for i in range(1,11)]
# print(emptylist)

# names = ['raj','disha','mohit']
# names =list(input("Enter your name comma Saprted : ").split(","))
# emptylist = []
# for name in names : 
#     emptylist.append(name[2])
# print(emptylist)

# emptylist = [name[0] for name in names]
# print(emptylist)

# def reverse_string(l):
#     return [name[::-1] for name in l]
# print(reverse_string(names))
#====================================================

 #names =list(input("Enter your name comma Saprted : ").split(","))
# def reverse_string(l):
#      emptylist = []
#      for name in l:
#          emptylist.append(name[::-1])
#      return emptylist
# print(reverse_string(names))

# list comprehension in if else statement 

# names =list(range(1,11))
# emptylist = []
# for i in names:
#      if i%2==0 :
#          emptylist.append(i)
# print(emptylist)

# emptylist = [i for i in names if i%2==0]
# print(emptylist)

# emptylist = [i for i in range(1,11) if i%2 !=0]
# print(emptylist)

# if conditiopn to print evene number
# number= list(range(1,11))
# num=[]
# for i in number :
#     if i%2==0:
#         num.append(i)
# print(num)
# if condition to print odd number 
# num =[]
# for i in number :
#     if i%2 !=0:
#         num.append(i)
# print(num)

# listr comprehension to print even number 

# number = [i for i in range(1,11)if i%2 == 0]
# print(number)

# how to list print first charecter to print 
# name = list(input("Plese enter your name from comma seprated : ").split(","))

# def reverse_string(l):
#       emptylist=[]
#       for name in l:
#          emptylist.append(name[0])
#       return emptylist
# print(reverse_string(name))


# num = []
# for i in range(1,11):
#     if i%2 !=0 :
#           num.append(i)
# print(num)

# list compreehension to print odd number 
# number = [i for i in range(1,11) if i%2 !=0 ]
# print(number)

# def num_to_string(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float) ]
# print(num_to_string([True , False ,[1,2,3],1,1.0,3]))