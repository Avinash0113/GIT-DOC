"""
# divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
a=[]
for i in range(1500, 2701):
    if (i%7==0) & (i%5==0):
        a.append(i)
print(a)
"""
"""

# program to guess a number between 1 to 9
import random
i=random.randint(1,15)
print(i)

"""
"""
# printing stars

i=0
while i<5:
    print("* "*i)
    i=i+1
for j in range(5,0,-1):
        print("* "*j)
"""
"""
# reversing the word

a = input("reverse a word: ")

for char in range(len(a) - 1, -1, -1):
  print(a[char])

"""
"""
a="sword"
print(a[::-1])

"""
"""
# count the number of even and odd numbers from a series
a = 0
b = 0
for i in range(1, 10):
    if i % 2 == 0:
        a += 1
    else i % 2 != 0:
        b += 1
print("even no:", a)
print("odd no:", b)
"""

# count the number of even and odd numbers from a series
x = int(input("enter first no:"))
y = int(input("enter end no:"))
a = 0
b = 0
for i in range(x, y):
    if i % 2 == 0:
        # print("even no:", i)
        a = a + 1
    else:
        # print("odd no:", i)
        b = b + 1
print('Even number:', a)
print('Odd number:', b)
