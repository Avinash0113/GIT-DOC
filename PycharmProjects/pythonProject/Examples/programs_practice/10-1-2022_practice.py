# given input should be equal to output

import random

user_input = "GK"
characters = []
char_count = 0
for index in range(65,91):
        characters.append(chr(index))
print(characters)
while True:

        first_char=random.choice(characters)
        print(f"first character is : {first_char}")

        if first_char == user_input[0]:
                char_count = char_count + 1
                print(f"{char_count} char_count for first; matched here")
                while True:
                        second_char = random.choice(characters)
                        random_string = first_char + second_char
                        if random_string == user_input:
                                char_count = char_count + 1
                                print(f"{char_count} char_count for second; matched {random_string}")
                                break
                        else:
                                print(f"{char_count} char_count for second; not  matched ")
                                char_count =char_count + 1
                break
        else:
                print(f"{char_count} char_count for first; not  matched ")
                char_count = char_count + 1




