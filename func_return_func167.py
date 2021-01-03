# fucntion returning function 

def outer_func():
    def inner_func():
         print('inside inner func')
    return inner_func

var = outer_func()
var()

# how to call function inside function 
def outer_func2(msg):
    def inner_func2():
         print(f"Hello Guyes Kaise Hai {msg}")
    return inner_func2

var = outer_func2("Raj gautam")
var()



    
    