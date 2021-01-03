# decoratores - enhance the functionality of other fucntion 
# decoratores ka kam dusre function ki functionality ko increase krta hai 
# sentacticsugar --> @ use for decorator




def decoratores_function(any_function):
    def wrapper_func():
        print('this is owesome function created with raj guatam')
        any_function()
    return wrapper_func

# this is owesome function 
@decoratores_function # shortcut
def func1():
    print('this is function 1')

func1()
@decoratores_function
def func2():
    print('this is fucntion 2')

func2()

# func1 = decoratores_function(func2)
# func1()