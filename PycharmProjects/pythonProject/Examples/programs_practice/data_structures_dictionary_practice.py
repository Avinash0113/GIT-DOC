dict_3 = {"00001": "bharath", "00002": "avinash", "00003": "visu", "00004": "raviteja"}
print(dict_3)
# dict_3["00004"] = "raviteja pamujula"
# print(dict_3)
# dict_3["00004"] = "ganesh", "vishnu"
# print(dict_3)
print(dict_3["00004"])
print(dict_3.keys())
print(type(dict_3.keys()))
dict_3_keys_list = list(dict_3.keys())
print(dict_3_keys_list)
dict_3_values_list = list(dict_3.values())
print(dict_3_values_list)
# print(dict_3["avinash"])   # if we give the key at run time we get value ,
# but if we give the value at run time it won't print key, it gives the error
