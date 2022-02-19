import random
import string

count_variable = 0
user_input = "XL"
characters=string.ascii_uppercase
print(characters)
characters_list=list(characters)
print(characters_list)

while True:

    first_char = random.choice(characters_list) # list
    print(f"first_char is : {first_char}")

    second_char = random.choice(characters_list) # list
    print(f"second_char is : {second_char}")

    random_string=first_char+second_char
    print(f"combining first_char and second_char is: {first_char+second_char}")

    if random_string != user_input:
        count_variable = count_variable+1

    else:
        count_variable = count_variable + 1

        print(f"random string : {random_string}  is equal to user input {user_input}")
        break
print(f"total number of comparisions :{count_variable}")