# list_1 = [1,2,4,5,9,12,98,56,84,72]
# print(len(list_1))
# for element in range(len(list_1)):
#     for value in range(element+1,len(list_1)):
#         if list_1[element] > list_1[value]:
#             list_1[element],list_1[value] = list_1[value],list_1[element]
#
# print(list_1)
# print(sum(list_1[-2:]))
# print(f"second largest number in the list is :{list_1[-2]}")
#

list_2 = [5,6,8,23,56,45,85,96,36,13,56,84,90]
for element in range(len(list_2)):
    for value in range(element+1,len(list_2)):
        if list_2[element]>list_2[value]:
            list_2[element],list_2[value] =list_2[value],list_2[element]
print(list_2)
# print(list_2[-2])
print(len(list_2)//2)
print(list_2[6])






