
# LCM - least common multiple
# 24 - 12, 6, 3
# 22, 12 - 132
# need to check from 1 to product of two numbers
while True:
    # user_input are to end the loop
    user_input_1 = input("enter num-1:")
    user_input_2 = input("enter num-2:")
    if user_input_1 == "exit" or user_input_2 == "exit":
        print("user want to exit")
        break
    else:
        # here user_inputs are data conversion into integer with same variables
        user_input_1 = int(user_input_1) # 24
        user_input_2 = int(user_input_2) # 45 # 1080
        # range is taken from highest to lowest series
        # iterating from min. of two numbers to one in reverse order
        for number in range(max(user_input_1,user_input_2),user_input_1*user_input_2+1):
            if number % user_input_1 == 0 and number % user_input_2 == 0:
                print(f"{number} : is LCM of{user_input_1,user_input_2}")
                break
        # if any negative or non-zero integer given else block will execute
        else:
            print(f"we should pass only non-zer positive numbers, but we got {user_input_1} and {user_input_2}")
# 19@@



















