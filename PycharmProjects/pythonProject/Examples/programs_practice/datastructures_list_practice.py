# person_1 = ["Avinash", "civil", 50, "nellore", "climate", "python"]
"""
person_2 = []
person_3 = list(person_2)
print(person_1, person_2, person_3)

"""
"""

for ele in person_1:
    print(ele, end = " ")
    
"""
"""

for index in range(len(person_1)):
    print(person_1[1])
    
"""

"""
print(person_1[0][5])
"""
"""
person_1 = ["Avinash", "civil", "nellore", "climate", "python"]
for outer_index in range(len(person_1)):
    for inner_index in range(len(person_1[outer_index])):
        print(person_1[outer_index][inner_index], end="")
print("\n")
person_1[2] = "mechanical"
print(person_1)
"""

"""
person_5 = [["Ravi", 4, 5, [1, 289789, "Teja"], "Hello", "hai"], "Travel", 29]
print(person_5[0][3][2][3])
"""
"""
sample_list = [1, 2, 3, 4]
sample_list.append([5, 6, 7])
print(sample_list)

sample_list.extend([8,9,10])
print(sample_list)

"""

"""
college = ["ECE", "CSE", "IT"]
college.append("CIVIL")
print(college)

college.extend("MECH")
print(college)

"""
"""
list_3 = [1, 2, 3, 4]
print("Initial List: ")
print(list_3)
# adds element 12 at index 3
list_3.insert(3, 12)
list_3.insert(0, 'Geeks')
print(list_3)

# it will remove the given value
list_3.remove("Geeks")
print(list_3)
# it will take out last element
list_3.pop()
print(list_3)

list_3.pop(2)
print(list_3)

"""

# person_6 = ["Raviteja", 28, "M.Tech", "Buchi", "ECE", 29, 121, "test", 121, 312, 9.01] starting index(default value
# zero),ending index(default value length of the list), step size(which step u need to print) print(person_6) left to
# right print(person_6[::]) print(person_6[0:2:])

# print(person_6[0:6:2])

# right to left
# print(person_6[0:6:-2])
# print(person_6[6:0:-2])

# print(person_6[-3:4:-3])

# print(person_6[-3::-2])
# print(person_6[-3::2])

# -1 as starting index , -11 ending index with step size 1
# print(person_6[::-1])
# print("________________________________________________________________________________")
# sublists
# person_7 = ["Raviteja", 28, "M.Tech", "Buchi", "ECE", 29, 121, "test", 121, 312, 9.0, 1.14, 8]
# print(person_7[5:9])
# default step size +1 person_7[-5:-9]  equals to person_7[-5:-9:1]
# print(person_7[-5:-9])

# print(person_7[-6:12])
