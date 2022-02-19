# list_1=[1,12,3,4,4,3,2,5,6,5,6]
# list_2=[]
# for element in list_1:
#     if element not in list_2:
#         list_2.append(element)
# print(list_2)
import re
string_1="986758h49ghsdfe#$%@3h4"
pattern=re.compile(r"[a-z]+")
# matches=pattern.search(string_1)
# print(matches)
matches=pattern.findall(string_1)
for match in matches:
    print(match,end="")


















