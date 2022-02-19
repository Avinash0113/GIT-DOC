

"""
Input ⇒ Welcome Yagna!  ,   given input string should be reversed, but the condition is that last
                            special character and space between the words should be in its
                            index position even after reversing the string
 this is the expected output
Output ⇒ angaYem ocleW!
"""
string_1 = "Welcome Yagna!"
string_2=""
for char in range(len(string_1)-1,-1,-1):
    string_2+=string_1[char]
var_1=string_2[0]
total=string_2[1:]+var_1
print(total)
# for value in enumerate(total):
#     print(value)
var_2=total[5]
var_3=total[:5]
var_4=total[6:8]
var_5=total[8:]
result=var_3+var_4+var_2+var_5
print(result)
