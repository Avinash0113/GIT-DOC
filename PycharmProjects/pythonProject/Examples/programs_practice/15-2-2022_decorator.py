def function_decorator_1(func):
    def function_2(arg1,arg2):
        func(arg1,arg2)
    return function_2

@function_decorator_1
def func(arg1,arg2):
    print(arg1+arg2)
func(2,3)

def func(arg1,arg2):
    print(arg1-arg2)
func(2,3)