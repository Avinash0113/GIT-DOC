# import re
# string_1="https://www.interviewbit.com/event/free-mock-coding-interview/?utm_source=ib&utm_medium=top_nudge&utm_campaign=MoCo&utm_content=/practice/"
# # splitted_list = string_1.split("/")
# # print(splitted_list[2])
#
# pattern = re.compile(r"www\.\w+\.com")
#
# matches = pattern.search(string_1)
# print(matches)

"""
string_1="this is python program"
splitted_string_1 = string_1.split(" ")
string_2 ="this is an python program"
splitted_string_2 = string_2.split(" ")
for index in range(len(splitted_string_1)):
    #for word in range(len(splitted_string_2)):
    if splitted_string_1[index] in splitted_string_2:
        print(splitted_string_1)
        break
"""
"""
string_1="this is python program"
splitted_string_1 = string_1.split(" ")
string_2 ="this is an python program"
splitted_string_2 = string_2.split(" ")
for index in range(len(splitted_string_2)):
    #for word in range(len(splitted_string_2)):
    if splitted_string_2[index] not in splitted_string_1:
        print(splitted_string_2[index])
"""
"""
string_1="this is python program"
splitted_string_1 = string_1.split()
list_1 =[]
print(splitted_string_1)
for index in range(len(splitted_string_1)-1,-1,-1):
    list_1.append(splitted_string_1[index])
print(list_1)

reverse=" ".join(list_1)
print(reverse)
"""
"""
string_1="this is python program"
for letter in range(len(string_1)-1,-1,-1):
    print(string_1[letter],end="")
"""
"""
string_1="this is python program"
for character in range(len(string_1)):
    if character % 2 == 0:
        print(string_1[character].upper(),end="")
    else:
        print(string_1[character].lower(),end="")
"""


num =564
while





























