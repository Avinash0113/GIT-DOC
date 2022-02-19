# number palindorme to remind bharath tomorrow
"""
num =int(input("enter a number:"))
original_num = num
result=0
while num>0:
    mod=num%10
    result=result*10+mod
    div=num//10
    num=div
print(result)
if original_num==result:
    print("palindrome")
else:
    print("not a palindrome")

"""


# first number to be divided by second and soo on......
"""
list_1 = [1,5,6,2,9,8,2,5,4,85,65,12,32,78]
print(len(list_1))
list_2=[]
for index in range(len(list_1)-1):
    result= list_1[index]/list_1[index+1]
    list_2.append(result)
print(list_2)
print(len(list_2))
"""

# reversing a number
"""
num= 98551368855
result = []
while num>0:
    mod = num%10
    result.append(mod)
    div =num//10
    num =div
print(result)
for value in result:
    print(str(value),end="")
"""




# Get the repeated values, unique values, min and max number
"""
list_1 = [1, 2, 3, 8, 7, 4, 9, 78, 200, 67]
list_2 = [10, 11, 3, 5, 7, 2, 9, 1, 8, 99, 45, 34, 30]
new_list=list_1+list_2
for index in range(len(new_list)-1):
    for element in range(index+1,len(new_list)):
        if new_list[index]>new_list[element]:
            new_list[index],new_list[element]=new_list[element],new_list[index]
print(new_list)
sum_of_max_3_no= new_list[-3:]
print(sum(sum_of_max_3_no))
"""

# print repeated values from the two lists
"""
list_1 = [1, 2, 3, 8, 7, 4, 9, 78, 200, 67]
list_2 = [10, 11, 3, 5, 7, 2, 9, 1, 8, 99, 45, 34, 30]
repeated_values=[]
for index in range(len(list_1)):
    if list_1[index] in list_2:
        repeated_values.append(list_1[index])
print(repeated_values)
"""
# print unique values from the two lists
"""
list_1 = [1, 2, 3, 8, 7, 4, 9, 78, 200, 67]
list_2 = [10, 11, 3, 5, 7, 2, 9, 1, 8, 99, 45, 34, 30]
unique_values=[]
for index in range(len(list_1)):
    if list_1[index] not in list_2:
        unique_values.append(list_1[index])
for index in range(len(list_2)):
    if list_2[index] not in list_1:
        unique_values.append(list_2[index])
print(unique_values)
"""
# appending all 0's at the end of the list
"""
list_1 = [1, 2,0,0, 3, 8, 7,0, 4,0, 9, 78,0,0, 200, 67]
for index in range(len(list_1)):
    if list_1[index]==0:
        list_1.append(0)
        list_1.remove(0)
print(list_1)
"""





































