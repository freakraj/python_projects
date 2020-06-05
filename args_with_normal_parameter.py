
# * args with normal parameter 


def multiply_num(para1,para2,*args):

    multy = 1
    for num in args:
        multy *= num 
    return multy 
print(multiply_num(1,2))