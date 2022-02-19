# interchange first and last element in the list
"""
list_1 = [9,2,3,15,46,16,81,32,53,93]
list_1[0],list_1[-1] = list_1[-1],list_1[0]
print(list_1)
"""



# swap two elements in a list




# find length of the list
# list_1 = [9,2,3,15,46,16,81,32,53,93]
# print(len(list_1))



# maximum element in two numbers
"""
a,b=5,10
if a>b:
    print(f"a value :{a} is greater than b:{b}")
else:
    print(f"a value :{a} is smaller than b:{b}")
"""


# Check if element exists in list
"""
list_1 = [9,2,3,15,46,16,81,32,53,93]
for index in range(len(list_1)):
    if list_1[index]==46:
        print(f"{46} is exists in list")
        print(index)
        print(list_1[index])
"""
"""
list_1 = [9,2,3,15,46,16,81,32,53,93]
if 4 in list_1:
    print(f"{46} exists in the list")
else:
    print(f"{4} not exists in the list")
"""


 # reversing the list

# list_1 = [9,2,3,15,46,16,81,32,53,93]
# for index in range(len(list_1)-1,-1,-1):
#     print(list_1[index],end=" ") # here how can i get the output as list

# list_1 = [9,2,3,15,46,16,81,32,53,93]
# print(list_1[::-1])



# Copying a list to another list
"""
list_1 = [9,2,3,15,46,16,81,32,53,93]
list_2 = []
for index in range(len(list_1)):
    if list_1[index] not in list_2:
        list_2.append(list_1[index])
print(list_2)
"""


# Count occurrences of an element in a list

# list_1 = [1,2,3,4,5,2,2,9,7,2,2,2,6,2,2]
# count = 0
# for index in range(len(list_1)-1):
#     for element in range(index+1,len(list_1)):
#         if list_1[index]=1:
#             break
#         else:
#             count = count+1
#
#
# print(f"most repeated number :{index} and its {count} ")

"""
list_1 = [1,2,3,4,5,2,2,9,7,2,2,2,6,2,2]
dict_1={}

for index in range(len(list_1)):
    if list_1[index] not in dict_1:
        dict_1[list_1[index]]=1
    else:
        dict_1[list_1[index]]+=1
print(dict_1)
for key,value in dict_1.items():
    if dict_1[key]>1:
        print(f"key is :{key} and it's occurence in list is :{value} times")
"""
"""
list_1 = [1,5,6,5,5,5,3,2,1,4,8,9,5,3,1,5,4,7,8,5,3,2,1]
dict_1 = {}
for index in range(len(list_1)):
    if list_1[index] not in dict_1:
        dict_1[list_1[index]]=1
    else:
        dict_1[list_1[index]]+=1
print(dict_1)
for key,value in dict_1.items():
    if value>1:
        print(key,value)

"""

list_1 = [1,2,3,4,5,2,2,9,7,2,2,2,6,2,2]
count = 0
for index in range(len(list_1)-1):
    for element in range(index+1,len(list_1)):
        if list_1[index]=1:
            break
        else:
            count = count+1


print(f"most repeated number :{index} and its {count} ")






















