# Dictionary into 
# Q -> why we use dictionary ?
# A -> Because of limitations of list , list are not enough to represent 
# real data 

# Example 
user1= ['raj',24,['coco','kimi no na wa'],['awakening','fairy tale']]

#this list contain  user name ,age ,fav movie ,fav tune 
# you can do this but this is not a good way to do this 

#Q -> What are dictionary 
#A -> Unordered collection of data in key : value pair 

# how to create dictionaryes 

# user = {'name':'raj gautam','age':24,'mobile':98956895745}
# print(user)
# print(type(user))

# Second method to create  dictionary 

std_data =dict(name='raj gautam',age=24,mobile=9865875464,address='kanpur')
print(std_data)
# --------------------------------------------------
# How to access data from dictionary 
# Note -There is no indexing because of unorder collection of data .

print(std_data['name'])
print(std_data['age'])
#------------------------------------------------------
# Which type of data dictionary can store ?
# Anything 
# numbers ,string ,list ,dictionary 

user_info ={
    'name':'raj gautam',
    'age' :23,
    'Fav_movie':['coco','kimi no na wa'],
    'fav_tune':['awakening','fairy tale']
}
print(user_info["Fav_movie"])
print(user_info['fav_tune'])

# how to storee data in dictionary 

user_inf2 ={}

user_inf2['name']='raj gautam'
user_inf2['age'] = 26
user_inf2['mobile']=9865745681
print(user_inf2)