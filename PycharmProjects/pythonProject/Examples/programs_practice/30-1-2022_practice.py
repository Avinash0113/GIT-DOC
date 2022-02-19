# count of occurences of character in string
"""
string_1="python is an interpreted language and easy to learn in geeksforgeeks"
count=0
for index in range(len(string_1)):
    if string_1[index]=="a":
        count= count+1
print(f"count of character is: {count}")
"""
"""
string_1="python is an interpreted language and easy to learn in geeksforgeeks"
dict_1={}
for index in range(len(string_1)):
    if string_1[index] not in dict_1:
        dict_1[string_1[index]]=1
    else:
        dict_1[string_1[index]]=dict_1[string_1[index]]+1
print(dict_1)
"""

"""
string_1="in geeksforgeeks python is an an interpreted an language and easy to to learn in an geeksforgeeks"
splitted_list=string_1.split()
print(splitted_list)
dict_1={}
for index in range(len(splitted_list)):
    if splitted_list[index] not in dict_1:
        dict_1[splitted_list[index]]=1
    else:
        dict_1[splitted_list[index]]=dict_1[splitted_list[index]]+1
print(dict_1)
"""

# list_1=[1,2,3,4,5,6,9,8,7,5,3,2,1,5]
# count=0
# for index in range(len(list_1)-1):
#     count=count+index
# print(count)


# list_1 = [333, 893, 1948, 34, 2346]# K = 3
# #Output : [”, 89, 1948, 4, 246]
# for index in range(len(list_1)):
#     list_1[index]=list(str(list_1[index]))
#     for element in range(len(list_1[index])):
#         if list_1[index][element] == "3":
#             list_1[index][element]=""
#     list_1[index]="".join(list_1[index])
#     if list_1[index]!="":
#         list_1[index]=int(list_1[index])
# print(list_1)













