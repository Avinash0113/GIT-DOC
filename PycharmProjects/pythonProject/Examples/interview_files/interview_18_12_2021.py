# dict_1 = {"Avinash":"Ganesh", "Mahesh":"Anjayya", "Ravi":"Umamaheswar", "Bharath" : "Narasimharao","Sumanth":"Srinivas"}
# # {keys} son of {values}
# # (list_1[index] son of list_2[index])
# list_1= []
# list_2=[]
#
# list_1= list(dict_1.keys())
# list_2= list(dict_1.values())
#
# for index in range(0,len(list_1)):
#     print(f"{list_1[index]} son of {list_2[index]}")
#

class Car():

    def __init__(self,colour,wheels,price):
        self.colour=colour
        self.wheels=wheels
        self.price=price

c=Car("white",4,50000)
print(c.colour,c.wheels,c.price)

