
# class Operations():
#     def addition(self):
#

# list_1=[1,2,5,8,9,2,1,45,8,9,3,2,1,2,5,4,7]
# list_2=[1,6,5,9,8,4,5,9]
# dict_1={}
# for index in range(len(list_1)):
#     if list_1[index] not in dict_1:
#         dict_1[list_1[index]]=1
#     else:
#         dict_1[list_1[index]]+=1
# print(dict_1)

# list_1=[1,2,5,8,9,2,1,45,8,9,3,2,1,2,5,4,7]
# list_2=[1,6,5,9,8,4,5,9]
# list_1.append(list_2)
# print(list_1)
# list_1.extend(list_2)
# print(list_1)

# list_2=[1,6,5,9,8,4,5,9]
# list_2.remove(9)
# print(list_2)
#list_2.pop((2),(5))
# del list_2[1]
# print(list_2)

list_2=[1,6,5,9,8,4,5,9]
for index in range(len(list_2)-1):
    if list_2[index]==9:
        del list_2[index]
print(list_2)
        







