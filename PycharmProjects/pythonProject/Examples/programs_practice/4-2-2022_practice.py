list_1 = [2,3,4,2,5,6,6,8,3,4]

for index in range(len(list_1)):
    for element in range(index+1,len(list_1)):
        if list_1[index]==list_1[element]:
            print(list_1[element],end=" ")


# list_1 = [2,3,4,2,5,6,6,8,3,4]
# list_2=[]
# for element in list_1:
#     if list_1.count(element)==1:
#         list_2.append(element)
# print(list_2)


# for index in range(len(list_1)):
#     for element in range(index+1,len(list_1)):
#         if list_1[index]==list_1[element]:
#             print(list_1[element])

# factorial
#
# num=int(input("enter a no:"))
# initial = 1
# for value in range(num,0,-1):
#     initial=value *initial
# print(initial)
#
# num=int(input("enter anumber:"))
# initial =1
# for value in range(num,0,-1):
#     initial=value*initial
# print(initial)



















