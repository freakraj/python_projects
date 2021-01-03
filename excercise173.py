# excercise decorator

# excercise decorator

import time

def decorator_func():
    

t1 = time.time()
print('this is line one ')
x=5
if x == 5:
    print('x is equal to 5')
print('this is line two ')
t2 = time.time()
print(t2-t1)


def func():
    print('this is function')




# self practice 
# import time
# t1 = time.time()
# # time calculate 
# def decorator_func(any_function):
#     def wrapping_func():
#         print('this is wrapping func')

#         any_function()
#     return wrapping_func


# @decorator_func
# def func():
#     print('this is function')


# t2 = time.time()
# print(t2-t1)
# func()





