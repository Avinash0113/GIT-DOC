

list_1 = [1,2,3,4,5,6,7,8,9,1,2,3,4]

# var_1 = list_1[0]
# count = 0
# non_unique = []
for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[i] == list_1[j]:
            break

        count = count + 1
    else:

        non_unique.append(element)
print(non_unique)

# for i in arr:
#         for j in arr:
#             if (arr[i] == arr[j] and i != j):
#                 break
#         if (j == size):
#             count += 1






