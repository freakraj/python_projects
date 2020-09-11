
# lambda expresion practice 

def is_even(a):
    if a%2 == 0 :
        return True 
    else :
        return False
print(is_even(6))
#------------------------------------------
# short way to present even odd program 

def is_even(a):
     return a%2==0 # true and false return
print(is_even(6))

This program to will be perform from the the lamda expresion 
lamex = lambda a:a%2 == 0 
print(lamex(6)) 
#------------------------------------------
# print sting last charecter with the hepl of lambda expresion 

def str_func(s):
    return s[-1]
print(str_func("raj"))

last_char =lambda s:s[-1] 
print(last_char('gautam'))

#------------------------------------------
# lambda with if else 

def str_func(s):
    if len(s)>5 :
        return True
    return False 
print(str_func('rajgautam'))

# Using  for lambda expresion 

func = lambda s:True if len(s)>5 else False 
print(func('rajg'))

func = lambda s : len(s) >5
print(func('gau'))