# lst = [12,23,34,5,67,78,56,43,34]
# initial = lst[0]
# for ele in range(0,len(lst)):
#     if lst[ele] > initial:
#         initial = lst[ele]
# print(initial)

list_1 = [12,23,34,5,67,78,56,43,34]

initial_value = list_1[0]
for element in range(len(list_1)):
    if list_1[element]<initial_value:
        initial_value = list_1[element]
print(initial_value)

