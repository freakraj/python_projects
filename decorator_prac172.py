from functools import wraps


def print_function_data(any_function):
    @wraps(any_function)
    def wrapping_func(*args,**kwargs):
        print(f"this is your own function {any_function.__name__}")
        print(f"{any_function.__doc__}")
        return any_function(*args,**kwargs)
    return wrapping_func


@print_function_data
def add(a,b):
    '''this fucntion takes two number as argument and return their summ '''
    return a+b

print(add(3,5))

# output 
# you are calling and function 
# this fucntion takes two number as parameters and return their sum 
# 8 

