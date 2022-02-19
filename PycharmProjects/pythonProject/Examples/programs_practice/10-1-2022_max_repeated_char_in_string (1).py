user_string = "geeksforgeeksisimportant"
dict_1 = {}
for character in user_string:
    if character in dict_1.keys():
        dict_1[character] = dict_1[character] + 1
    else:
        dict_1[character] = 1
print(dict_1)
max_value = max(dict_1.values())
print(max_value)
for key in dict_1.keys():
    if dict_1[key]==max_value:
        print(key)

# for key in dict_1.items():
#     if dict_1[key]==max_value:
#         print(max())
