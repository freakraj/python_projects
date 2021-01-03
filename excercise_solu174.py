from functools import wraps
import time

def calculate_time(function):
    @wraps(function)
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        return_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2 - t1 
        print(f'This function took {total_time} seconds')
        return return_value
    return wrapper_func


@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(10)
print(square_finder(10))
        
