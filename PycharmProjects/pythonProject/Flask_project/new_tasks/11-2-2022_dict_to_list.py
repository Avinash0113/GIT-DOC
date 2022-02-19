
dict_1={"107.99.42.01" : "True", "107.99.42.02":"True", "107.99.42.03" : "True", "107.99.42.04" :  "False",
        "107.99.42.05" : "True", "107.99.42.06" : "True", "107.99.42.07" : "True", "107.99.42.08" : "False",
        "107.99.42.09" : "True", "107.99.42.10" : "True", "107.99.42.11" : "False", "107.99.42.12" : "True",
        "107.99.42.13" : "True", "107.99.42.14" : "True", "107.99.42.15" : "True"}
list_1=[]
#output= [107.99.42.02,True]

for key,value in dict_1.items():
        if value == "True":
                var_1=[key,value]
                list_1.append(var_1)
                #print(key,value)
print(list_1)