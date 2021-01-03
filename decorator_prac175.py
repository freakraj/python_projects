from functools import wraps


def only_int_allow(function):
    @wraps(function)
    # this line print for the doc msg and using inbuild function for wrap
    def wrapper(*args,**kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print("invalid arguments")
    return wrapper
    



# this function is how to find total number of list using decorator 
@only_int_allow
def all_add(*args):
    total = 0
    for i in args:
        total +=i 
    return total

print(all_add(1,2,3,4,5,6,[1,2,3]))
print(all_add(1,2,3,4,5,6))