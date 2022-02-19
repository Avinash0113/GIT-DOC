# add two numbers
"""
a,b=5,10
sum=a+b
print(f"sum of two numbers :{sum}")
print("sum of two munbers {0},{1} :".format(a,b),sum)

a,b,c=4,8,12
total=a+b+c
print(f"sum of all numbers:{total}")
print("sum of all numbers {0},{1},{2} :".format(a,b,c),total)
"""

# square root of number
"""
import math
#a=50
a=int(input("enter a number:"))
print(f"{math.sqrt(a):.2f}")
"""
""""
# swaping of two numbers
a,b=90,20
a,b=b,a
print(f"value of a :{a},value of b:{b}")
"""

"""
# generate random number
import random
list_1=[1,5,6,8,9,45,56,1,2]
print(random.choice(list_1)) # it will give random value from the list
print(random.randint(1,50))
print(random.randrange(1,50,5))
print(random.random()) # this will give the random float value from the 0.0 to 1
"""
"""
# check number is +ve,-ve,0
user_input=int(input("enter a no:"))
if user_input>0:
    print(f"{user_input}:  is a +ve number")
elif user_input==0:
    print(f"{user_input}: is equal to 0")
else:
    print(f"{user_input}: is -ve number")
"""

"""
# check the number is even or odd

user_input=int(input("enter a no:"))
if user_input % 2==0:
    print(f"{user_input}: is even number")
else:
    print(f"{user_input}: is odd number")
"""
"""
# find largest number among given
a=int(input("enter a no:"))
b=int(input("enter a no:"))
c=int(input("enter a no:"))
if a>b and a>c:
    print(f"a value: {a} is greater than other two")
elif b > a and b > c:
    print(f"b value: {b} is greater than other two")
else:
    print(f"c value: {c} is greater than other two")

"""



