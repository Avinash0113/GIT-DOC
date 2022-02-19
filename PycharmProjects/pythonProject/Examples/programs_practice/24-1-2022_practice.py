string_1 = "pavari sarath"
dict_1 = {}

for ele in string_1:
    if ele not in dict_1:
        dict_1[ele] = 1
    else:
        dict_1[ele] += 1

print(dict_1)
# for keys, values in dict_1.items():
#     lsit_1.append(keys)
#     lsit_2.append(values)
# for ele in string_1:
#     if ele not in dict_1:
#         dict_1[ele] = 1
#     else:
#         dict_1[ele] += 1
# for keys, values in dict_1.items():
#     # print()
#     # print(list(zip(keys, values)))
#             # lsit_1.append(keys)
#             # lsit_2.append(values)
#
#
# print(list(zip(lsit_1, lsit_2)))
