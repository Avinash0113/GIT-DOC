input= [(2, 3), (4, 5), (6, 7), (2, 8)]
#Output= [6, 20, 42, 16]
output=[]
for element in input:
    var_1= element[0]*element[1]
    output.append(var_1)
print(output)