# first element should be divided by second number , second number should be divided by third and soo on..
"""
list_1 = [5,6,1,9,52,62,41,32,85]
list_2 = []
for index in range(len(list_1)-1):
    result = list_1[index]/list_1[index+1]
    list_2.append(result)
print(list_2)
"""


# print only duplicate elements from the list
"""
list_1 = ["avi","visu","teja","vishnu","bharath","ganesh","vamsi","ravi","teja","sumanth","bharath","mahesh","bharath"]

dict_1 = {}

for index in range(len(list_1)):
    if list_1[index] not in dict_1.keys():
        dict_1[list_1[index]]=1
    else:
        dict_1[list_1[index]] =dict_1[list_1[index]] + 1
print(dict_1)

"""


list_1 = [1,2,3,4,5,6,7,8,9,3,2,1,1,1,2,4,3]

dict_1 = {}

for index in range(len(list_1)):
    if list_1[index] not in dict_1.keys():
        dict_1[list_1[index]]= 1
    else:
        dict_1[list_1[index]] = dict_1[list_1[index]] + 1
print(dict_1)

for key,value in dict_1.items():
    if dict_1[key]>1:
        print(f"key is:{key} and it occured in list :{value} times")





# print duplicate characters from the string
"""
string_1 = "duplicate characters from the string"
dict_1 = {}

for index in range(len(string_1)):
    if string_1[index] not in dict_1:
        dict_1[string_1[index]] = 1
    else:
        dict_1[string_1[index]]= dict_1[string_1[index]] + 1
print(dict_1)

for key,value in dict_1.items():
    if dict_1[key]>1:
        print(key,value)
"""
"""
list_1 = [1,2,5,0,0,8,3,0,6,1,0,9,0,5,0]

for index in range(len(list_1)):
    if list_1[index]==0:
        list_1.append(list_1[index])
        list_1.remove(list_1[index])
print(list_1)
"""
"""
list_1 = [12,2,1,5,9,1,3,5,7,82,6,5]

for index in range(len(list_1)):
    for element in range(index+1,len(list_1)):
        if list_1[index]>list_1[element]:
            list_1[index],list_1[element] = list_1[element],list_1[index]
print(list_1)
"""

"""
list_1 = [12,2,3,5,9,14,15,35,7,82,6,25]
list_2=[]
while list_1:
    min_num=list_1[0]
    for num in list_1:
        if num<min_num:
            min_num= num
    list_2.append(min_num)
    list_1.remove(min_num)
print(list_2)
"""
"""
list_1 = [12,2,3,5,9,14,15,35,7,82,6,25]
list_2=[]
max_num = list_1[0]
second_max_num=list_1[0]
for index in range(len(list_1)):
    if list_1[index]>max_num:
        max_num=list_1[index]
list_2.append(max_num)
#print(max_num)
for element in range(len(list_1)):
    if list_1[element]<max_num and list_1[element] > second_max_num:
        second_max_num=list_1[element]
list_2.append(second_max_num)
print(list_2)
#print(second_max_num)
"""


# string_1 = "avinash bharath sumanth mahesh visweswar raviteja sarath venkatesh rajesh"
# list_1 = string_1.split()
# print(list_1)
# for index in range(len(list_1)):
#     if "a" in list_1[index]:

































# for index in range(len(list_1)):
#     for element in range(index+1,len(list_1)):
#         if list_1[index]>list_1[element]:
#             list_1[index],list_1[element] = list_1[element],list_1[index]
# print(list_1)
# print(list_1[-1:])


















































































