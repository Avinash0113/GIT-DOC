import re

user_string = r"Hello world This is python @ . 984562135 !@#$%^&*+-. and This is end of an the session for day 62"

# ^ carat symbol is used to identify the first letter/word in the string
# pattern = re.compile(r"^Hello") # o/p: <re.Match object; span=(0, 5), match='Hello'>

# print("---------------------------------------------------------------------------------------------------")

# . dot is used to get the single letter starting of the string in search method and in iter method we get each letter as single
# pattern = re.compile(r".") # we get first letter of the string
# pattern = re.compile(r"........") # here we get the letters based on the dots we give we get corresponding letters

# print("---------------------------------------------------------------------------------------------------")

# \. by using backward slash followed by . dot we get the dot wherever it is available in string
# pattern= re.compile(r"\.")

# print("---------------------------------------------------------------------------------------------------")

# + this is used to match 1 or more occurances of the pattern left to it
# pattern = re.compile(r"a+") #( we get the letters followed by + if they are available or else it gives as none)

# print("---------------------------------------------------------------------------------------------------")

# * this is used to match 0 or more occurances of the pattern left to it
# pattern =re.compile(r"nd*")

# print("---------------------------------------------------------------------------------------------------")

# ? this is used to match 0 or 1 occurances of the pattern left to it
# pattern=re.compile(r"nd?")

# print("---------------------------------------------------------------------------------------------------")

# pattern=re.compile(r"nd") # here in double quotes whatever we give we get output, if the match is available in string, else it shows as none

# print("---------------------------------------------------------------------------------------------------")

# square brackets shows a set of characters/available character that we wish to match
# pattern = re.compile(r"[end]")

# print("---------------------------------------------------------------------------------------------------")

# in square brackets if we give lower case,upper case, digits we get all the characters from the string except special characters
# pattern=re.compile(r"[a-zA-Z0-9]")
# pattern=re.compile(r"[a-z]") # we get only lowercase characters
# pattern=re.compile(r"[A-Z]") # we get only uppercase characters
# pattern=re.compile(r"[0-9]") # we get only numeric values

# print("---------------------------------------------------------------------------------------------------")

# if we use ^ carat symbol before alpha-numericals we get spaces,special characters
# pattern=re.compile(r"[^a-zA-Z0-9]")

# print("---------------------------------------------------------------------------------------------------")

# pattern=re.compile(r"56+") # 20@@

# print("---------------------------------------------------------------------------------------------------")

# by using this [0-9]+ we get as the numeric values as a set if they are available in string
# pattern=re.compile(r"[0-9]+") # <re.Match object; span=(31, 40), match='984562135'>

# print("---------------------------------------------------------------------------------------------------")

# by this we get lowercase characters/uppercase characters as a set if they are available in string
# pattern=re.compile(r"[a-z]+") # <re.Match object; span=(1, 5), match='ello'>

# print("---------------------------------------------------------------------------------------------------")

# | this pipe character gives us if any one of the word/character available in the string
# pattern=re.compile(r"is|nd")

# print("---------------------------------------------------------------------------------------------------")

# here also pipe symbol check whether alphabets or numbers are in striing or not
# pattern = re.compile(r"([a-zA-Z]+|[0-9]{10})")

# print("---------------------------------------------------------------------------------------------------")

# $ dollar symbol shows whether the last character is same or not
pattern=re.compile(r"62$") # <re.Match object; span=(94, 97), match=' 62'>








print("-------------------------------search method---------------------------")
matches = pattern.search(user_string)
print(matches)

print("----------------------------find iter method-----------------------------")
matches = pattern.finditer(user_string)
for match in matches:
    print(match)
