
"""
x = str(input("enter a name:"))
for i in range(0, int(len(x) // 2)):
    if x[i] == x[len(x) - i - 1]:
        continue
    else:
        print("{0} is not a palindrome".format(x))
        break
else:
    print("{0} is a palindrome".format(x))
"""

x = str(input("enter a number:"))

for i in range(0, int(len(x) // 2)):
    if x[i] == x[len(x) - i - 1]:
        continue
    else:
        print("{0} is not a palindrome".format(x))
        break
else:
    print("{0} is a palindrome".format(x))
