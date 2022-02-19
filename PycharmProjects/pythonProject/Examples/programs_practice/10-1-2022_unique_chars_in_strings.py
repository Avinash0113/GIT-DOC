string_1 = "abstract"
string_2 = "subject"

list_1 = list(string_1)
print(list_1)
list_2 = list(string_2)
print(list_2)

unique_chars=[]
non_unique_chars = []
for character in list_1:
    if character in list_2:
        unique_chars.append(character)
print(unique_chars) # ['b', 's', 't', 'c', 't']


for character in list_1:
    if character not in list_2:
        non_unique_chars.append(character)

for character in list_2:
    if character not in list_1:
        non_unique_chars.append(character)
print(non_unique_chars)



















