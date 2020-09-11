# funbction with all parameter 
# verry importent to understand 

# PADK 


#parameter 
#args 
# default pameter 
# kwargs 
#-----------------------------------
# def func(name,age='24'):
#      print(name)
#      print(age)

# func('raj gautam',35)
#------------------------------------
# using for all parameter for in fuction in order wise 

def func(name,*args,last_name='Unknown',**kwargs):
     print(name)
     print(args)
     print(last_name)
     print(kwargs)

func('raj gautam',1,2,3,a=1,b=2,father_name='mahendra')

