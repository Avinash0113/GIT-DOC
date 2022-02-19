"""
person_4 = ["Raviteja", "M.Tech", "Buchi", "ECE"]

# outer for loop iterate based on person_4 total length
for outer_index in range(len(person_4)):
    # inner for loop iterate based on element length
    for inner_index in range(len(person_4[outer_index])):
        print(person_4[outer_index][inner_index], end=" ")
print("\n")

"""
"""
# nested for loop

for i in range(1, 3):
    for j in range(1, 3):
        print(i*j, end= " \n")
"""
"""
i = int(input("Enter a no:"))
if i % 2 == 0:
    print("it is even")
else:
    print("it is odd")
"""
"""
#Python program to display all the prime numbers within an interval
a = 1
b = 50
print(f"Prime numbers between 1 and 50:")
for num in range(a, b ):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
"""

"""
number = 17
if number > 1:
for a in range(2, number):
if (number % a)==0:
print(number, "is not a prime number")
break
else:
print(number, "is a prime number")
"""

i = int(input("Enter a no:"))
if i > 1:
    for j in range(2, i):
        if i % j == 0:
            print(i, "is not a prime no")
    else:
        print(i, "is a prime no")
