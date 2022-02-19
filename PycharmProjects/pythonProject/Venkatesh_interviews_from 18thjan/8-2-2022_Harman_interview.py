string_1="12345LKJHNMS@!@#$5"
string_2="123456789"
for index in range(len(string_1)):
    for element in range(len(string_2)):
        if string_1[index]==string_2[element]:
            print(string_1[index],end="")
print(len(string_1))
# result = string_1.index("123456789")
# print(result)

# list_1=[1,2,3,4,5,6,7,8]
# result=[var for var in list_1 if var % 2 != 0]
# print(result)