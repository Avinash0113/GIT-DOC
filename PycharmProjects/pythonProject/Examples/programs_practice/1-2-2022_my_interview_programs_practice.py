"""
list_1=[1,5,3,6,9,5,656,32,41,58,45,78,1,2,36]
list_2=[74,85,96,123,32,65,54,52,36,14,15,1,19]
even_list=[]
odd_list=[]

for index in range(len(list_1)):
    if index%2==0:
        even_list.append(list_1[index])
print(even_list)
for element in range(len(list_2)):
    if element%2!=0:
        odd_list.append(list_2[element])
print(odd_list)
total_list=even_list+odd_list
print(total_list)


"""
"""
string_1 = "Welcome Yagna@"
#Output ⇒ "angaYem ocleW@"
string_2=""
splitted_list=string_1.split()
#for element in range(len(splitted_list)-1,-1,-1):
for value in range(len(string_1)-1,-1,-1):
    string_2=string_2+string_1[value]
print(string_2)
"""

list_1=[1,5,3,6,9,5,656,32,41,58,45,78,1,2,36]
list_2=[74,85,96,123,32,65,54,52,36,14,15,1,19]
list_1.extend(list_2)
print(list_1)








