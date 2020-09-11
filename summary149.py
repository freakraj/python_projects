
# simple two number adding parameter program

def func(a,b):
    return a+b

print(func(5,2)) # problem ye hai ki isme sirf hum do number hi add krne ke liye pass kr skte hai

# passing multiple parameter in function --> with the help of *args
# sum multiple number in args
def func2(*args):
    total=0
    for num in args:
        total +=num
    return total

# print(func2(1,2,3,4,5,6,5,4))

#passing list in args and firstly unpacking list 
l=[2,5,3,2] 
print(func2(*l))

# kwargs --> keyword argument ,**kwargs 
def kwargs_func(**kwargs):
#      print(kwargs)

# print dictionary with the help of for loop

     for k,v in kwargs.items():
          print(f"{k}:{v}")
# kwargs_func(first_name='raj',last_name='gautam')

d={'name':'Mahendra pratap','age':55}
#dictonary unpacking 

kwargs_func(**d)


    