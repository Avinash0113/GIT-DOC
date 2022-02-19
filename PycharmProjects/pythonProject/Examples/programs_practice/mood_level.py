PERSON_TEMP = 98
user_name = input("Enter the name:")
user_temp = int(input("Enter the person temp:"))
print(f"Hello {user_name}")
allergy_item = 2
mood = False
if mood:
    print("Go to picnic")
else:
    print("Be in home")
    mood_level = 0
    if mood_level == 0:
        print("Go to home")
    elif mood_level == 1:
        print("Go to hotel")
    elif mood_level == 2:
        print("Go to work")
if user_temp > PERSON_TEMP:
    print("Go out of hotel")
    exit()
else:

    for i in range(1, 6):
        if i != allergy_item:
            print("Eat item", i)
