
# kwargs (keyword argument)
# **kwargs  (double start operater)

# kawargs as parameter 
def func(**kwargs):
    # print(type(kwargs))
    # return kwargs

    # how to print dict in for looop
     for k,v in kwargs.items():
         print(f"{k}:{v}")
# dictionary unpacking 
d={'name':'raj','age':24}
func(**d)

# print(func(first_name='raj',last_name='gautam'))


 





