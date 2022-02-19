# list_1 = [1,2,3,4,5,8,5,2,3,1,62,1,2]
# print(list(set(list_1)))


list_1 = [1,2,3,4,5,6,7,8,9,1,2,3,4]

list_2 = []
for element in list_1:
    if element not in list_2:
        list_2.append(element)
print(list_2)


