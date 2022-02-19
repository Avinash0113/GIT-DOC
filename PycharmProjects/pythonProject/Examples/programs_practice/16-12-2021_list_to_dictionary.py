# printing the list_1 to list_2 as dictionary
# dict_1 = {}
# list_1 = ["Avinash", "Mahesh", "Raviteja"]
# list_2 = ["Ganesh", "Anjayya", "Umamaheswar"]
# for index in range(0,len(list_1)):
#     dict_1[list_1[index]] = list_2[index]
# print(dict_1)
#

# printing the list_1 to list_2 as reversing the dictionary
# 0 1 2 3 4 5  i
# 5 4 3 2 1 0  len-i-1
#
# dict_2 = {}
# list_1 = ["Avinash", "Mahesh", "Raviteja"]
# list_2 = ["Ganesh", "Anjayya", "Umamaheswar"]
# for i in range(0,len(list_1)):
#     dict_2[list_1[i]] = list_2[len(list_2)-i-1]
# print(dict_2)


# list_1 = []
# string_1 = "Raviteja"
# string_2 = "Mahesh12"
# string_3 = "Bharath1"
# string_4 = "Avinash1"

#max_len = max
# print(max(string_1,string_2,string_3,string_4))
# print(max(len(string_1),len(string_2),len(string_3),len(string_4)))
# max_value = max(len(string_1),len(string_2),len(string_3),len(string_4))
# for index in range(0,max_value):
#     element = string_1[index]+string_2[max_value-index-1]+string_3[index]+string_4[max_value-index-1]
#     list_1.append(element)
# print(list_1)



# printing GCD and highest no
#
# list_1 = []
# num_1 = int(input("enter a no1:"))
# for index in range(1,num_1+1):
#     if num_1 % index == 0:
#         list_1.append(index)
# print(list_1)
#
# list_2 = []
# num_2 = int(input("enter a no2:"))
# for index in range(1,num_2+1):
#     if num_2 % index == 0:
#         list_2.append(index)
# print(list_2)
#
# length_list_1 = len(list_1)
# length_list_2 = len(list_2)
# min_value = min(length_list_1,length_list_2)
# print(min(length_list_1,length_list_2))
#
# for index in range(3,0,-1):
# #for index in range(0,len(list_1)-1,-1):
#     if list_1[index] in list_2:
#         gcd = list_1[index]
#         print("avi",gcd)
#         break
# print("avi1",gcd)

# sum of given no
num = 5698
sum_of_num = 0
while num != 0:
    mod_value = num%10
    print(mod_value)
    sum_of_num=sum_of_num+mod_value
    num = num//10
print(sum_of_num)






# print required fibonacci series
#
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
#
# fib(100)


# initial_value = 1
# for i in range(1,10):
#     print(initial_value)
#     initial_value=initial_value+1
#     if initial_value>4:
#         initial_value=1


# print keys & values as list
# dict_1 = {1:"one",2:"two",3:"three",4:"four"}
# print((list(dict_1.keys())))
# print(list(dict_1.values()))

# print

