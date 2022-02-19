
# Approach:1 - method using loop in list
"""
string_1="iam learning python madam said to write it in malayalam to convey the matter by using rotator"
words = string_1.split(" ")
LOWER_VALUE= 5
UPPER_VALUE= 7

for word_index in range(len(words)):
    if LOWER_VALUE <= len(words[word_index])< UPPER_VALUE:
        print(words[word_index])
"""
# for word in words:
#     if LOWER_VALUE <= len(word)< UPPER_VALUE:
#         print(word)



# Approach:2 - method using function
"""
string_1="iam learning python madam said to write it in malayalam to convey the matter by using rotator"
words = string_1.split(" ")
LOWER_VALUE= 5
UPPER_VALUE= 7

def word_length(word):
    if LOWER_VALUE <= len(word) < UPPER_VALUE:
        print(word)
        return True
    else:
        return False

for word_index in range(len(words)):
    if word_length(words[word_index]):
       print()
"""


# Approach:3 - using dictionary

"""
string_1="iam learning python madam said to write it in malayalam to convey the matter by using rotator"
words = string_1.split(" ")

LOWER_VALUE= 5
UPPER_VALUE= 7
dict_1 = {}
for index in range(len(words)):
    if words[index] not in dict_1:
        dict_1[words[index]]=1
    else:
        dict_1[words[index]] += 1
print(dict_1)
for key,value in dict_1.items():
    #print(key)
    if LOWER_VALUE<=len(key)<UPPER_VALUE:
        print(key,len(key))
"""
















