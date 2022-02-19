# a1,a2,a3 = (input("Enter the values:")). split()
"""
print(a1)
print(a2)
print(a3)
"""
'''
print("\nage of avi is {0}, \nvishnu is is {1},\ndaday is is {2}".format(a1,a2,a3))
'''

"""
a = int(input("Enter a no:"))
if a % 2 == 0:
   print ("it is even")
else:
    print("it is odd")

"""
'''
for i in range (1, 500):
    if i % 5 == 0:
        print(i)
'''
"""
x = 2, 3, 4
for item in x:
    print(item*2)
"""

'''
x = input("enter the name:")
for i in range (0,len(x)//2):
    if x[i] == x[len(x)-i-1]:
  '''
"""
x=[z**2 for z in range (10) if z>4]
print(x)
"""

"""
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print("\n")
"""

"""
a = 1
b = 2

print(a, b)
#print("a value is  ", a, "b value is ", b)
#print("a value is {}, b value is {}".format(a, b))
#print(f"a value is {a}, b value is {b}")

#print("a value is {0}, b value is {1}".format(a, b))
#print("a value is {1}, b value is {0}".format(a, b))
"""
"""print("Pamujula family members names.{visu} {avi} and {teja}".format(visu="Visweswar", avi= "Avinash", 
teja="Raviteja")) print("Pamujula family members names.{vyshu} {avi} and {poorna}".format(vyshu="\n vishnu priya \n", 
avi="Avinash \n", poorna="Sampoorna")) """

String1 = "\n{0:^20} was founded in {1:<2}!".format("GeeksforGeeks", 2009)
print(String1)
