# print duplicates
"""

list_1=[1,2,3,4,5,6,4,1,2,3,51,2,3]
list_2=[]
for element in list_1:
    if element not in list_2:
        list_1.append(element)
        print(element)
"""

# list_1=[1,2,3,4,5,6,4,1,2,3,51,2,3]
# del list_1[:4]
# print(list_1)


list_1=[-1,-2,-3,-4,5,6,4,7]
for index in range(len(list_1)):
    if list_1[index]<0:
        print()
