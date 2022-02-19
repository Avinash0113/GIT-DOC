


"""
string_1="ABC"
string_2="BC"
output_1=""
output_2=""
for index in range(len(string_1)):
    if string_1[index] not in string_2:
        output_1=output_1+string_1[index]
print(output_1)
for char in range(len(string_2)):
    if string_2[char] not in string_1:
        output_2=output_2+string_2[char]
print(output_2)
"""
"""
string_1="BC"
string_2="BANGLORE"
output_1=""
output_2=""
for index in range(len(string_1)):
    if string_1[index] not in string_2:
        output_1=output_1+string_1[index]
print(output_1)
for char in range(len(string_2)):
    if string_2[char] not in string_1:
        output_2=output_2+string_2[char]
print(output_2)
"""

list_1=[("U1","U2"),("U3","U4"),("U1","U5"),("U2","U1"),("U3","U4")]
list_2=[]
for element in list_1:
        if element not in list_2:
            list_2.append(element)
print(list_2)




