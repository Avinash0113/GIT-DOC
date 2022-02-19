# lambda functions : it is an anonymous function were the function is defined without a name
# and we can pass multiple arguments/parameters and it returns as a single output ,and it is
# similar like return method
# syntax: lambda arguments: expression


# input = lambda a : a*a
# result = input(5)
# print(result)

# input = lambda n:n**2
# result = input(6)
# print(result)

# input=lambda n:n+n
# result=input(50)
# print(result)


# lambda supports 3 functions like: filter(), map(), reduce()
#
#
# def even_list(n):
#     return n % 2==0
# num_1=[1,3,5,6,8,23,22,56,12,69,33,31]
# even_num=list(filter(even_list,num_1))
# print(even_num)
#
# filter() : The filter() function takes all the elements in the list as arguments and
# it filter all the elements of a sequence for which the function returns True
#
# num_1=[1,3,5,6,8,23,22,56,12,69,33,31]
# even_num=list(filter(lambda n :n%2==0,num_1))
# print(even_num)
#
#
# map() : The map() function takes all the elements in the list as arguments and
#  it map each element of a sequence and returns the new list
#
# num_1=[1,3,5,6,8,23,22,56,12,69,33,31] # map() is used to map all the values in the list
# double =list(map(lambda n :n*2,num_1))
# print(double)
#
#
# reduce()  --> while using reduce method we need to import it from functools
# The reduce() function takes all the elements in the list as arguments
# and it performs a repetitive operation over the pairs of the iterable and new reduced result is returned
#
# from functools import reduce
#
# num_1=[1,3,5,6,8,23,22,56,12,69,33,31] # reduce() is used to map all the values in the list
# total_sum =reduce(lambda a,b:a+b,num_1)
# print(total_sum)
