# advanace min() and max() function 

# number = [1,2,4,5,8]
# print(max(number))
 
 # how to use advance data structure 

name_list = ['harshit','pooja','raj','kk']
# how to find maximum lenght of this name list

# def func(item):
#     return len(item)
# print(min(name_list, key=func))

# using for the lambda function 
# print(max(name_list,key= lambda item:len(item)))



# print(max(student , key = lambda item :item.get('harshit')))

student2 = [

     {'name':'harshit','score':90 , 'age': 24},
     {'name':'mohit', 'score':85, 'age':26},
     {'name':'disha', 'score':95, 'age':18}
]
print(max(student2 , key=lambda item:item.get('score'))['name'])

student = {
    'harshit':{'score':90,'age':25},
    'raj':{'score':58,'age':35},
    'disha':{'score':95,'age':32}
}

print(max(student,key=lambda item : student[item]['score']))