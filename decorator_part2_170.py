# # decoratores - enhance the functionality of other fucntion 
# @ use for the decoraators

def decorator_func(any_function):
    def wrapper_func(*args,**kwargs):
        print('this is owesome function for raj')
        return any_function(*args ,**kwargs)
    return wrapper_func

# simple printing function 
@decorator_func 
def func1(a):
    print(f'this is the function {a}')

func1(5)        

# simple returning function 
@decorator_func
def func2(a,b):
    return a+b

print(func2(5,2))
