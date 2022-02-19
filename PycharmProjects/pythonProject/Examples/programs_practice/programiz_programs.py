# print("hello world")
"""
a, b = 5, 10
sum = a + b
print(a+b)
"""

"""
a, b = 5, 10
sum = a + b
print("sum of {0} and {1} is {2}".format(a, b, sum))
"""

"""
a = int(input("enter a no:"))
b = int(input("enter a no:"))
sum = a + b
print("sum of {0} and {1} is {2}".format(a, b, sum))
print("-------------------------------------------------")
print(sum)
"""
"""
import math
a = int(input("enter a no:"))
print(math.sqrt(9))
"""
"""
import cmath
a = int(input("enter a no:"))
print(cmath.sqrt(1+2j))
"""
"""
a, b, c = 5, 6, 7
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)
"""
"""
#a = 5
#b = 10
a = int((input("enter a value no:")))
b = (int(input("enter b value no:")))
temp = a
a = b
b = temp
print(" a value after swapping:{}".format(a))
print(" b value after swapping:{}".format(b))

"""
"""
#swapping numbers can be done in above and below types
a, b = 5, 10
a, b = b, a
print("a =", a)
print("b =", b)


"""

"""
import random
print(random.randint(0, 9))

"""
"""
kilometers = float(input("enter a no:"))
conv_fac = 0.62
miles = kilometers * conv_fac
print(kilometers, miles)
"""
"""
#Program to Check if a Number is Positive, Negative or 0

i = int(input("enter a no:"))
if i > 0:
    print("it is positive")
elif i < 0:
    print("it is negative")
else:
    print("it is zero")

"""
"""
# Program to Check if a Number is Odd or Even


i = int(input("enter a no:"))
if i % 2 != 0:
    print("{0} is an odd no".format(i))
else:
    print("{0} is an even no".format(i))
 print("------------------------------------------------")
    

i = int(input("enter a no:"))
if i % 2 ==0:
    print("it is a even no")
else:
    print("it is a odd no")

"""
"""

#Program to Check Leap Year

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

"""
"""

def checkYear(year):
    # Return true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
    import calendar
    return (calendar.isleap(year))
year = int(input("Enter a year: "))
#year = 2000
if (checkYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")

"""
"""

# program to print all Prime numbers in an Interval

start =5
end = 25

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)

"""

"""
#Program to Display the multiplication Table
num = int(input("enter a no:"))
for i in range(1,11):
    print(num, "x", i, "=", num*i)

"""
