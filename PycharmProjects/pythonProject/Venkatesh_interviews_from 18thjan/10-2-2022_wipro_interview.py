# tuple_1=(2,)
# Input :  arr = [1, 2, 0, 4, 3, 0, 5, 0]
# Output : arr = [1, 2, 4, 3, 5, 0, 0, 0]
# list_1= [1, 2, 0, 4, 3, 0, 5, 0]
# for index in range(len(list_1)):
#     if list_1[index]==0:
#         list_1.append(0)
#         list_1.remove(0)
# print(list_1)
#
# Input= [(2, 3), (4, 5), (6, 7), (2, 8)]
# # Output: [6, 20, 42, 16]
# print(list(Input))

def decorator_function_1(func):
    def function_2(arg1,arg2):
        func(arg1,arg2)
    return function_2

@decorator_function_1
def values(value1,value2):
    print(value1+value2)
values(8,9)

@decorator_function_1
def values(value1,value2):
    print(value1-value2)
values(8,9)

# def method_1():
#     list_1=[1,2,3,4,5]
#     for element in list_1:
#         yield element
#
# for value in method_1():
#     print(value)

























