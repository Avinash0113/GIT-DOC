"""

person = input("Enter the name:")
print(f"hi {person}")
no_need = 7
Con_Temp = 98
person_Temp = int(input(f"Enter {person} Temp:"))
free_time = True
if free_time:
    if person_Temp<Con_Temp:
        print("Go to hospital")
    elif person_Temp == Con_Temp:
        print("Go to restaurent")
    elif person_Temp>Con_Temp:
        print("Go to emergency")

    for i in range(1, 11):
        if i != no_need:
            print("I want", i)

else:
    print("Go to office")

"""
"""
set_1={1,2,3}
print(set_1)
print(type(set_1))

set_2={"bharatth","avi", "visu","mahi"}
set_2.clear()
print(set_2)
"""
"""

#using (CLDR) Common Locale Data Repository Project
# grinning face
print("\N{grinning face}")

# winking face
print("\N{winking face}")

"""
"""
print("\N{money-mouth face}")
# we can print even using unicodes
# print("\U0001f900")

print("\N{winking face}")
"""
"""
# using emoji module

import emoji

print(emoji.emojize(":grinning_face_with_big_eyes:"))
print(emoji.emojize(":winking_face_with_tongue:"))
print(emoji.emojize(":zipper-mouth_face:"))
"""

# < left alignment ^center alignment > right alignment , 10 minimum size guranteeed irrespective of occupancy
String1 = "|{:<10}|{:^10}|{:>10}|".format('Ge', 'formatting12211111', 'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

"""
import itertools, random
# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck)
# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
   """
"""

import random
cards = list(["spade", "heart", "diamond", "club"])
random.shuffle(cards)
print("you got:")
for i in range(5):
    print(cards)
    
    """

import random
import time
starting_time = time.time()

cards = ["king", "queen", "Autin", "diamond", "joker"]
while True:
    if time.time()-starting_time<4:
        # shuffle list every time
        random.shuffle(cards)
        time.sleep(1)
        print(cards)
    else:
        break
