# list_1 = [2,3,4,5,6,3,9,10,11,12,9,8,7,6]
#
# for index in range(len(list_1)):
#     if list_1[index] < list_1[index + 1]:
#         if list_1[index + 1] < 1:
#             count = count + 1
#     else:
#
#         break
# print(count)


#
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)


from functools import reduce
li = [1,2,3,4]
mul = reduce((lambda x, y: x * y), li)
print (mul)