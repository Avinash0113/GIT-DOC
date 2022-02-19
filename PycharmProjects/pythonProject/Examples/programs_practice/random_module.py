import random

# to get the random value from the range
# print(random.randrange(1,100))


# to get the random float value 0.0 - 1
# from random import random
# print(random())


# to get the random value choice from the list
# list_1 =  [12,16,2,5,8,9,19,5,66,99]
# print(random.choice(list_1))


# to get the random value choice from the tuple
# tuple_1 =  [12,16,2,5,8,9,19,5,66,99]
# print(random.choice(tuple_1))


# to get the random-char from the string ( we get output if we give not give the paranthesis also)
# string_1 = ("Avinash")
# print(random.choice(string_1))


# to get the random string from the given strings
# string_1 = ("Avinash", "teja", "bharath", "visu", "mahesh")
# print(random.choice(string_1))


# we get the different list after shuffling every time
# list_1 = [1,2,3,4,5,6,7,8,9]
# (random.shuffle(list_1))
# print(list_1)

# list_1 = ["Avinash", "teja", "bharath", "visu", "mahesh"]
# random.shuffle(list_1)
# print(list_1)


# we can get the random char from string or list by below 2 methods

# string_1 = ("b a v m s t")
# print(random.choice(string_1))

# list_1 =["a","v","b","m","s"]
# print(random.choice(list_1))


# we can get the samples from the list as a (list/tuple/string/set) but we need to give the k: An Integer value, it specify the length of a sample.
# Returns: k length new list of elements chosen from the sequence.
# random.sample(sequence, k)

# from random import sample
# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(sample(list1,4))

# we get the random int value, but we need to give the starting & ending value
# sample = random.randint(1,10)
# print(sample)

