import time
def function1_decorator(func):
    def function2(arg1,arg2):
        func(arg1,arg2)
    return function2

@function1_decorator
def values(value1,value2):
    time.sleep(5)
    print(value1+value2)
    time.sleep(5)
    print(value1 + value2)

values(2,3)

# list_1=[2,3,4,5,6,2,3,4]
#
# dict_1={}
# for element in list_1:
#     if element not in dict_1:
#         dict_1[element]=1:
#     else:
#         dict_1[element]+=1
#
# for key,value in dict_1.items():
#     if value>1:
#         print(key)









