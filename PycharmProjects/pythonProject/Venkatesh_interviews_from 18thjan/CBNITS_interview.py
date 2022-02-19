#
# list_1= [8,0,0,65,79,0,21,0,0,0,54,12]
# var_1 = list_1[1]
# for element in list_1:
#     if list_1[element]== var_1:
#
#
#
#
# print(sorted(list_1))


# user_input = "ffgyytuuugg"
# converted_list= list(user_input)
# print(converted_list)
# dict_1 = {}
# count = 0
# for element in range(len(converted_list)):
#     if converted_list[element] == dict_1:
#         converted_list[element] +=1
#     else:

list_1 = [1,2,3,4,2,5,6,8,9,10]

initial_value = list_1[0]
count = 0
for element in list_1:
    if list_1[element] > initial_value:
        initial_value = list_1[element]
        count +=1
    else:
        print(initial_value)



