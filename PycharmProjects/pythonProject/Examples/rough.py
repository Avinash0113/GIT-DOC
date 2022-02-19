"""
a=list[]
for i in range(1, 5, 1):

        print(my_list, end=",")
"""

"""
a = []
s = 0

for i in range(1, 6):
    s = s + i + ','
    print(s)
"""

# print(list(range(10)))
"""
# count the number of even and odd numbers from a series
n=10
a = 0
b = 0
for i in range(1, n):
    if i % 2 == 0:
        a += 1
    else:
        b += 1
print("even no:", a)
print("odd no:", b)

"""

# # 123 sum should be 6
# num = "123"
# initial_num =0
# for char in num:
#     initial_num=initial_num + int(char)
# print(initial_num)

# #[1,2,3,4,5],i=6
# sample_list = []
# for i in range(1,6):
#     sample_list.append(i)
# print(sample_list)


# num = []
# num.append(1)
# num.append(2.5)
# num.append("king")
# print(num)


# sample_list = [1,2,3]
# sample_list.append([4,5,6])
# print(sample_list)


"""
num = int(input("enter a no:"))
#flag = False
a = 0
if num > 1:
    for i in range(2 , num):
        if (num % i) == 0:
            #flag = True
            a = 1
            break
if a:
    print(num, "is not a prime no")
else:
    print(num, "is a prime no")


"""

# prime no or not

# num = int(input("enter a no:"))
# count = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         count = count + 1
# if count == 2:
#     print(num, "is a prime no")
# else:
#     print(num, "is not a prime no")


# a = int(input("enter first no:"))
# b = int(input("enter last no:"))
# x = 1
# for i in range(a, b):
#     if a % i ==0:
#
#         x = 1
# if a:
#     print(a, "is not a prime no")
# else:
#     print(a, "is a prime no")


# # print whether string is a keyword or not
# import keyword
# keys = ["for", "while", "tanisha", "break", "sky",
# "elif", "assert", "pulkit", "lambda", "else", "sakshar"]
#
# for i in range(len(keys)):
#     if keyword.iskeyword(keys[i]):
#         print(keys[i] + " is a keyword")
#     else:
#         print(keys[i] + " is not a keyword")


# # print all keywords
# import keyword
# print(keyword.kwlist)

#
#
# for i in range(10):
#     print(i, end="  ")
#     if i == 6:
#         break
# #print()


# # def keyword
# def fun():
#     print("Inside Function")
# fun()

# Return keyword
# def fun():
#     s = 0
#
#     for i in range(10):
#         s = s + i
#     return s
#
#
# print(fun())


# Yield Keyword
# def fun():
#     S = 0
#
#     for i in range(10):
#         S += i
#         yield S
#
#
# for i in fun():
#     print(i, end=" ")


# as Keyword means alias
# import math as f
#
# print(f.factorial(5))


# # import keyword
# import math
# print(math.factorial(10))
#
# # from keyword
# from math import factorial
# print(factorial(10))


#
# x, y = input("Enter a two value: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)


# import time
#
# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end='>>>')
#         time.sleep(1)
#     else:
#         print('Start')


# for i in range(4):
#     for j in range(i):
#         print("#", end=" ")
#     print(i)


# file1 = open("my file.txt", "r")
# print("Output of Read lines after appending")
# print(file1.read())
# print()
# file1.close()

# with open("file.txt", "w") as f:
#     print(f.write("Hello World!!!"))

# print 123123123

# sample = 1
# for i in range(1, 10):
#     print(sample)
#     sample += 1
#     if sample>3:
#         sample=1

# triangle stars printing pattern

# *
# * *
# * * *
# * * * *
# * * * * *


# for i in range(1,6):
#     for j in range(1,6):

# for i in range(1, 6):
#     print("1 " * i)
#     i += 1

# rows = 6
# for i in range(1, rows):
#         num = 1
#         for j in range(rows, 0, -1):
#             if j > i:
#                 print(" ", end=' ')
#             else:
#                 print(num, end=' ')
#                 num += 1
#         print("")


# for i in range(0,10):
#     print(i)

















