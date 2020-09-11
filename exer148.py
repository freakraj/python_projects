# function 
# list ,reverse_str =True 
# list 

def func(l,**kwargs):
    # get() function dictionary ki key value find krne ke liye krta hai 
     if kwargs.get('reverse_str') == True:
         return [name[::-1].title() for name in l]
     else :
        return [name.title() for name in l]

name =['harshit','mohit']
print(func(name, reverse_str ==True))
# print(func(name))   # O/P --> ['Harshit', 'Mohit']

# AND PASSING FOR THE REVERSE STRING PARAMETER IN FUNCTION 






