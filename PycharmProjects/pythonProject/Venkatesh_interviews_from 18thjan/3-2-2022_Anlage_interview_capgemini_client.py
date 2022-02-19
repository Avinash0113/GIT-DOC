list_1=[5,2,98,12,63,54,12,35,45,78]

for index in range(len(list_1)):
   for element in range(index+1,len(list_1)):
     if list_1[index]>list_1[element]:
        list_1[index],list_1[element]=list_1[element],list_1[index]
print(list_1)
print(list_1[0])
print(list_1[-1])












