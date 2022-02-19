# using pop() method
# list_1= [8,0,0,65,79,0,21,0,0,0,54,12]
# for num in list_1:
#     if num == 0:
#        index_num = list_1.index(num)
#        list_1.pop(index_num)
#        list_1.append(num)
# print(list_1)



list_1= [8,0,0,65,79,0,21,0,0,0,54,12]
for index in range(len(list_1)):
    if list_1[index] == 0:
        list_1.append(list_1[index])
        list_1.remove(list_1[index])
print(list_1)



