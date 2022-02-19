"""

var_1 = ()
print(type(var_1))
"""
"""
var_4 = ("avinash")
print(var_4)
print(len(var_4))
print(var_4[2])

var_2 = ("ravi")
print(var_2)
#print(len(var_4))
print(var_2[0])
"""
"""
list_1 = [1, 2, 3, 4]
var_3 = tuple(list_1)
print(var_3)
"""

"""
var_2 = ("bharath", "nellore", 26)
print(var_2)
"""
"""
sample_string = "visu"
#sample_string[1] = "j"
print(sample_string)
sample_string = "Avinash"
print(sample_string)


list_1 = [1,2,3,4]
print(hex(id(sample_string)))
list_1[2]=66
print(hex(id(sample_string)))

sample_string = sample_string.replace("i", "j")
print(sample_string)

"""
"""
tup_1 = (1,2,3)
tup_2 = tup_1*3
tup_3 = tup_1+tup_1
print(tup_2)
print(tup_3)
"""
tuple_5 = 9

for i in range(5):
    tuple_5 = (tuple_5,)  # ((9,),)  (((9,),),)
    print(tuple_5)


def ravi_info_method():
    print("calling some_method")
    # returning multiple inputs (packing)
    return "Raviteja", 28, "Buchi"


def ravi_info_method_nt():
    print("calling some_method")
    # returning multiple inputs (packing)
    return "Raviteja", 28, "Buchi"


# handling multiple returns and unpacking below.
name, age, location = ravi_info_method()
# checking return type of the method
print(type(ravi_info_method()))
print(f"name: {name}, age: {age}, location: {location}")

# returned 3 values and unpacked only 3 values
name, age, location = ravi_info_method_nt()
# checking return type of the method
print(type(ravi_info_method()))
print(f"name: {name}, age: {age}, location: {location}")
print("_____________________________________________________________________________________________________")

# returned 3 values and unpacked only 2 values
# error: ValueError: too many values to unpack (expected 2)
# name,age = ravi_info_method()


# returned 3 values and unpacked only 1 values
name = ravi_info_method()
print(name)

# returned n --> unpacking 1 value(assign returned values as tuple) or n values(assign returned values individually)
