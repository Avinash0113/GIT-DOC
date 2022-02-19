string_1="iam learning python madam said to write it in malayalam to convey the matter by using rotator"
words = string_1.split(" ")
count = 0
dict_1 = {}

def is_palindrome(word):
    for letter_index in range(len(word)):
        if word[letter_index] == word[len(word)-letter_index-1]:
            print("--------------------------------------------------------------------")
            print(f"{word}: is a palindrome")
            return True
        else:
            return False

for word_index in range(len(words)):
    # print(words[word_index],end=" ")
    if is_palindrome(words[word_index]):
        count = count+1
print(f"total palindrome's count is :{count}")
# for word in words:
#     print(word)





